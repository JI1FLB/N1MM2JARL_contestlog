#------------------------------------------------------------------------
#
#   サマリーシート作成ツール v.0.1 
#  
#       (c) 2024/12/16 Seiichi Tanaka JI1FLB


def summary_maker():
    from bs4 import BeautifulSoup
    import sys
    import TkEasyGUI as eg
    from pathlib import Path
    import chardet
    import datetime


    global  contestname , categorycode , callsign , opcallsign , totalscore ,address , name , tel , email , licensedate , age , power , fdcoeff , opplace , powersupply , comments , multioplist , regclubnumber , oath , date , signature , filename , enc

    filename = "summarysheet.txt"

    layoutsummary = [[eg.Button("ファイルの新規作成", key = "btn0" ),eg.Button("ファイル読込", key ="btn1"),eg.Button("ファイルの保存", key ="btn2"),eg.Button("終了", key ="btn3")],
            [eg.Text("コンテストの名称:"),eg.Input(  key = 'disp_contestname' ,size = (35,1) )],
            [eg.Text("参加部門種目コードナンバー:"),eg.Input( key = 'disp_categorycode' , size = (6,1))],
            [eg.Text("コールサイン:"),eg.Input( key = 'disp_callsign' , size = (10,1))],
            [eg.Text("ゲストオペ運用者のコールサイン:"),eg.Input( key = 'disp_opcallsign' , size = (10,1))],
            [eg.Text("総得点:"),eg.Input( key = 'disp_totalscore' , size = (8,1))],
            [eg.Text("連絡先住所:"),eg.Input( key = 'disp_address' , size = (80,1))],
            [eg.Text("氏名(クラブ局の名称):"),eg.Input( key = 'disp_name' , size = (60,1))],
            [eg.Text("電話番号:"),eg.Input( key = 'disp_tel' , size = (15,1))],
            [eg.Text("E-mailアドレス:"),eg.Input( key = 'disp_email' , size = (40,1))],
            [eg.Text("局免許年月日:"),eg.Input( key = 'disp_licensedate' , size = (22,1))],
            [eg.Text("年齢:"),eg.Input( key = 'disp_age' , size = (3,1))],
            [eg.Text("コンテスト中使用した最大空中線電力(W):"),eg.Input( key = 'disp_power' , size = (4,1))],
            [eg.Text("フィールドデーコンテストの場合の局種係数:"),eg.Input( key = 'disp_fdcoeff' , size = (2,1), text_align = "right")],
            [eg.Text("運用地:"),eg.Input( key = 'disp_opplace' , size = (80,1))],
            [eg.Text("使用電源:"),eg.Input( key = 'disp_powersupply' , size = (50,1))],
            [eg.Text("意見:"),eg.Multiline( key = 'disp_comments' , size = (80,5))],
            [eg.Text("マルチオペ種目運用者のコールサインまたは氏名:")],
            [eg.Text("       "),eg.Multiline( key = 'disp_multioplist' , size = (80,2))],
            [eg.Text("登録クラブ番号:"),eg.Input( key = 'disp_regclubnumber' , size = (40,1))],
            [eg.Text("宣誓文:"),eg.Multiline( key = 'disp_oath' , size = (80,4))],
            [eg.Text("日付:"),eg.Input( key = 'disp_date' , size = (22,1)),eg.Button("日付の記入", key = "filldate")],
            [eg.Text("署名:"),eg.Input( key = 'disp_signature' , size = (40,1))],
            [eg.Text("サマリーシート作成ツール v.0.1 (c) 2024/12/16 Seiichi Tanaka JI1FLB" , font= ("Times",9))],
            ]
    win = eg.Window( "サマリーシート作成ツール【JARL v.2.1用】", layoutsummary )


    #   日付の記入

    def fillindate():
        now = datetime.datetime.now()
        win[ "disp_date" ].update( f"{now:%Y年%m月%d日}" )
        date = v["disp_date"]
        

    def redisplaysummary():
    
        win[ "disp_contestname" ].update( contestname )
        win[ "disp_categorycode" ].update( categorycode )
        win[ "disp_callsign" ].update( callsign )
        win[ "disp_opcallsign" ].update( opcallsign )
        win[ "disp_totalscore" ].update( totalscore )
        win[ "disp_address" ].update( address )
        win[ "disp_name" ].update( name )
        win[ "disp_tel" ].update( tel )
        win[ "disp_email" ].update( email )
        win[ "disp_licensedate" ].update( licensedate )
        win[ "disp_age" ].update( age )
        win[ "disp_power" ].update(  power )
        win[ "disp_fdcoeff" ].update( fdcoeff )
        win[ "disp_opplace" ].update( opplace )
        win[ "disp_powersupply" ].update( powersupply )
        win[ "disp_comments" ].update( comments )
        win[ "disp_multioplist" ].update( multioplist )
        win[ "disp_regclubnumber" ].update( regclubnumber )
        win[ "disp_oath" ].update( oath )
        win[ "disp_date" ].update( date )
        win[ "disp_signature" ].update( signature )

    #
    #   summaryシートを閉じる
    #

    def closesummary():
        with open( filename,"rb") as f:
            f.close()


    #
    #   summaryシートの読み込み
    #

    def opensummary():

        global  contestname , categorycode , callsign , opcallsign , totalscore ,address , name , tel , email , licensedate , age , power , fdcoeff , opplace , powersupply , comments , multioplist , regclubnumber , oath , date , signature , filename , enc



        with open( filename,"rb") as f:
            b = f.read()
            enc = chardet.detect(b)["encoding"]
            p = Path( filename )
            summary_contents = p.read_text(encoding = enc)

        soup = BeautifulSoup(summary_contents, 'html.parser')

        elm01 = soup.select_one('CONTESTNAME')
        if len(elm01) >= 1 :
            contestname = elm01.contents[0].strip()
        else :
            contestname = ""

        elm02 = soup.select_one('CATEGORYCODE')
        if len(elm02) >= 1 :
            categorycode = elm02.contents[0].strip()
        else :
            categorycode = ""
        
        elm03 = soup.select_one('CALLSIGN')
        if len(elm03) >= 1 :
            callsign = elm03.contents[0].strip()
        else :
            callsign = ""
        
        elm04 = soup.select_one('OPCALLSIGN')
        if len(elm04) >= 1 :
            opcallsign = elm04.contents[0].strip()
        else :
            opcallsign = ""

        elm05 = soup.select_one('TOTALSCORE')
        if len(elm05) >= 1 :
            totalscore = elm05.contents[0].strip()
        else :
            totalscore = ""

        elm06 = soup.select_one('ADDRESS')
        if len(elm06) >= 1 :
            address = elm06.contents[0].strip()
        else :
            address = ""

        elm07 = soup.select_one('NAME')
        if len(elm07) >= 1 :
            name = elm07.contents[0].strip()
        else :
            name = ""

        elm08 = soup.select_one('TEL')
        if len(elm08) >= 1 :
            tel = elm08.contents[0].strip()
        else :
            tel = ""

        elm09 = soup.select_one('EMAIL')
        if len(elm09) >= 1 :
            email = elm09.contents[0].strip()
        else :
            email = ""

        elm10 = soup.select_one('LICENSEDATE')
        if len(elm10) >= 1 :
            licensedate = elm10.contents[0].strip()
        else :
            licensedate = ""

        elm11 = soup.select_one('AGE')
        if len(elm11) >= 1 :
            age = elm11.contents[0].strip()
        else :
            age = ""
        
        elm12 = soup.select_one('POWER')
        if len(elm12) >= 1 :
            power = elm12.contents[0].strip()
        else :
            power = ""

        elm13 = soup.select_one('FDCOEFF')
        if len(elm13) >= 1 :
            fdcoeff = elm13.contents[0].strip()
        else :
            fdcoeff = ""

        elm14 = soup.select_one('OPPLACE')
        if len(elm14) >= 1 :
            opplace = elm14.contents[0].strip()
        else :
            opplace = ""

        elm15 = soup.select_one('POWERSUPPLY')
        if len(elm15) >= 1 :
            powersupply = elm15.contents[0].strip()
        else :
            powersupply = ""    

        elm16 = soup.select_one('COMMENTS')
        if len(elm16) >= 1 :
            comments = elm16.contents[0].strip()
        else :
            comments = ""        

        elm17 = soup.select_one('MULTIOPLIST')
        if len(elm17) >= 1 :
            multioplist = elm17.contents[0].strip()
        else :
            multioplist = ""      

        elm18 = soup.select_one('REGCLUBNUMBER')
        if len(elm18) >= 1 :
            regclubnumber = elm18.contents[0].strip()
        else :
            regclubnumber= ""

        elm19 = soup.select_one('OATH')
        if len(elm19) >= 1 :
            oath = elm19.contents[0].strip()
        else :
            oath = ""

        elm20 = soup.select_one('DATE')
        if len(elm20) >= 1 :
            date = elm20.contents[0].strip()
        else :
            date = ""

        elm21 = soup.select_one('SIGNATURE')
        if len(elm21) >= 1 :
            signature = elm21.contents[0].strip()
        else :
            signature = ""


    def elementprintoutText() :
        prinText(contestname)
        prinText(categorycode)
        prinText(callsign)
        prinText(opcallsign)
        prinText(totalscore)
        prinText(address)
        prinText(name)
        prinText(tel)
        prinText(email)
        prinText(licensedate)
        prinText(age)
        prinText(power)
        prinText(fdcoeff)
        prinText(opplace)
        prinText(powersupply)
        prinText(comments)
        prinText( multioplist )
        prinText(regclubnumber)
        prinText( oath )
        prinText( date )
        prinText( signature )


    def savesummary():

        contestname = v["disp_contestname"]
        categorycode = v["disp_categorycode"]
        callsign = v["disp_callsign"]
        opcallsign = v["disp_opcallsign"]
        totalscore = v["disp_totalscore"]
        address = v["disp_address"]
        name = v["disp_name"]
        tel = v["disp_tel"]
        email = v["disp_email"]
        licensedate = v["disp_licensedate"]
        age = v["disp_age"]
        power = v["disp_power"]
        fdcoeff = v["disp_fdcoeff"]
        opplace = v["disp_opplace"]
        powersupply = v["disp_powersupply"]
        comments = v["disp_comments"]
        multioplist = v["disp_multioplist"]
        regclubnumber = v["disp_regclubnumber"]
        oath = v["disp_oath"]
        date = v["disp_date"]
        signature = v["disp_signature"]

        summaryoutput = "<SUMMARYSHEET VERSION=R2.1>\n" + "<CONTESTNAME>" + contestname + "</CONTESTNAME>\n"+ "<CATEGORYCODE>" +  categorycode + "</CATEGORYCODE>\n" + "<CALLSIGN>" + callsign + "</CALLSIGN>\n" + "<OPCALLSIGN>"+ opcallsign + "</OPCALLSIGN>\n" + "<TOTALSCORE>" + totalscore + "</TOTALSCORE>\n" + "<ADDRESS>" + address + "</ADDRESS>\n" + "<NAME>" + name + "</NAME>\n"+   "<TEL>" + tel + "</TEL>\n"+ "<EMAIL>" + email + "</EMAIL>\n" +  "<LICENSEDATE>" + licensedate + "</LICENSEDATE>\n" + "<AGE>" + age + "</AGE>\n" + "<POWER>" + power + "</POWER>\n" + "<FDCOEFF>" + fdcoeff + "</FDCOEFF>\n"+ "<OPPLACE>" + opplace + "</OPPLACE>\n" + "<POWERSUPPLY>" + powersupply + "</POWERSUPPLY>\n" + "<COMMENTS>" + comments + "</COMMENTS>\n" + "<MULTIOPLIST>" + multioplist + "</MULTIOPLIST>\n"+ "<REGCLUBNUMBER>" + regclubnumber + "</REGCLUBNUMBER>\n" + "<OATH>" + oath +" </OATH>\n" + "<DATE>" + date + "</DATE>\n" + "<SIGNATURE>" + signature + "</SIGNATURE>\n" + "</SUMMARYSHEET>\n"

        with open( filename , "w", encoding='UTF-8') as f:
            f.write( summaryoutput )
            f.close()

    def create_summary() :
        summaryoutput = "<SUMMARYSHEET VERSION=R2.1>\n" + "<CONTESTNAME>" + "" + "</CONTESTNAME>\n"+ "<CATEGORYCODE>" +  "" + "</CATEGORYCODE>\n" + "<CALLSIGN>" + "" + "</CALLSIGN>\n" + "<OPCALLSIGN>"+ "" + "</OPCALLSIGN>\n" + "<TOTALSCORE>" + "" + "</TOTALSCORE>\n" + "<ADDRESS>" + "" + "</ADDRESS>\n" + "<NAME>" + "" + "</NAME>\n"+   "<TEL>" + "" + "</TEL>\n"+ "<EMAIL>" + "" + "</EMAIL>\n" +  "<LICENSEDATE>" + "" + "</LICENSEDATE>\n" + "<AGE>" + "" + "</AGE>\n" + "<POWER>" + "" + "</POWER>\n" + "<FDCOEFF>" + "" + "</FDCOEFF>\n"+ "<OPPLACE>" + "" + "</OPPLACE>\n" + "<POWERSUPPLY>" + "" + "</POWERSUPPLY>\n" + "<COMMENTS>" + "" + "</COMMENTS>\n" + "<MULTIOPLIST>" + "" + "</MULTIOPLIST>\n"+ "<REGCLUBNUMBER>" + "" + "</REGCLUBNUMBER>\n" + "<OATH>" + "" +" </OATH>\n" + "<DATE>" + "" + "</DATE>\n" + "<SIGNATURE>" + "" + "</SIGNATURE>\n" + "</SUMMARYSHEET>"

        with open( filename , "w+", encoding='UTF-8') as f:
            f.write( summaryoutput )
            f.close()


    while True :
        e, v =win.read()
        if e == "btn0":
            create_summary()
        if e == "btn1" :
            opensummary()
            redisplaysummary()
        if e == "btn2" :
            savesummary()
        if e == "btn3" :
            break
        if e == "filldate" :
            fillindate()
        if e is None :
            break

    win.close()

if __name__=="__main__":
    summary_maker()
