def phase1( a:str ):
    
    import os

    filename = ""
    forming_file = ""
    Callsign = ""

#------------------------------------------------------------------------
#
#   ファイルネーム（コールサイン）の入力
#
#

    Callsign = a

    filename =  Callsign + ".adi"
    forming_file = Callsign + "_forming.adi"
    adi_file = open(filename,"r",encoding='utf-8')
    output_log = open(forming_file ,"w",encoding='utf-8')

#--------------------------------------------------------------------

    data1=""
    a = ""


#------------------------------------------------------------------------
#
# ADIFファイルが改行分割されたレコードを1レコードに編集
#
#

    lines = adi_file.readlines()

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
        
    adi_file.close()
    output_log.close()


    return
