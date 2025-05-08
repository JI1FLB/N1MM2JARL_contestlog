#------------------------------------------------------------------------
#
#   QSO DB library 生成ツール rev.2
#  
#       (c) 2025/05/07 Seiichi Tanaka JI1FLB

def QSO_db_maker() :
    import TkEasyGUI as eg
    import os
    import pickle


    #   ウインドウのレイアウト
    layout_qso_db = [
        [eg.Text("QSO DB library 生成ツール rev.2", font= ("HGP行書体",14))],
        [eg.Text("")],
        [eg.Button( '新規dB作成（空ファイル））',key = '-create_qso_db-' ),eg.Button("ライブラリ作成", key = '-QSO_db_lib-'),eg.Button("終了", key ="-close_btn-")],
        [eg.Text("")],
        [eg.Text("QSO DB library 生成ツール v.0 rev.2 (c) 2025/05/07 Seiichi Tanaka JI1FLB" , font= ("Times",9))]
    ]

    #   ウインドウの作成
    win = eg.Window( "QSO DB library 生成ツール rev.2", layout_qso_db )

    #

    # パラメータ
    adif_file = set()
    ask_adif_file = set()
    QSO_DB = set()


    # adif.adiファイル選択ボタンの動作

    def ask_adif(): 
        global ask_adif_file

        ask_adif_file = eg.popup_get_file( message = "HamlogのADIFファイルを選択してください" , file_types = [("ADIFトファイル", "*.adi"), ("すべてのファイル", "*")] )


    def QSO_db_lib():

    #------------------------------------------------------------------------
    #
    #   ファイルネーム（コールサイン）の入力
    #

        global ask_adif_file

        forming_file =  "temp_forming.adi"
        file_name = ask_adif_file
        
        adif_file = open(file_name,"r",encoding='utf-8')
        output_log = open(forming_file ,"w",encoding='utf-8')


    #------------------------------------------------------------------------
    #
    # ADIFファイルが改行分割されたレコードを1レコードに編集
    #
    #

        data1 = ""

        lines = adif_file.readlines()

        for line in lines:
            
            if "<CALL:"  in line:
                
                if "<EOR>" in line:
                    data1=line
                    output_log.write(data1)
                    continue
                
                data1=line.rstrip('\n')
                continue
            
            if "<CALL:" not in line:
                
                if "<EOR>" in line:
                    data1=data1 + line
                    output_log.write(data1)
                    data1 = ""
                    continue
                
                data1= data1 + line.rstrip('\n')
                continue

            output_log.write(line)
            
        adif_file.close()
        output_log.close()

    #-----------------------------------------------------------------------------

        file_name = ""
        db_file = ""
        Callsign = ""

        temp_adif_file ="temp_forming.adi"
        db_file =  "Callsign_db.txt"

        #--------------------------------------------------------------------
        #
        #   ファイル名の定義
        #

        file_name=ask_adif_file
        adif_log = open( temp_adif_file ,"r",encoding='utf-8')
        qsodb_log = open( db_file ,"w",encoding='utf-8')

        logs = adif_log.readlines()

        #--------------------------------------------------------------------
        #
        #   変数宣言
        #

        data=""
        data1=""
        data2=""
        data3=""

        log = ""
        i=0

        a = ""
        b = ""
        c = ""

        CALL = ""
        FREQ = ""
        MODE = ""
        SUBMODE =""

        line = ""

    #----------------------------------------------------------------------------
        #--------------------------------------------------
        #
        #   N1MM Logger+が出力しないADIFパラメータ対策
        #

        #line = "年月日" +" "+ "時分" +" "+ "バンド" +" "+ "モード" +" "+ "交信局" +" "+ "送信RST" +" "+ "送信ナンバー" +" "+ "受信RST" +" "+ "受信ナンバー" +" "+ "マルチ" +" "+ "得点"+ "\n"
        
        #logsheet.write(line)

        for log in logs:

            if "CALL:" not in log :
                CALL = " "

            if "GRIDSQUARE:" not in log :
                GRIDSQUARE = " "

            if "BAND:" not in log :
                BAND = " "

            if "CONTEST_ID:" not in log :
                CONTEST_ID = " "

            if "<MODE:" not in log :
                MODE = " "

            if "<SUBMODE:" not in log :
                SUBMODE = " "

                
        #--------------------------------------------------
        #
        #       JARL LOG作成　　ADIFフォーマットから要素抽出
        #
                
            log = log.replace(' "','')
            log = log.rstrip('\n')
            log = log.lstrip()
            log = log.split("<")

            for i in log:

                if "CALL:" in i :
                    a = i
                    b = a[5:7]
                    b1= b.rstrip(">")
                    b2 = len(b1)
                    CALL = a[6+b2:7+b2+int(b1)]
                    CALL = CALL.rstrip()

                if "BAND:" in i:
                    a = i
                    b = a[5:7]
                    b1= b.rstrip(">")
                    b2 = len(b1)
                    BAND = a[6+b2:7+b2+int(b1)]
                    BAND = BAND.rstrip()
                    BAND = BAND.upper()

                if "CONTEST_ID:" in i:
                    a = i
                    b = a[11:13]
                    b1= b.rstrip(">")
                    b2 = len(b1)
                    CONTEST_ID = a[12+b2:13+b2+int(b1)]
                    CONTEST_ID = CONTEST_ID.rstrip()
                
    # 2019/12/10 WSJTXのADIFファイルに対応するため、iの部分一致から特定文字の完全一致へ変更
                    
                if "MODE:" == i[:5] :
                    a = i
                    b = a[5:7]
                    b1= b.rstrip(">")
                    b2 = len(b1)
                    MODE = a[6+b2:7+b2+int(b1)]
                    MODE = MODE.rstrip()
                    
    # 2019/12/10 WSJTXのADIFファイルに対応するため、SUBMODEを追加
    # 2019/12/10 WSJTXのADIFファイルに対応するため、iの部分一致から特定文字の完全一致へ変更

                if "SUBMODE:" == i[:8] :
                    a = i
                    b = a[8:10]
                    b1= b.rstrip(">")
                    b2 = len(b1)
                    SUBMODE = a[9+b2:10+b2+int(b1)]
                    SUBMODE = SUBMODE.rstrip()             

        #--------------------------------------
        #
        #   QSO DBファィル出力
        #
        
            db_data = CALL+'-'+BAND+'-'+MODE+'\n'
            QSO_DB.add( db_data )

        for l in sorted( QSO_DB ) :
            qsodb_log.write( l )
            
        adif_log.close()
        qsodb_log.close()

    #tempファイルの削除
        os.remove(temp_adif_file)

    #「pickle」での書き出し
        f = open('QSO_DB_lib.txt', 'wb')
        pickle.dump(QSO_DB, f)
        f.close()

    # ライブラリー作成完了の通知

        eg.popup('作成状態 : QSO_DB_libの作成完了' )
        
        return

    #--------------------------------------------------------------------
    #   空ファイルの作成
    #--------------------------------------------------------------------
    def create_qso_db() :

        with open('QSO_DB_lib.txt', 'wb') as f :
        #--------------------------------------
        #   QSO DBファィル出力
        #       2025/05/08 0byteではEOFerrorを生じるためにダミーデータでDBを作成
        
            db_data = "JA1QRZ"+'-'+"40m"+'-'+"CW"+'\n'
            QSO_DB.add( db_data )
            pickle.dump(QSO_DB, f)

            f.close()


    # 
    while True :
        e, v =win.read()
        if e == "-create_qso_db-" :     #   空ファイルの作成
            create_qso_db()
        if e == "-QSO_db_lib-" :       #   ライブラリの作成"
            ask_adif()
            QSO_db_lib()
        if e == "-close_btn-" :
            break
        if e == None :
            break
    win.close()

if __name__=="__main__":
    QSO_db_maker()

