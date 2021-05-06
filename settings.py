# ドライバ(geckodriver.exe)のパスを指定 exeファイル名を含めること
executable_path = "C:\MyProgram\geckodriver.exe"

# 選択項目

# 都道府県 3つまで 市町村は5つまで
tdks = [
          ["東京都", "千代田区"]
        , ["東京都", "港区"]
        , ["埼玉県"]
        ]

# 職種 3つまで
sksus = [["技術職（建設、開発、ＩＴ）、専門職", "ソフトウェア開発技術者、プログラマー", "その他の情報処理・通信技術者"]
        , ["事務、管理職", "一般事務、事務補助"]
        ]

_kensaku = {	
	  "ID_kSNoJo": ""						# text 求人番号
	, "ID_kSNoGe": ""						# text 求人番号
	, "ID_kjKbnRadioBtn1": False			# radio 一般求人
	, "ID_ippanCKBox1": True				# checkbox フルタイム
	, "ID_ippanCKBox2": False				# checkbox パート
	, "ID_kjKbnRadioBtn2": False			# radio 新卒・既卒求人
	, "ID_kjKbnRadioBtn3": False			# radio 季節求人
	, "ID_kjKbnRadioBtn4": False			# radio 出稼ぎ求人
	, "ID_kjKbnRadioBtn5": False			# radio 障害のある方のための求人
	, "ID_sGSYACKBox1": False				# checkbox フルタイム
	, "ID_sGSYACKBox2": False				# checkbox パート
	, "ID_nenreiInput": "60"				# text 年齢
	, "ID_nenreiCKBox1": False				# checkbox 不問のみ
	, "ID_nenreiCKBox2": False				# checkbox 不問をのぞく
	, "ID_sKGYBRUIJo1": ""					# text 職業分類
	, "ID_sKGYBRUIGe1": ""					# text 職業分類
	, "ID_sKGYBRUIJo2": ""					# text 職業分類
	, "ID_sKGYBRUIGe2": ""					# text 職業分類
	, "ID_sKGYBRUIJo3": ""					# text 職業分類
	, "ID_sKGYBRUIGe3": ""					# text 職業分類
	, "ID_koyoFltmCKBox1": False			# checkbox 正社員
	, "ID_koyoFltmCKBox2": False			# checkbox 正社員以外
	, "ID_koyoFltmCKBox3": False			# checkbox 有期雇用派遣労働者
	, "ID_koyoFltmCKBox4": False			# checkbox 無期雇用派遣労働者
	, "ID_koyoPartCKBox5": False			# checkbox パート労働者
	, "ID_koyoPartCKBox6": False			# checkbox 有期雇用派遣パート
	, "ID_koyoPartCKBox7": False			# checkbox 無期雇用派遣パート
	, "ID_newArrivedCKBox1": False			# checkbox 新着（当日・前日）の求人情報から検索
	, "ID_newArrivedCKBox2": True			# checkbox 新着（１週間以内）の求人情報から検索
	, "ID_freeWordRadioBtn0": False			# radio ＯＲ検索
	, "ID_freeWordRadioBtn1": False			# radio ＡＮＤ検索
	, "ID_freeWordInput": ""				# text フリーワード
	, "ID_nOTKNSKFreeWordInput": ""			# text をのぞく
	, "ID_kJNoJo1": ""						# text 求人番号
	, "ID_kJNoGe1": ""						# text 求人番号
	, "ID_kJNoJo2": ""						# text 求人番号
	, "ID_kJNoGe2": ""						# text 求人番号
	, "ID_kJNoJo3": ""						# text 求人番号
	, "ID_kJNoGe3": ""						# text 求人番号
	, "ID_kJNoJo4": ""						# text 求人番号
	, "ID_kJNoGe4": ""						# text 求人番号
	, "ID_kJNoJo5": ""						# text 求人番号
	, "ID_kJNoGe5": ""						# text 求人番号
	, "ID_jGSHNoJo": ""						# text 事業所番号
	, "ID_jGSHNoChuu": ""					# text 事業所番号
	, "ID_jGSHNoGe": ""						# text 事業所番号
	}

_shosai_settei = {    
      "ID_shoyoAriCKBox1":  False				#checkbox",,あり
	, "ID_shgJnStaJiCmbBoxHH": []				#select時(0-23)["8"]と指定、時と分はセットで指定
	, "ID_shgJnStaFunCmbBoxMM": []				#select分(0,10,20,30,40,50)
	, "ID_shgJnEndJiCmbBoxHH": []				#select時(0-23)["8"]と指定、時と分はセットで指定
	, "ID_shgJnEndFunCmbBoxMM": []				#select分(0,10,20,30,40,50)
	, "ID_kiboShgJnCKBox1":  False				#checkbox",,交代制（シフト制）を含まない
	, "ID_kiboShgJnCKBox2":  False				#checkbox",,裁量労働制を含まない
	, "ID_kiboShgJnCKBox3":  False				#checkbox",,変形労働時間制を含まない
	, "ID_jkgiRadioBtn0":  False				#radio",,指定しない
	, "ID_jkgiRadioBtn1":  False				#radio",,あり
	, "ID_jkgiRadioBtn2":  False				#radio",,なし
	, "ID_thkin":  ""			        		#text",
	, "ID_holidayCKBox1":  False				#checkbox",,月曜日
	, "ID_holidayCKBox2":  False				#checkbox",,火曜日
	, "ID_holidayCKBox3":  False				#checkbox",,水曜日
	, "ID_holidayCKBox4":  False				#checkbox",,木曜日
	, "ID_holidayCKBox5":  False				#checkbox",,金曜日
	, "ID_holidayCKBox6":  True				#checkbox",,土曜日
	, "ID_holidayCKBox7":  True				#checkbox",,日曜日
	, "ID_holidayCKBox8":  True				#checkbox",,祝日
	, "ID_shukFtskRadioBtn0":  False			#radio",,指定しない
	, "ID_shukFtskRadioBtn1":  True			#radio",,毎週
	, "ID_shukFtskRadioBtn2":  False			#radio",,その他
	, "ID_hakenUkeoinCKBox1":  False			#checkbox",,派遣
	, "ID_hakenUkeoinCKBox2":  False			#checkbox",,請負
	, "ID_hakenUkeoinCKBox3":  False			#checkbox",,派遣・請負を含まない
	, "ID_kanyuHknCKBox1":  False				#checkbox",,雇用保険
	, "ID_kanyuHknCKBox2":  False				#checkbox",,労災保険
	, "ID_kanyuHknCKBox3":  False				#checkbox",,健康保険
	, "ID_kanyuHknCKBox4":  False				#checkbox",,厚生年金
	, "ID_kanyuHknCKBox5":  False				#checkbox",,公務災害補償
	, "ID_kanyuHknCKBox6":  False				#checkbox",,財形
	, "ID_kanyuHknCKBox7":  False				#checkbox",,企業年金
	, "ID_kanyuHknCKBox8":  False				#checkbox",,退職金制度
	, "ID_kanyuHknCKBox9":  False				#checkbox",,退職金共済
	, "ID_keiyakuKsnNoKnsiAriCKBox1":  False	#checkbox",,あり
	, "ID_knsiAriCKBox1":  False				#checkbox",,原則更新
	, "ID_knsiAriCKBox2":  False				#checkbox",,条件あり
	, "ID_tnseiRadioBtn0":  False				#radio",,指定しない
	, "ID_tnseiRadioBtn1":  False				#radio",,あり
	, "ID_tnseiCmbBox":  []						#select歳以上(60-70)
	, "ID_tnseiRadioBtn2":  False				#radio",,なし
	, "ID_nyukyoKaCKBox1":  False				#checkbox",,単身用あり
	, "ID_nyukyoKaCKBox2":  False				#checkbox",,世帯用あり
	, "ID_riyoKanoNaTjsAriCKBox1":  False		#checkbox",,あり
	, "ID_jgshMeiIn":  ""						#text",
	, "ID_nozokuCKBox1":  False					#checkbox",,のぞく
	, "ID_jginSuRadioBtn0":  False				#radio",,指定しない
	, "ID_jginSuRadioBtn1":  False				#radio",,１０人以上
	, "ID_jginSuRadioBtn2":  False				#radio",,１００人以上
	, "ID_jginSuRadioBtn3":  False				#radio",,３００人以上
	, "ID_jginSuRadioBtn4":  False				#radio",,１０００人以上
	, "ID_kiboSuruSngBrui1In":  ""				#text",
	, "ID_kiboSuruSngBrui2In":  ""				#text",
	, "ID_kiboSuruSngBrui3In":  ""				#text",
	, "ID_grkiFumonCKBox1":  False				#checkbox",,不問
	, "ID_hynaKikntFumonCKBox1":  False			#checkbox",,不問
	, "ID_hynaMenkyoSkkuFumonCKBox1":  False	#checkbox",,不問
	, "ID_jdsMenkyoCKBox1":  False				#checkbox",,必須
	, "ID_jdsMenkyoCKBox2":  False				#checkbox",,あれば尚可
	, "ID_jdsMenkyoCKBox4":  False				#checkbox",,必須・あれば尚可をのぞく
	, "ID_jdsMenkyoCKBox3":  False				#checkbox",,AT限定可
	, "ID_menkyoSkku1In":  ""					#text",
	, "ID_menkyoSkkuNo1CKBox1":  False			#checkbox",,のぞく
	, "ID_menkyoSkku2In":  ""					#text",
	, "ID_menkyoSkkuNo2CKBox1":  False			#checkbox",,のぞく
	, "ID_menkyoSkku3In":  ""					#text",
	, "ID_menkyoSkkuNo3CKBox1":  False			#checkbox",,のぞく
	, "ID_sonotaCKBox1":  False					#checkbox",,書類選考なし
	, "ID_sonotaCKBox2":  False					#checkbox",,正社員登用あり
	, "ID_sonotaCKBox3":  False					#checkbox",,マイカー通勤可
	, "ID_sonotaCKBox4":  True					#checkbox",,転勤の可能性なし
	, "ID_sonotaCKBox5":  False					#checkbox",,在宅勤務
	, "ID_sonotaCKBox6":  False					#checkbox",,駅近（最寄り駅から徒歩１０分以内）
	, "ID_sonotaCKBox7":  False					#checkbox",,屋内の受動喫煙対策あり
	, "ID_sonotaCKBox8":  False					#checkbox",,トライアル雇用併用求人
    , "ID_sonotaCKBox9":  False					#checkbox",,UIJターン歓迎求人
    }