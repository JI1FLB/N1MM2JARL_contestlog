from bs4 import BeautifulSoup
import sys
import TkEasyGUI as eg
from pathlib import Path
import chardet


global contestname , categorycode , callsign , opcallsign , totalscore ,address , name , tel , email , licensedate , age , power , fdcoeff , opplace , powersupply , comments , multioplist , regclubnumber , oath , date , signature , filename , enc
global parameters

filename = "summarysheet.txt"
parameters = []


#
#   summaryシートの読み込み
#

global  callsign , fdcoeff

filename = "summarysheet.txt"

def summarysheet2parameters():

    parameters = []         #   パラメータ　リスト要素のリセット

    with open( filename,"rb") as f:
        b = f.read()
        enc = chardet.detect(b)["encoding"]
        p = Path( filename )
        summary_contents = p.read_text(encoding = enc)

    soup = BeautifulSoup(summary_contents, 'html.parser')

    elm03 = soup.select_one('CALLSIGN')
    if len(elm03) >= 1 :
        callsign = elm03.contents[0].strip()
    else :
        callsign = ""
    
    parameters.append( callsign )

    elm13 = soup.select_one('FDCOEFF')
    if len(elm13) >= 1 :
        fdcoeff = elm13.contents[0].strip()
    else :
        fdcoeff = ""

    parameters.append( fdcoeff )

    print( callsign )
    print( fdcoeff ) 

    print( parameters )

    f.close()

    return parameters

