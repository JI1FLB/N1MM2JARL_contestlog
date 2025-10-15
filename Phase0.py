def phase0(Guest, FD_contest, Multi_Op):

#------------------------------
#
#   サマリーシートからコールサインを取得
#


    import os

    fill_in_form = open( "summarysheet.txt" ,"r", encoding='utf-8')

    Callsign =""
    Ph0 = []


#------------------------------------------------------------------------
#
#   コールサイン取得
#   サマリーシート作成
#

    fill_in = fill_in_form.readlines()

    for fill in fill_in :
        fill = fill.rstrip('\n')
        fill = fill.strip()
        fill = fill.split(":")
        if "コールサイン"==fill[0] :
            Callsign = fill[1]
            Callsign = Callsign.lstrip().rstrip()
            Ph0.append(Callsign)
            break

    fill_in_form.close()
    
    return Ph0
