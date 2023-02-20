"""
ハローワークの求人情報を検索し結果をCSVファイルに出力する
"""

from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import datetime
import csv, sys, os, subprocess
from tqdm import tqdm
sys.path.append(os.path.dirname(sys.executable))
import settings     # 選択項目を定義している

# Webドライバーに依り対象ブラウザを変える
if settings.executable_path.endswith("geckodriver.exe"):
    from selenium.webdriver.firefox.options import Options
    from webdriver_manager.firefox import GeckoDriverManager
else:
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.hellowork.mhlw.go.jp/kensaku/GECA110010.do?action=initDisp&screenId=GECA110010"
url0 = "https://www.hellowork.mhlw.go.jp/kensaku"

def get_job_dt(url):
    """
    求人情報詳細を開いて「仕事の内容」と「必要な経験など」を取得する

    Args:
        url:    求人情報詳細のURL

    Return:
        「仕事の内容」と「必要な経験など」の文字列
    """
    browser.get(url)
    wait.until(Ec.url_contains(url))
    _text = browser.find_element_by_id("ID_shigotoNy").text # 仕事の内容
    try:    # 必要な経験などがあれば追加する
        _text = _text + "\n【必要な経験など】\n" + browser.find_element_by_id("ID_hynaKikntShsi").text
    except NoSuchElementException:
        pass
    # browser.close()
    return _text

def write_condition(soup):
    """
    求人情報検索の検索条件をテキストファイルに出力する
    ファイルは固定で上書き保存とする
    データを取るのが難しくて保留
    """
# コマンドライン引数からオプションを取得
# オプション    a:結果ファイル起動、b:ブラウザ表示
flag_a = [x for x in sys.argv if x == "a"]
flag_b = [x for x in sys.argv if x == "b"]

try:
    # ブラウザーを起動
    options = Options()             # オプションインスタンス作成
    if not (flag_b or settings.flag_b):
        options.headless = True     # ヘッドレスモード(ブラウザを見せない)
    # Webドライバーに依り対象ブラウザを変える
    if settings.executable_path.endswith("geckodriver.exe"):
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)  # ブラウザインスタンス作成
    else:
        options.add_argument("--disable-software-rasterizer")   # Chromeではこれを付けないとエラー(kFatalFailure)になる(理由はよくわからない)
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)  # ブラウザインスタンス作成

    # 待機
    wait = WebDriverWait(browser, 15)  # Timeout 15秒（最大待ち時間）

    # ハローワーク検索画面にアクセス
    print("start browsing")
    browser.get(url)
    # 求人情報検索画面が表示されるまで待機
    wait.until(Ec.title_contains("求人情報検索"))
    print("got url, start selecting")

    # 検索条件の設定 クリックするもの
    # sttingsから値がTrueで設定されているもので辞書を作成
    _kensaku = {k: v for k, v in settings._kensaku.items() if v and type(v) is bool}
    for id in _kensaku:
        browser.find_element_by_id(id).click()  # チェックボックスをオンにする

    # 検索条件の設定 キー入力するもの
    # sttingsから値が文字列で設定されているもので辞書を作成
    _kensaku = {k: v for k, v in settings._kensaku.items() if v and type(v) is str}
    for id, v in _kensaku.items():
        browser.find_element_by_id(id).send_keys(v)     # 設定文字列をセットする

    # 就業場所の設定
    # 都道府県のselectタグを取得して、ID順にする。
    sels = browser.find_elements_by_tag_name("select")          # selectタグは都道府県のみ
    sels = sorted(sels, key=lambda x: x.get_attribute("id"))    # id属性でソート

    # 市町村選択ボタンのタグを取得して、onclick属性順にする。selectタグと同期させるため。
    # inputタグでvalueが選択を抽出、onclick属性でソート
    buttons = browser.find_elements_by_css_selector("input.button")         # 他のボタンも含まれる
    btns = [x for x in buttons if x.get_attribute("value") == "選択"]       # valueで選別可能
    btns = sorted(btns, key=lambda x: x.get_attribute("onclick"))           # onclick属性にIDが含まれる

    # 就業場所3か所の設定
    for _sel, _btn, _tdk in zip(sels, btns, settings.tdks):
        Select(_sel).select_by_visible_text(_tdk[0])
        if len(_tdk) > 1:   # 市町村を選択する場合
            _btn.click()    # 市町村選択画面表示
            # 選択画面が表示されるまで待つ
            wait.until(Ec.element_to_be_clickable((By.ID, "ID_rank1CodeMulti")))
            element = browser.find_element_by_id("ID_rank1CodeMulti")
            for _city in _tdk[1:]:
                Select(element).select_by_visible_text(_city)
            browser.find_element_by_id("ID_ok").click()    # OKをクリック
            # 選択画面が閉じるまで待つ
            wait.until(Ec.invisibility_of_element_located((By.ID, "ID_ok")))

    # 職種
    # inputタグでvalueが「職種を選択」を抽出、onclick属性でソート
    btns = [x for x in buttons if x.get_attribute("value") == "職種を選択"]
    btns = sorted(btns, key=lambda x: x.get_attribute("onclick"))

    # 職種3か所の設定
    for  _btn, _sksu in zip(btns, settings.sksus):
        _btn.click()    # 職種選択画面表示
        # 選択画面が表示されるまで待つ
        wait.until(Ec.element_to_be_clickable((By.ID, "ID_rank1Code")))
        _sel = browser.find_element_by_id("ID_rank1Code")
        # 大分類選択
        Select(_sel).select_by_visible_text(_sksu[0])   # Selectクラスのインスタンスを作成して選択する
        # 詳細が出るまで待つ
        wait.until(Ec.text_to_be_present_in_element((By.ID, "ID_rank2Codes"), "こだわらない"))
        element = browser.find_element_by_id("ID_rank2Codes")
        for _city in _sksu[1:]:
            Select(element).select_by_visible_text(_city)
        browser.find_element_by_id("ID_ok").click()    # OKをクリック
        # 選択画面が閉じるまで待つ
        wait.until(Ec.invisibility_of_element_located((By.ID, "ID_ok")))
    print("set occupation")

    # 「詳細検索条件」をクリック
    browser.find_element_by_id("ID_searchShosaiBtn").click()
    # 選択画面が表示されるまで待つ
    wait.until(Ec.visibility_of_element_located((By.ID, "ID_saveCondBtn")))

    # 詳細検索条件の設定
    # 詳細検索条件の設定 クリックするもの
    # sttingsから値がTrueで設定されているもので辞書を作成
    _detial = {k: v for k, v in settings._shosai_settei.items() if v and type(v) is bool}
    for id in _detial:
        browser.find_element_by_id(id).click()  # チェックボックスをオンにする

    # 詳細検索条件の設定 キー入力するもの
    # sttingsから値が文字列で設定されているもので辞書を作成
    _detial = {k: v for k, v in settings._shosai_settei.items() if v and type(v) is str}
    for id, v in _detial.items():
        browser.find_element_by_id(id).send_keys(v)     # 設定文字列をセットする

    # 詳細検索条件の設定 要素選択するもの
    # sttingsから値がリストで設定されているもので辞書を作成
    _detial = {k: v for k, v in settings._shosai_settei.items() if v and type(v) is list}
    for id, v in _detial.items():
        Select(browser.find_element_by_id(id)).select_by_visible_text(v[0])     # 設定文字列をセットする
    print("set detailed conditions")

    # 「OK」をクリック
    browser.find_element_by_id("ID_saveCondBtn").click()
    # 選択画面が閉じるまで待つ
    wait.until(Ec.invisibility_of_element_located((By.ID, "ID_saveCondBtn")))
    print("selected, start job search")

    # 「検索」をクリック
    browser.find_element_by_id("ID_searchBtn").click()
    # 0件の時「ご希望の条件に合致する情報は見つかりませんでした」が出る
    # 表示件数選択肢がクリックできるようになるまで待つ
    wait.until(lambda x: 
        Ec.element_to_be_clickable((By.ID, "ID_fwListNaviDispTop"))
                or Ec.text_to_be_present_in_element((By.ID, "msg_area"), "ご希望の条件に合致する情報は見つかりませんでした。"))

    try:    # 検索結果が0件の場合、ID_fwListNaviDispTopが見つからないので例外を出す
        _sel = browser.find_element_by_id("ID_fwListNaviDispTop")
    except NoSuchElementException:
        raise Exception("ご希望の条件に合致する情報は見つかりませんでした")

    Select(_sel).select_by_visible_text("50件")
    # 表示件数選択肢がクリックできるようになるまで待つ
    wait.until(Ec.element_to_be_clickable((By.ID, "ID_fwListNaviDispTop")))
    print("got jobs, start analysis")

    # 今見ているページをBeautifulSoupで解析
    soup = BeautifulSoup(browser.page_source, "html.parser")

    write_condition(soup)

    # 「求人」のテーブルを検索
    jobs = soup.find_all("table", class_="kyujin")

    _table = []
    _csv_header = []
    # jobsの要素を処理し、プログレスバーを表示する。
    for job in tqdm(jobs, unit="件", ncols=75):
        # 1度だけCSVのヘッダーとなる情報を取得する
        # 見出しとなるタグにはfbクラスが設定されている。
        if not _csv_header:
            _csv_header = [x.get_text(strip=True) for x in job.select("td.fb")]

        # 職種の取得
        head = [job.find("td", class_="m13").get_text()]
        # 求人区分から公開範囲の取得
        body1 = [x.get_text(strip=False) for x in job.select("tr.border_new td:not([class])")]
        # 期限、特徴などの取得
        body2 = [x.get_text(" ", strip=True) for x in job.select("tr:not([class]) > td:not([class])")]
        # 詳細情報のURL取得 相対アドレスが返るので、外部アドレスに変える。
        foot = [url0 + job.find("a", id="ID_dispDetailBtn")['href'][1:]]
        # 詳細情報の仕事を取得し、置き換える。仕事の内容は、4番目
        shigoto = [get_job_dt(foot[0])]
        body1[3:4] = shigoto
        # 1件分のデータを設定
        _table.append(head + body1 + body2 + foot)

except TimeoutException:
    print("ブラウザタイムアウト プログラム要調査")
except Exception as identifier:
    print("プログラムのブラウザ操作エラー", identifier)
finally:
    # ブラウザーを終了
    browser.quit()
print("analyzed, start writing csv")

# CSVに出力
output_path = '{}.csv'.format(datetime.datetime.now().strftime("%m%d_%H%M_%S"))

try:
    with open(output_path, encoding="cp932", mode="w", newline="") as f:
        _writer = csv.writer(f)
        _writer.writerow(_csv_header)   # 見出しを出力
        _writer.writerows(_table)       # データを出力
except Exception as e:
    print("CSVエラー", e)

print("finished")

# CSVファイルをファイル名を指定して起動する。関連付けされている必要がある。
if (flag_a or settings.flag_a):
    subprocess.Popen(["start", output_path], shell=True)    
    
