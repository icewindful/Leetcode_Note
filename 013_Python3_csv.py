#coding: utf-8

import os
import csv
import sys
import gc

folder = "Filefolder"
csvname01 = "store_data.csv"
csvname02 = "store_data02.csv"

print("Now folder : "+os.getcwd())
os.chdir(folder)
print("Now folder : "+os.getcwd())

if os.path.isfile(csvname01):
    os.remove(csvname01)
else :
    file = open(csvname01 ,mode='w' ,newline='')
    
    filectl = csv.writer(file) # , replace ';'
    #filectl = csv.writer(file,delimiter=';') # , replace ';'
    filectl.writerow(['apple','banana','cherry','dragonfruit'])
    file.flush()
    file.close()

    file = open(csvname01 ,mode='r' ,newline='')
    rows = csv.reader(file)
    
    try:
        for row in rows:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(csvname01, rows.line_num, e))

    #for row in rows:
    #    print(row)

if os.path.isfile(csvname02):
    os.remove(csvname02)
else :
    with open(csvname02 ,mode ="w" , newline='') as mulfile:
        
        filectl = csv.writer(mulfile)

        # 建立 CSV 檔寫入器
        writer = csv.writer(mulfile)

        # 1.直接寫出-標題
        writer.writerow(['姓名','年齡','電話','地址'])

        # 1.直接寫出-資料
        writer.writerow(['葉大雄',18, '0911-123-123', '台北市火車站大廳'])
        writer.writerow(['林靜香',26, '0911-456-456', '台北市中山北路二段'])

        # 2.寫出多維陣列 【writerow"s"】
        Table = [['姓名','年齡','電話','地址'],['葉大雄',18, '0911-123-123', '台北市火車站大廳'],['林靜香',26, '0911-456-456', '台北市中山北路二段']]
        writer.writerows(Table)
        
gc.collect()