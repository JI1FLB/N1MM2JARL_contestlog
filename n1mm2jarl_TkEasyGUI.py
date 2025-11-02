import TkEasyGUI as eg
#from Phase0 import phase0
from Phase0_1 import phase0_1
from Phase1 import phase1
from Phase2 import phase2
from Phase3 import phase3
from summary_parameters import summarysheet2parameters
from QSO_db_maker_rev2 import QSO_db_maker
from summary_maker_eg import summary_maker
# from jarl2txlog import jarl2txlog


import subprocess

global folder_path, form_file, adif_file, log_file , HL_file, Ph0_data , Callsign , FD_coe , Contest_name , Multi ,Remarks1 , My_multi , Guest , FD_contest , Multi_Op , Contest_type , AA_contest , Power_code , JST_convert_flag , QSLyesno , summary2parameter

#   ウインドウのレイアウト
layout_contestlog = [
        [eg.Text("N1MM ADIFファイル to JARLコンテストログ作成ツール【JARL v.2.1用】", font= ("HGP行書体",14))],
        [eg.Text("")],
        [eg.Button("サマリーシート作成",key= '-summary_maker-')],
        [eg.Text("")],
        [eg.Button("QSO DB ライブラリ作成",key= '-qso_db-')],
        [eg.Text("")],     
        [eg.Text("★ログ作成パラメータ")],
        [eg.Text("              "),eg.Text("コールサイン ："),eg.Text( '-Callsign-' )],
        [eg.Text("              "),eg.Text("局 種 係 数 ："),eg.Text( '-FD_coe-' )],
        [eg.Text("              "),eg.Checkbox( 'UTC時刻をJSTに変換',key = '-JST_convert_flag' )],
        [eg.Text("              "),eg.Checkbox( 'QSLを発行',key = '-QSLyesno' )],
        [eg.Text("              "),eg.Checkbox( '1.2Gバンド以上のパワーコード変換 M -> L',key = '-Power_code' )],
        [eg.Text("              "),eg.Checkbox( 'ALL Asia DX Contestに参加',key = '-AA_contest' )],
        [eg.Text("              "),eg.Checkbox( '2TX部門に参加',key = '-Division_2TX' )],       
        [eg.Text("              自局のマルチ   "),eg.Input( key = '-My_Multi' , size = (7,1))],
        [eg.Text("              Hamlog Remark1"),eg.Input( key = '-Remarks1' , size = (50,1))],
        [eg.Text("              "),eg.Button("パラメータ設定", key = '-setup_parameter-' , text_color="red", background_color="lightblue")],
        [eg.Text("")],
        [eg.Button("コンテストログ生成", key = '-log_create-' )],
        [eg.Text("")],
        [eg.Button("終了", key ="-close_btn-")],
        [eg.Text("")],
        [eg.Text("サマリーシート作成ツール v.0.2 (c) 2025/05/05 Seiichi Tanaka JI1FLB" , font= ("Times",9))],
]

#   ウインドウの作成
win = eg.Window( "N1MM ADIFファイル to JARLコンテストログ作成ツール【JARL v.2.1用】", layout_contestlog )


# パラメータ
folder_path : str = ""
form_file : str = ""
adif_file : str = ""

log_file : str = ""
HL_file : str = ""


#　変数の定義
Ph0_data : list = []
Callsign : str = ""
FD_coe : int = 1
Contest_name : str = "" 
Multi : str = ""
Remarks1 : str = ""
My_multi : str =""
Guest : bool = False
FD_contest : bool = False
Multi_Op : bool = False
Contest_type : bool = False
AA_contest: bool = False
Power_code : bool = False
JST_convert_flag : bool = False
QSLyesno : bool = False
Division_2TX : bool = False

def data_clear():
    Remarks1.delete()
    My_multi.delete()
    Guest.set(False)
    FD_contest.set(False)
    Multi_Op.set(False)
    Contest_type.set(False)
    AA_contest.set(False)
    Power_code.set(False)
    JST_convert_flag.set(False)
    QSLyesno.set(False)
    Division_2TX.set(False)
    form_file.set('')
    adif_file.set('')


def log_generate() :
    Guest_op =Guest
    FD = FD_contest
    Mop = Multi_Op

    Contest_name = phase0_1( Callsign )
    
    print(FD_coe)

#  Phase1を起動
#       ADIFファイルのログライン分割を1ラインに修正
    phase1( Callsign , Division_2TX )

#  Phase2を起動
#     スコアサマリーの生成、JARLサマリーシートへ得点を転記
    phase2( Callsign , FD_coe , Contest_name )

# Phase3を起動
    Multi = My_multi
    QSL = QSLyesno
    JST_conv = JST_convert_flag
    Power = Power_code
    AA = AA_contest
    
    phase3( Callsign , Contest_name, QSL, JST_conv, Power, Multi, AA, Remarks1, Division_2TX )


while True :
    e, v =win.read()

    if e == "-close_btn-" :
        break

    if e == "-summary_maker-" :
        # command = ["python","summary_maker_eg.py"]
        # proc = subprocess.Popen(command)
        # proc.communicate()
        summary_maker()
        parameters = summarysheet2parameters()
        # コールサインと局種別係数をアップデート
        Callsign = parameters[0]
        FD_coe = int( parameters[1] ) 
        win["-Callsign-"].update ( Callsign )
        win["-FD_coe-"].update ( FD_coe ) 

    if e== "-qso_db-" :
        # command = ["python","QSO_db_maker_rev2.py"]
        # proc = subprocess.Popen(command)
        # proc.communicate()
        QSO_db_maker()

    # if e== "-2tx-" :
    #     jarl2txlog( Callsign )

    if e == "-setup_parameter-" :
        parameters = summarysheet2parameters()
        Callsign = parameters[0]
        FD_coe = int( parameters[1] )
        win["-Callsign-"].update ( Callsign )
        win["-FD_coe-"].update ( FD_coe )
        JST_convert_flag = v['-JST_convert_flag']
        QSLyesno = v['-QSLyesno']
        Power_code = v['-Power_code']
        AA_contest = v['-AA_contest']
        My_multi = v["-My_Multi"]
        Remarks1 = v["-Remarks1"]
        Division_2TX = v["-Division_2TX"]

    if e == "-log_create-" :
        log_generate()

    if e == None :
        break

win.close()
