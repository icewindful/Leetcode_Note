#coding: utf-8

import gc
from math import degrees
from random import shuffle, uniform #import garbagecollection.


mathFlag = False
randomFlag = False
trigonometricFlag = True
if mathFlag or trigonometricFlag:
    import math
    from decimal import Decimal

if randomFlag:
    import random

# Mathematical Functions

if mathFlag:
    a = 3.14
    b = 5.6
    c = -10
    d = 10
    e = 100
    f = Decimal(7.5649)
    g = 7.5
    h = 8.5
    i = 1
    j = 2
    k = 8

    math_array01 = [10 ,-1 ,200 ,100 ,-999 ,50 ,499 ,999]
    math_array02 = [1000 ,-10 ,300 ,150 ,-500 , 75 ,299 ,599]

    #abs() retun absolute 
    print("abs({originalval01}) : {method}".format(originalval01 = a ,method = abs(a))) 
    print("abs({originalval01}) : {method}".format(originalval01 = c ,method = abs(c)))

    #math.cell() roundup
    print("ceil({originalval01}) : {method}".format(originalval01 = a ,method = math.ceil(a))) 
    print("ceil({originalval01}) : {method}".format(originalval01 = b ,method = math.ceil(b)))

    #math.floor() rounddown
    print("floor({originalval01}) : {method}".format(originalval01 = a ,method = math.floor(a))) 
    print("floor({originalval01}) : {method}".format(originalval01 = b ,method = math.floor(b)))

    #math.round(value,set decimal places Field) ###note### import decimal avoid python round in .5 false
    print("round({originalval01},0) : {method}".format(originalval01 = f ,method = round(f,0))) 
    print("round({originalval01},1) : {method}".format(originalval01 = f ,method = round(f,1))) 
    print("round({originalval01},2) : {method}".format(originalval01 = f ,method = round(f,2)))
    print("round({originalval01},3) : {method}".format(originalval01 = f ,method = round(f,3)))

    ### it not expected round : 7.5 get 8(ture) but 8.5 get 8 (false) 
    print("round({originalval01},0) : {method}".format(originalval01 = g ,method = round(g,0))) 
    print("round({originalval01},0) : {method}".format(originalval01 = h ,method = round(h,0))) 

    print("exp({originalval01}) : {method}".format(originalval01 = i ,method=math.exp(i))) 

    #math.fabs() can't complex to float
    print("math.fabs({originalval01}) : {method}".format(originalval01 = a ,method = math.fabs(a))) 
    print("math.fabs({originalval01}) : {method}".format(originalval01 = c ,method = math.fabs(c)))

    #math log , log10 , log2 , log1p 
    print("math.log({originalval01} ,{originalval02}) : {method}".format(originalval01 = k ,originalval02=j,method = math.log(k,j))) 
    print("math.log({originalval01} ,{originalval02}) : {method}".format(originalval01 = e ,originalval02=d,method = math.log(e,d)))
    print("math.log10({originalval01}) : {method}".format(originalval01 = e ,method = math.log10(e)))
    print("math.log10({originalval01}) : {method}".format(originalval01 = d ,method = math.log10(d)))

    #max(val01,val02) min(val01,val02)
    print("max({originalval01} ,{originalval02}) : {method}".format(originalval01 = a,originalval02=b,method = max(a,b)))
    print("max({originalval01} ,{originalval02}) : {method}".format(originalval01 = math_array01 ,originalval02 = math_array02,method = max(math_array01,math_array02)))
    print("min({originalval01} ,{originalval02}) : {method}".format(originalval01 = a ,originalval02=b,method = min(a,b)))
    print("min({originalval01} ,{originalval02}) : {method}".format(originalval01 = math_array01 ,originalval02 = math_array02,method = min(math_array01,math_array02)))

    print("max({originalval01}) : {method}".format(originalval01 = math_array01 ,method = max(math_array01)))
    print("min({originalval01}) : {method}".format(originalval01 = math_array01 ,method = min(math_array01)))
    print("min(max({originalval01} ,{originalval02}) : {method})"\
           .format(originalval01 = math_array01 ,originalval02=math_array02, method = min(max(math_array01,math_array02))))
    print("max(min({originalval01} ,{originalval02}) : {method})"\
           .format(originalval01 = math_array01 ,originalval02=math_array02, method = max(min(math_array01,math_array02))))

    #square sqrt(value)
    print("math.sqrt({originalval01}) : {method}".format(originalval01 = e ,method = math.sqrt(e)))

    del a ,b ,c ,d ,e ,f ,g ,h ,i ,math_array01 ,math_array02
    gc.collect()

if randomFlag:
    a = 1
    b = 10
    c = -99
    step_number = 3
    math_array01 = [-1 ,10 ,20 ,100 ,200 ,500 ,499 ,999]
    math_array02 = [1000 ,-10 ,300 ,150 ,-500 , 75 ,299 ,599]
    #★★★★★# if list(array copy not reference use array[:] copy it)
    math_array03 = math_array02[:]
    print("id({item}) : memory address :{address}".format(item = "math_array02",address = id(math_array02)))
    print("id({item}) : memory address :{address}".format(item = "math_array03",address = id(math_array03)))

    print("choice({originalval01}) : {method}".format(originalval01 = math_array01 ,method = random.choice(math_array01)))
    print("choice(range({originalval01},{originalval02})) : {method}".format(originalval01 = a, originalval02 = b,method = random.choice(range(a,b))))
    #step = step_number is two : 1-10 , it like 1 3 5 7 9 choice , step_number is three : 1-10 , it like 1 ,4 ,7
    print("choice(range({originalval01},{originalval02},{originalval03})) : {method}"\
          .format(originalval01 = a, originalval02 = b ,originalval03 = step_number ,method = random.choice(range(a,b,step_number))))
    
    #★★★★★# want to set after place 1 value use 【:.1f】 sample value :100.1 
    print("random.random()*100 : {method:.1f}".format(method=(random.random()*100)))
    print("random.shuffle({originalval01}) : return :{method} \nafter {originalval02}"\
          .format(originalval01=math_array03, method=random.shuffle(math_array02) ,originalval02=math_array02))

    print("uniform({originalval01},{originalval02}) : {method:.0f}".format(originalval01 = b ,originalval02 = c ,method = uniform(b,c)))

    del a ,b ,c ,math_array01 ,math_array02
    gc.collect()

if trigonometricFlag:
    #math trigonometric method
    """
    math.asin(x)
    math.acos(x)
    math.atan(x)
    math.sin(x)
    math.cos(x)
    math.tan(x)
    math.radians(x)
    math.degrees(x)
    math.hypot(x,y)
    """
    a = 3
    b = 4
    c = 5

    onedegrees = math.pi/180
    print("math.degrees({pi:.2f}/12) : {method}".format(pi=math.pi ,method = math.degrees(math.pi)/12))
    print("sin(90) : {method}".format(method = math.sin(math.pi/2)))
    print("cos(90) : {method}".format(method = math.cos(math.pi/2)))
    print("tan(90) : {method}".format(method = math.tan(math.pi/2)))

    print("sin(45) : {method}".format(method = math.sin(math.pi/4)))
    print("cos(45) : {method}".format(method = math.cos(math.pi/4)))
    print("tan(45) : {method}".format(method = math.tan(math.pi/4)))

    print("sin(30) : {method}".format(method = math.sin(math.pi/6)))
    print("cos(30) : {method}".format(method = math.cos(math.pi/6)))
    print("tan(30) : {method}".format(method = math.tan(math.pi/6)))

    print("a = {tri_a} , b = {tri_b} , c = {tri_c}".format(tri_a = a , tri_b = b , tri_c = c))
    print("math.hypot({tri01} ,{tri02}) : {method}".format(tri01 = a , tri02 = b , method = math.hypot(a,b)))

    del a , b ,c ,onedegrees
    gc.collect()