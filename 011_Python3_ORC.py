#coding: utf-8

import pytesseract
import gc
from PIL import Image

engflag01 = False
chiflag02 = False
chiengflag03 = True

def main():
    if engflag01:
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        img = Image.open(r".\imagefolder\image1.JPG")
        #img.show()
        print(pytesseract.image_to_string(img, lang="eng"))

    if chiflag02:
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        img = Image.open(r".\imagefolder\image2.JPG")
        #img.show()
        print(pytesseract.image_to_string(img, lang="chi_tra"))

    if chiengflag03:
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        img = Image.open(r".\imagefolder\image3.JPG")
        #img.show()
        print(pytesseract.image_to_string(img, lang="chi_tra+eng"))

if __name__ == "__main__":
    main()

gc.collect()