#coding: utf-8

import gc

stringFlag = True

if stringFlag :
    a = "icewindful"
    b = "is genius"
    width = 40
    mark = "★"
    strAlnumber = "ThisNumber01"
    strAplha = "greatBrian"
    strspace = "    mastermodifter    "
    laststr ="neverGive"
    
    num01 = u"4"  #unicode
    num02 = "4" # 全角
    num03 = "四" # 中文
    num04 = "IV" # 羅馬數字
    num05 = b"4" # byte

    print("a = {str01}\nb = {str02}".format(str01=a ,str02=b))
    print("capitalize(a) : {method}".format(method = str.capitalize(a))) # the first upper
    print("center({val01},{val02}) : {method}".format(val01 = width , val02 = mark , method = a.center(width,mark)))
    print("ljust({val01},{val02}) : {method}".format(val01 = width , val02 = mark , method = a.ljust(width,mark)))
    print("rjust({val01},{val02}) : {method}".format(val01 = width , val02 = mark , method = a.rjust(width,mark)))

    print("{str01} isdigit(): {method}".format(str01 = num01, method = num01.isdigit()))
    print("{str01} isdecimal(): {method}".format(str01 = num01, method = num01.isdecimal()))
    print("{str01} isnumeric(): {method}".format(str01 = num01, method = num01.isnumeric()))

    print("{str01} isdigit(): {method}".format(str01 = num02, method = num02.isdigit()))
    print("{str01} isdecimal(): {method}".format(str01 = num02, method = num02.isdecimal()))
    print("{str01} isnumeric(): {method}".format(str01 = num02, method = num02.isnumeric()))

    print("{str01} isdigit(): {method}".format(str01 = num03, method = num03.isdigit()))
    print("{str01} isdecimal(): {method}".format(str01 = num03, method = num03.isdecimal()))
    print("{str01} isnumeric(): {method}".format(str01 = num03, method = num03.isnumeric()))
    
    print("{str01} isdigit(): {method}".format(str01 = num04, method = num04.isdigit()))
    print("{str01} isdecimal(): {method}".format(str01 = num04, method = num04.isdecimal()))
    print("{str01} isnumeric(): {method}".format(str01 = num04, method = num04.isnumeric()))

    print("{str01} isdigit(): {method}".format(str01 = num05, method = num05.isdigit()))
    #### false use ####
    #print("{str01} isdecimal(): {method}".format(str01 = num05, method = num05.isdecimal()))
    #print("{str01} isnumeric(): {method}".format(str01 = num05, method = num05.isnumeric()))
    #### false use ####

    print("{str01} isalnum(): {method}".format(str01 = strAlnumber, method = strAlnumber.isalnum()))
    print("{str01} isalnum(): {method}".format(str01 = strAplha, method = strAplha.isalnum()))

    print("{str01} isalpha(): {method}".format(str01 = strAlnumber, method = strAlnumber.isalpha()))
    print("{str01} isalpha(): {method}".format(str01 = strAplha, method = strAplha.isalpha()))

    print("{str01} : strip()  + {str02}:\n{method}".format(str01 = strspace, str02 = laststr, method = strspace.strip()  + laststr))
    print("{str01} : lstrip() + {str02}:\n{method}".format(str01 = strspace, str02 = laststr, method = strspace.lstrip() + laststr))
    print("{str01} : rstrip() + {str02}:\n{method}".format(str01 = strspace, str02 = laststr, method = strspace.rstrip() + laststr))

    print("{str01} split(' '): {method}".format(str01 = b, method = b.split(' ')))
    
    tmplist = []
    tmplist = b.split(' ')

    print(len(tmplist))
    print(tmplist[1])

    del a ,b ,width ,mark ,strAlnumber ,strAplha ,num01 ,num02 ,num03 ,num04 ,num05 ,tmplist
    gc.collect()