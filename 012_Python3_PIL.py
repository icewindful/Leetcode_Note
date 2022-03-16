#coding: utf-8

from PIL import Image
from PIL import ImageFilter
from pathlib import Path
import os
import gc

imagefolder = "./PIL_image"
jpg01name = "test.jpg"
png01name = "test.png"
pdf01name = "test.pdf"
tiffname = "test.tiff"
resizename = "test_resized.jpg"
zipname = "test_c.jpg"
imgRname = "test_R180.jpg"
imgLname = "test_L180.jpg"
thumbnailname = "test_thumbnail.jpg"
rfname = "test_rf.jpg"
#openfile = imagefolder + "/" +jpg01name

print(os.getcwd())
#os.chdir("./PIL_image")
os.chdir(imagefolder)
print(os.getcwd())

if os.path.isfile(png01name):
    os.remove(png01name)
else :
    im = Image.open(jpg01name)
    im.save("test.png","png")

if os.path.isfile(pdf01name):
    os.remove(pdf01name)
else :
    im = Image.open(jpg01name)
    im.save("test.pdf","pdf")

"""
#if want test file is exist other methods
try :
    os.remove(tiffname)
except:
    print("can't find {file}".format(file = tiffname))
"""

if os.path.isfile(tiffname):
    os.remove(tiffname)
else :
    im = Image.open(jpg01name)
    im.save(tiffname)


#resize
if os.path.isfile(resizename):
    os.remove(resizename)
else :
    im = Image.open("test.jpg")
    print (im.size)
    width = 400
    ratio = float(width)/im.size[0]
    height = int(im.size[1]*ratio)
    nim = im.resize( (width, height), Image.BILINEAR )
    print (nim.size)
    nim.save("test_resized.jpg")

if os.path.isfile(zipname):
    os.remove(zipname)
else :
    img = Image.open(jpg01name)
    img.save("test_c.jpg",quality=65, subsampling=0)

"""
Image.FLIP_LEFT_RIGHT (左右翻轉)
Image.FLIP_TOP_DOWN (上下翻轉)
Image.ROTATE_90 (旋轉90度)
Image.ROTATE_180 (旋轉180度)
Image.ROTATE_270 (旋轉270度)
"""

if os.path.isfile(imgRname):
    os.remove(imgRname)
else :
    img = Image.open(jpg01name)
    imgR = img.transpose(Image.ROTATE_180)
    imgR.save(imgRname)

if os.path.isfile(imgLname):
    os.remove(imgLname)
else :
    img = Image.open(jpg01name)
    imgL = img.transpose(Image.FLIP_LEFT_RIGHT)
    imgL.save(imgLname)


if os.path.isfile(imgLname):
    os.remove(imgLname)
else :
    img = Image.open(jpg01name)
    imgL = img.transpose(Image.FLIP_LEFT_RIGHT)
    imgL.save(imgLname)

if os.path.isfile(thumbnailname):
    os.remove(thumbnailname)
else :
    img = Image.open(jpg01name)
    img.thumbnail( (400,100) ) #指定長與寬並進行縮圖製作
    img.save(thumbnailname)

if Path(rfname).is_file():
    os.remove(rfname)
else :
    img = Image.open(jpg01name)
    img_f = img.filter(ImageFilter.FIND_EDGES)
    img_f.save(rfname)

gc.collect()