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
calendarFlag = False
inputFlag01 = False
inputFlag02 = True

#funtion 
def fileWriteTime(filename):
    #print("funtion get dirfolder name " + os.getcwd())
    file_operator = open(filename,"a+")
    file_operator.write("fileWriteTime Funtion : " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())) +"\n")
    file_operator.close()

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

"""
b = binary file , r = read , w = write , a = add
r	| 以只讀方式打開文件。 文件的指針將會放在文件的開頭。 這是默認模式。
rb	| 以二進制格式打開一個文件用於只讀。 文件指針將會放在文件的開頭。 這是默認模式。
r+	| 打開一個文件用於讀寫。 文件指針將會放在文件的開頭。
rb+	| 以二進制格式打開一個文件用於讀寫。 文件指針將會放在文件的開頭。
w	| 打開一個文件只用於寫入。 如果該文件已存在則將其覆蓋。 如果該文件不存在，創建新文件。
wb	| 以二進制格式打開一個文件只用於寫入。 如果該文件已存在則將其覆蓋。 如果該文件不存在，創建新文件。
w+	| 打開一個文件用於讀寫。 如果該文件已存在則將其覆蓋。 如果該文件不存在，創建新文件。
wb+	| 以二進制格式打開一個文件用於讀寫。 如果該文件已存在則將其覆蓋。 如果該文件不存在，創建新文件。
a	| 打開一個文件用於追加。 如果該文件已存在，文件指針將會放在文件的結尾。 也就是說，新的內容將會被寫入到已有內容之後。 如果該文件不存在，創建新文件進行寫入。
ab	| 以二進制格式打開一個文件用於追加。 如果該文件已存在，文件指針將會放在文件的結尾。 也就是說，新的內容將會被寫入到已有內容之後。 如果該文件不存在，創建新文件進行寫入。
a+	| 打開一個文件用於讀寫。 如果該文件已存在，文件指針將會放在文件的結尾。 文件打開時會是追加模式。 如果該文件不存在，創建新文件用於讀寫。
"""

if inputFlag01:
    inputstr = input("enter :")
    print("input string : {str}".format(str = inputstr))

if inputFlag02:
    filename01 = "input_write.txt"
    filename02 = "add_remove.txt"
    
    fd01 = open(filename01,"w+")
    fd02 = open(filename02,"w+")
    fd02.close()
    inputstr = ""
    while inputstr != "exit" :
        inputstr = input("write file word :")
        fd01.write(inputstr+"\n")
        fd01.flush() ### if right now write file , use it ###

    fd01.close()

    os.remove(filename02) ### remove file ###


"""
(1) os.access(path, mode)                       檢驗權限模式
(2) os.chdir(path)                              改變當前工作目錄
(3) os.chflags(path, flags)                     設置路徑的標記為數字標記。
(4) os.chmod(path, mode)                        更改權限
(5) os.chown(path, uid, gid)                    更改文件所有者
(6) os.chroot(path)                             改變當前進程的根目錄
(7) os.close(fd)                                關閉文件描述符fd
(8) os.closerange(fd_low, fd_high)              關閉所有文件描述符，從fd_low (包含) 到fd_high (不包含), 錯誤會忽略
(9) os.dup(fd)                                  複製文件描述符fd
(10)os.dup2(fd, fd2)                            將一個文件描述符fd 複製到另一個fd2
(11)os.fchdir(fd)                               通過文件描述符改變當前工作目錄
(12)os.fchmod(fd, mode)                         改變一個文件的訪問權限，該文件由參數fd指定，參數mode是Unix下的文件訪問權限。
(13)os.fchown(fd, uid, gid)                     修改一個文件的所有權，這個函數修改一個文件的用戶ID和用戶組ID，該文件由文件描述符fd指定。
(14)os.fdatasync(fd)                            強制將文件寫入磁盤，該文件由文件描述符fd指定，但是不強制更新文件的狀態信息。
(15)os.fdopen(fd[, mode[, bufsize]])            通過文件描述符fd 創建一個文件對象，並返回這個文件對象
(16)os.fpathconf(fd, name)                      返回一個打開的文件的系統配置信息。 name為檢索的系統配置的值，它也許是一個定義系統值的字符串，這些名字在很多標準中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
(17)os.fstat(fd)                                返回文件描述符fd的狀態，像stat()。
(18)os.fstatvfs(fd)                             返回包含文件描述符fd的文件的文件系統的信息，像statvfs()
(19)os.fsync(fd)                                強制將文件描述符為fd的文件寫入硬盤。
(20)os.ftruncate(fd, length)                    裁剪文件描述符fd對應的文件, 所以它最大不能超過文件大小。
(21)os.getcwd()                                 返回當前工作目錄
(22)os.getcwdu()                                返回一個當前工作目錄的Unicode對象
(23)os.isatty(fd)                               如果文件描述符fd是打開的，同時與tty(-like)設備相連，則返回true, 否則False。
(24)os.lchflags(path, flags)                    設置路徑的標記為數字標記，類似chflags()，但是沒有軟鏈接
(25)os.lchmod(path, mode)                       修改連接文件權限
(26)os.lchown(path, uid, gid)                   更改文件所有者，類似chown，但是不追踪鏈接。
(27)os.link(src, dst)                           創建硬鏈接，名為參數dst，指向參數src
(28)os.listdir(path)                            返回path指定的文件夾包含的文件或文件夾的名字的列表。
(29)os.lseek(fd, pos, how)                      設置文件描述符fd當前位置為pos, how方式修改: SEEK_SET 或者0 設置從文件開始的計算的pos; SEEK_CUR或者1 則從當前位置計算; os.SEEK_END或者2則從文件尾部開始. 在unix，Windows中有效
(30)os.lstat(path)                              像stat(),但是沒有軟鏈接
(31)os.major(device)                            從原始的設備號中提取設備major號碼(使用stat中的st_dev或者st_rdev field)。
(32)os.makedev(major, minor)                    以major和minor設備號組成一個原始設備號
(33)os.makedirs(path[, mode])                   遞歸文件夾創建函數。 像mkdir(), 但創建的所有intermediate-level文件夾需要包含子文件夾。
(34)os.minor(device)                            從原始的設備號中提取設備minor號碼(使用stat中的st_dev或者st_rdev field )。
(35)os.mkdir(path[, mode])                      以數字mode的mode創建一個名為path的文件夾.默認的mode 是0777 (八進制)。
(36)os.mkfifo(path[, mode])                     創建命名管道，mode 為數字，默認為0666 (八進制)
(37)os.mknod(filename[, mode=0600, device])     創建一個名為filename文件系統節點（文件，設備特別文件或者命名pipe）。
(38)os.open(file, flags[, mode])                打開一個文件，並且設置需要的打開選項，mode參數是可選的
(39)os.openpty()                                打開一個新的偽終端對。 返回pty 和tty的文件描述符。
(40)os.pathconf(path, name)                     返回相關文件的系統配置信息。
(41)os.pipe()                                   創建一個管道. 返回一對文件描述符(r, w) 分別為讀和寫
(42)os.popen(command[, mode[, bufsize]])        從一個command 打開一個管道
(43)os.read(fd, n)                              從文件描述符fd 中讀取最多n 個字節，返回包含讀取字節的字符串，文件描述符fd對應文件已達到結尾, 返回一個空字符串。
(44)os.readlink(path)                           返回軟鏈接所指向的文件
(45)os.remove(path)                             刪除路徑為path的文件。 如果path 是一個文件夾，將拋出OSError; 查看下面的rmdir()刪除一個directory。
(46)os.removedirs(path)                         遞歸刪除目錄。
(47)os.rename(src, dst)                         重命名文件或目錄，從src 到dst
(48)os.renames(old, new)                        遞歸地對目錄進行更名，也可以對文件進行更名。
(49)os.rmdir(path)                              刪除path指定的空目錄，如果目錄非空，則拋出一個OSError異常。
(50)os.stat(path)                               獲取path指定的路徑的信息，功能等同於C API中的stat()系統調用。
(51)os.stat_float_times([newvalue])             決定stat_result是否以float對象顯示時間戳
(52)os.statvfs(path)                            獲取指定路徑的文件系統統計信息
(53)os.symlink(src, dst)                        創建一個軟鏈接
(54)os.tcgetpgrp(fd)                            返回與終端fd（一個由os.open()返回的打開的文件描述符）關聯的進程組
(55)os.tcsetpgrp(fd, pg)                        設置與終端fd（一個由os.open()返回的打開的文件描述符）關聯的進程組為pg。
(56)os.tempnam([dir[, prefix]])                 返回唯一的路徑名用於創建臨時文件。
(57)os.tmpfile()                                返回一個打開的模式為(w+b)的文件對象.這文件對像沒有文件夾入口，沒有文件描述符，將會自動刪除。
(58)os.tmpnam()                                 為創建一個臨時文件返回一個唯一的路徑
(59)os.ttyname(fd)                              返回一個字符串，它表示與文件描述符fd 關聯的終端設備。 如果fd 沒有與終端設備關聯，則引發一個異常。
(60)os.unlink(path)                             刪除文件路徑
(61)os.utime(path, times)                       返回指定的path文件的訪問和修改的時間。
(62)os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])   輸出在文件夾中的文件名通過在樹中游走，向上或者向下。
(63)os.write(fd, str)                           寫入字符串到文件描述符fd中. 返回實際寫入的字符串長度    
"""

gc.collect()