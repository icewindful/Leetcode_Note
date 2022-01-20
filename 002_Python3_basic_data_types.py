#basic data types
#coding: utf-8


# all option Flag Ture(1) is on , False(0) is off
# if want to print two or three the item, please use  【 , 】 like print("abc", number , 123)
from typing import Sequence
import gc #import garbagecollection.

timeFlag = False
strFlag = False
numFlag = False
setFlag = False
dictionaryFlag = False
typeConversionFlag = False
operatorsFlag = True

if timeFlag :
    import time


if timeFlag :
    import timeit

"""
Python variables need not be declared.
"""
if strFlag :
    str = "Runoob"
    str1 = "ABC"

    print(str[5]) # [0] start , last word 
    print(str[-6]) # last word [-1]start
    print(str[2:6]) # 3~6 word
    print(str) # all word
    print(str[0:]) # all word but last word be assign end flag
    print(str[-1:6]) # all word 
    print(str1 * 4) # ABCABCABCABC word
    #print("Hello, World!")

    #PS bool on Python3 false = 0 , true = 1; and bool can add number.
    #python word array , can't change 1 word like str[1] = 'Z', but can  all Re-describe str1 = "ABC" after str1 = "CBA"
    str1 = "CBA"
    print(str1)

    #release memory use " del "

    del str , str1
    gc.collect()

"""
Numerical operations
"""
if numFlag :
    number_Addition = 1 + 1 
    number_Subtraction = 3 - 1
    number_Multipliction = 2 * 3
    number_Division_float = 5 / 2 
    number_Division_int = 5 // 2
    number_Remainder = 18 % 5 
    number_Square = 2 ** 5

    #number to str ●1. str(number) , ●2.  f-formatting , f'{object}' like  f'{number_Addition}

    print("number_Addition 1 + 1 = " + str(number_Addition) + "\nnumber_Subtraction 3 -1 = " + str(number_Subtraction) + \
        "\nnumber_Multipliction 2 * 3 = " + str(number_Multipliction) + \
        "\nnumber_Division_float_int 5 // 2 , 5 / 2 = ", number_Division_float, number_Division_int, \
        "\nnumber_Remainder 18 % 5 = " + f'{number_Remainder}' + \
        "\nnumber_Square 2 ** 5 = " + str(number_Square))

    #return multi number , allary , linklist , value catch (###warning### catch and return be match)
    def multi_return_func01():
        allarray = [number_Addition,number_Subtraction,number_Multipliction]
        return allarray

    print(multi_return_func01())

    def multi_return_func01():
        NA01 = number_Addition + number_Addition
        NS01 = number_Subtraction + number_Subtraction + number_Subtraction
        return NA01 , NS01

    CatchN01 , CatchN02 = multi_return_func01()

    print(CatchN01,CatchN02)

    del number_Addition,number_Subtraction,number_Multipliction,number_Division_float,number_Division_int,number_Remainder,number_Square
    gc.collect()

    #list [a,b,c] , tuple (a,b,c,"d") ##cann't change any array[n]##,

    tuple_a = ('a','b','c',"d")

    a = [1,2,3,4,5,6,7]
    a[0] = 9
    a[2:5] = [11,22,33]
    print(a)
    #delele sequence 2~5 item
    a[2:5] = [] 
    print(a)
    a.append(999)
    print(a)
    print(len(a))
    a.clear()
    print(a)

    print("tuple : " , tuple_a)

    #start = 0
    #end = 0

    empty_t_array = ()

    del a,empty_t_array , tuple_a
    gc.collect()

if timeFlag :
    def t_array01():
        #print(empty_t_array)
        t_array01 = ("ABC",1,["X","Y","Z",1,2,3])
        #t_array01 = ("ABC",1,["X"])
        #start = time.time()
        print(t_array01)
        #start = time.time()
        #print(t_array01)
        #end = time.time()
        #print("01 : %f秒" %(start - end))
        #print(t_array01[2].append("ICE"))

if timeFlag :
    def t_array02():
        t_array02 = ("ABC",1,"X","Y","Z",1,2,3)
        #t_array02 = ("ABC",1,"X")
        #start = 0
        #end = 0
        print(t_array02)
        #start = time.time()
        #print(t_array02)
        #end = time.time()
        #print("02 : %f秒" %(start - end))

if timeFlag :
    #test function timeit
    print("it want test second unmask it")
    #t = timeit.timeit(t_array01,number=10000)
    #print("01 : %f sec" % t)
    #t = timeit.timeit(t_array02,number=10000)
    #print("02 : %f sec" % t)
    
if timeFlag :
    del t_array01,t_array02
    gc.collect()


if setFlag :
    #set methods | & - ^ , |= &= -= ^=
    studentList = ["ABC","CBA",123,321]
    student01 = {'ABC','CBA','XYZ','ZYX'}
    student02 = set("ABC")
    student03 = set(studentList)
    student04 = {"CBA"}
    student05 = set()
    print("student01 : " + str(student01))
    print("student02 : " + str(student02))
    print("student03 : " + str(student03))
    print("student04 : " + str(student04))  
    print("student05 : " + str(student05))  
    print("( | ) 01 | 03 union() : " + str(student01 | student03))
    print("( & ) 01 & 03 intersection() : " + str(student01 & student03))
    print("( - ) 01 - 03 difference() : " + str(student01 - student03))    
    print("( ^ ) 01 ^ 03 symmetric_difference() : " + str(student01 ^ student03))
    student05 = student04
    student05 |= student03
    print("( |= ) 04 |= 03 update() : " + str(student05))
    student05 = student04
    student05 &= student03
    print("( &= ) 04 &= 03 intersection_update() : " + str(student05))
    student05 = student04
    student05 -= student03
    print("( -= ) 04 -= 03 difference_update() : " + str(student05))
    student05 = student01
    student05 -= student03
    print("( -= ) 01 -= 03 difference_update() : " + str(student05))
    student05 = student04
    student05 ^= student03
    print("( ^= ) 04 ^= 03 symmetric_difference_update() : " + str(student05))

    del studentList , student01 , student03 , student04 , student05
    gc.collect()


if dictionaryFlag :
    ## make dictionary {} , key and value , one set , this fix font 
    dict = {}
    dict['one'] = "1 - this dictionary01"
    dict[5566] = "2 - this dictionary02"

    tinydict = {'name': 'Py3 dictionary01 ', 'site': 'icewindful', 'code': 1}

    print(dict['one'])       # key print value
    print(dict[5566])        # key print value
    print(dict)              # 
    print(tinydict)          # all Dictionary all Key and Value
    print(tinydict.keys())   # all Dictionary Keys
    print(tinydict.values()) # all Dictionary Value

    del dict , tinydict
    gc.collect()

if typeConversionFlag :
    x = 3.14
    y = '[a-z]+'
    z = 97
    chr_c = "a"
    array_a = 1,2,3,4,5,6,7,8,"abc"
    print("x :" ,x)
    print("y :" ,y)
    conversionX = int(3) # to int
    print("int conversionX : " ,conversionX)
    conversionX = float(1/2) # to float
    print("float conversionX : " ,conversionX)
    print("str(x) :" ,str(x)) # to string
    print("repr(y) :" ,repr(y)) # to string expression
    print("tuple(array_a) :" ,tuple(array_a)) # Sequence to tuple
    print("list(array_a) :" ,list(array_a)) # Sequence to list
    print("set(array_a) :" ,set(array_a)) # Sequence to set
    print("frozenset(array_a) :",frozenset (array_a)) # Sequence to frozenset 
    print("chr(z) : " ,chr(z)) # Convert a character to string 
    #print("unichr(x)",unichr(x)) , python is not use it
    print("ord(chr) :" ,ord(chr_c)) # string to Convert a character 
    print("hex(z) :" ,hex(z)) # An integer is converted to a hexadecimal string
    print("oct(z) :" ,oct(z)) # An integer is converted to an octal string
    del x , y , z , chr_c , array_a , conversionX
    gc.collect()

if operatorsFlag : 
    # logic operators 【and】 , 【or】 , 【not】
    a = 0x03 # 0000 0011
    b = 0x05 # 0000 0101

    #print("a :" ,a ,"\nbinary :" ,bin(a).replace('0b','') ,"\nb :", b ,"\nbinary :" ,bin(b).replace('0b',''))
    #print("a :" ,a ,"\nbinary :" ,"{0:b}".format(a) ,"\nb :", b ,"\nbinary :" ,"{0:b}".format(b))
    #if want to hex , ord , bin , have the symbol. set 【 # 】

    #★★★★★#
    #print("a :" ,a ,"\nbinary :" ,f"{a:#b}" ,"\nb :", b ,"\nbinary :" ,f"{b:#b}") 
    #print("a :" ,a ,"\nbinary :" ,f"{a:08b}" ,"\nb :", b ,"\nbinary :" ,f"{b:08b}") 
    #print("a : %s \nb : %s" % (f"{a:b}" ,f"{b:b}")) 
    print("a : {abc} \nb : {xyz}".format(abc=f"{a:08b}" ,xyz=f"{b:08b}"))
    #★★★★★#

    if (a and b):
        print("a and b : 【a == b】")
    else:
        print("a not b : 【a \= b】")

    if (a or b):
        print("a or b :【a | b】")
    else: 
        print("a not or b : 【a !| b】")

    if not(a and b):
        print("a not b : 【a != b】")
    else:
        print("a is b : 【a == b】")

    #meber operators 【in】 , 【not in】
    a = 10 
    b = 20
    serachList = [1,2,3,4,5,10]

    print("a : {a} \nb : {b} \nserachList : {serachList} ".format(a=a,b=b,serachList=serachList))

    if (a in serachList) :
        print("a in list")
    else :
        print("a not in list")

    if (b not in serachList):
        print("b not in list")
    else :
        print("b in list")

    #check memory address operators , 【is】,【not is】, if want to check function is id(item) how to memory address

    a = 1
    b = 1
    c = a 
    alist = [1,2,3,4,5,6]
    blist = [1,2,3,4,5,6]
    clist = alist

    if (a == b) :
        print("a == b is true")
    else :
        print("a == b is false")

    
    if (a == c) :
        print("a == c is true")
    else :
        print("a == c is false")

    if (a is b) :
        print("a == b is true")
    else :
        print("a == b is false")

    if (a is c) :
        print("a == c is true")
    else :
        print("a == c is false")

    print("a :memroy address : {a_addr} \nb :memory address : {b_addr} \nc :memory address : {c_addr}".format(a_addr=id(a) ,b_addr=id(b) ,c_addr=id(c)))

    if (alist == clist) :
        print("a == c is true")
    else :
        print("a == c is false")

    if (alist is blist) :
        print("a == b is true")
    else :
        print("a == b is false")

    if (alist is clist) :
        print("a == c is true")
    else :
        print("a == c is false")

    print("alist :memroy address : {a_addr} \nblist :memory address : {b_addr} \nclist :memory address : {c_addr}".format(a_addr=id(alist) ,b_addr=id(blist) ,c_addr=id(clist)))
    
    del a , b , c , serachList , alist ,blist ,clist
    gc.collect()


