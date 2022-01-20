#coding: utf-8

#★★★★★#

from genericpath import isdir
import sys
import gc
import os
import shutil
import time;
import calendar

inputFlag = False
fileFlag = False
timeFlag = False
calendarFlag = True

#funtion 
def fileWriteTime(filename):
    #print("funtion get dirfolder name " + os.getcwd())
    file_operator = open(filename,"a+")
    file_operator.write("fileWriteTime Funtion : " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())) +"\n")
    file_operator.close()


if inputFlag:
    inputstr = input("enter :")
    print("input string : {str}".format(str = inputstr))

if fileFlag:
    folderName = "Filefolder"
    #abspath00 = "G\\:\\Leetcode_py\\{name}".format(name = folderName)
    abspath01 = os.path.abspath('.')
    nowpath = os.getcwd()
    dirpath = nowpath + "\\" + folderName

    #print("abspath folder : {name}".format(name = abspath00))
    print("abspath02 folder : {name}".format(name = abspath01))
    print("nowpath folder : {name}".format(name = nowpath))
    print("dirpath folder : {name}".format(name = dirpath))
    print(os.listdir())

    if isdir(dirpath):
        try:
            os.rmdir(dirpath)
            print("os.rmdri remove sucess!!")
        except:
            print("os.rmdir can't remove dir:{errinfo}".format(errinfo = sys.exc_info()[0]))
            print("dir not empty!!")
            print("now use shutil.rmtree!!!!")
            shutil.rmtree(dirpath)

    else :
        os.makedirs(folderName,exist_ok=True)
        print(os.getcwd())
        os.chdir(dirpath)
        print(os.getcwd())
        os.chdir('../')
        print(os.getcwd())
        os.chdir(os.path.join(os.getcwd(), folderName))
        print(os.getcwd())

        #f = os.open("test01.txt",os.O_RDWR | os.O_CREAT)
        #string = b"icewindful will be prefact manastone!!"
        #os.close(f)

        filename01 = "test01.txt"
        filename02 = "test02.txt"
        
        file_operator = open(filename01,"a+")
        str02 = "At last, lose icewindful any memory!!"
        naxtline = "\n"

        file_operator.write(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())) + " : ")
        fileWriteTime(filename01)
        file_operator.write("icewindful will be perfact mana stone!!!"+naxtline)
        print(file_operator.tell())
        #nowindex = file_operator.tell()
        file_operator.seek(0) # back file index
        #str01 = file_operator.read()
        str01 = file_operator.readline()
        print(str01)
        file_operator.seek(file_operator.tell())


        file_operator.write(str02)
        print(file_operator.tell())
        file_operator.seek(0) # back file index
        str01 = file_operator.read()
        print(str01)
        file_operator.close()


if timeFlag :
    print(time.time())
    print(time.localtime(time.time()))
    print(time.asctime( time.localtime(time.time())))

    # 格式化成2016-03-20 11:45:39形式
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # 格式化成Sat Mar 28 22:24:24 2016形式
    print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

    # 將格式字符串轉換為純秒數
    time01 = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(time01,"%a %b %d %H:%M:%S %Y")))

    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    
    #Notes
    """        
    %y 兩位數的年份表示（00-99）
    %Y 四位數的年份表示（000-9999）
    %m 月份（01-12）
    %d 月內中的一天（0-31）
    %H 24小時制小時數（0-23）
    %I 12小時制小時數（01-12）
    %M 分鐘數（00=59）
    %S 秒（00-59）
    %a 本地簡化星期名稱
    %A 本地完整星期名稱
    %b 本地簡化的月份名稱
    %B 本地完整的月份名稱
    %c 本地相應的日期表示和時間表示
    %j 年內的一天（001-366）
    %p 本地AM或PM的等價符
    %U 一年中的星期數（00-53）星期天為星期的開始
    %w 星期（0-6），星期天為星期的開始
    %W 一年中的星期數（00-53）星期一為星期的開始
    %x 本地相應的日期表示
    %X 本地相應的時間表示
    %Z 當前時區的名稱
    %% %號本身
    """
    
if calendarFlag:
    cal = calendar.month(2016, 1)
    print ("Print 2016 january:")
    print (cal)

    cal = calendar.calendar(2022)
    print (cal)

gc.collect()