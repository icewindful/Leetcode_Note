#coding: utf-8

functionFlag = False
classFlag = False
multiclassFlas = False
VariablelengthFlag = True


import types

import gc

#basic function
def test(int):
    return int*int*int

def if_elif_fuc(a , b):
    if a > b:
        print("{val01}>{val02}".format(val01=a,val02=b))
        return a
    elif a < b:
        print("{val01}<{val02}".format(val01=a,val02=b))
        return b
    else :
        print("can't use function")
        return a,b

def while_fuc01(n):
    sum = 0
    counter = 1
    while counter <=n:
        sum += counter
        counter += 1
        
    print("funtion : sum : 1 to {val01} : {answer}".format(val01=n,answer=sum))
    return sum

def while_fuc02(n):

    count = 0
    while count < n :
        print("{number}<{setval}".format(number = count , setval = n))
        count += 1
    else :
        print("{number}>{setval}".format(number = count , setval = n))

def forfunc01():

    breakword = "but"

    sites = ["icewindful","is","genius","but","all the world","be remake"]
    for site in sites:
        if site == breakword:
            print("\n【break and leave forfunction!】")
            break
        else:
            print(site,end=' ')
    print("break word = \"{word}\" : forcunc01 end".format(word = breakword))

def forfunc02():

    for letter in 'icewindful': 
        if letter == 'f':
            pass #note 
            print ('now pass')
        print ('word = \'{word}\''.format(word = letter))

    print ("Good bye!")

def forfunc03():

    for letter in 'ice,wind,ful': 
        if letter == ',':
            print ('continue return for loop')
            continue #note 
        print ('word = \'{word}\''.format(word = letter))

    print ("Good bye!")

@staticmethod ## define static function
def passfun():
    print("passfun")
    pass #it not any run , but can premake function name

#staticmethod(passfun)

class addclass01:

    def __init__(self, func):
        self.numberOfCalls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.numberOfCalls += 1
        return self.func(*args, **kwargs)

    def class01method(self):
        print("add class method01")

class addclass02:

    def __init__(self, func):
        self.numberOfCalls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.numberOfCalls += 1
        return self.func(*args, **kwargs)

    def class02method(self):
        print("add class method02")

@addclass02
def adds01(x,y,z):
    return x * y * z

#★★★★★# multi sub class have to method class01method() class02method() and overridder class02method()
class addclass03(addclass02,addclass01):

    def class02method(self):
        print("use super call original method")
        super().class02method()
        print("override method02 to method03")

    def class03method(self):
        print("add class method03")

@addclass03
def adds02(x,y,z):
    return x * y * z


class multiclass:

    def __init__(self, seat, color):
        self.seat = seat
        self.color = color

    @staticmethod
    def onemethod():
        print("one")

    @staticmethod
    def twomethod():
        print("two")
    
    @staticmethod
    def threemethod():
        print("two")

    @classmethod
    def van(cls):
        return cls(6,"black")

    @classmethod
    def sports_car(cls):
        return cls(4,"yellow")


if functionFlag:
    n = 3
    val01 = 10
    val02 = 100
    answer = 0
    print(test(n))

    answer = if_elif_fuc(val01,val02)
    print("a<b:a?b : {method}".format(method=if_elif_fuc(val01,val02)))
    print("sum 1 to {n} : {method}".format(n=val02 ,method=while_fuc01(val02)))
    while_fuc02(val01)
    forfunc01()
    forfunc02()

    classtest = multiclass
    multiclass.onemethod()
    multiclass.twomethod()
    van = multiclass.van()
    sports_car = multiclass.sports_car()
    print(van.seat)
    print(sports_car.seat)
    print(van.color)
    print(sports_car.color)

    print(adds01(10,20,2))
    adds01.class02method() #multi add method on class
    print("adds funtion call counts : {counts}".format(counts = adds02.numberOfCalls))
    print(adds02(20,20,2))
    print("adds funtion call counts : {counts}".format(counts = adds02.numberOfCalls))
    adds02.class02method() #multi add method on class
    adds02.class01method() #multi add method on class
    adds02.class03method()
    print(adds02(5,20,2))
    print("adds funtion call counts : {counts}".format(counts = adds02.numberOfCalls))

    forfunc03()


    del n , val01 ,val02 ,answer
    gc.collect()


if classFlag:

    class ClassDecorator:
        def __init__(self, func):
            self.numberOfCalls = 0
            self.func = func

        def __call__(self, *args, **kwargs):
            self.numberOfCalls += 1
            return self.func(*args, **kwargs)

        def __get__(self, instance, cls):
            if instance is None:
                return self
            else:
                return types.MethodType(self, instance)


    #Class Implementation method 
    @ClassDecorator 
    def add(x, y):
        return x + y

    class Decorated:
        @ClassDecorator
        def bar(self, x):
            print(self, x)


    print(add(5, 10))
    print(add(1, 999))
    print(add.numberOfCalls) #call function counts
    s = Decorated()
    s.bar(1)
    s.bar(2)
    s.bar(3)
    print(Decorated.bar.numberOfCalls) #call function counts

    del s
    gc.collect()


if multiclassFlas :
    # base classes

    class A:
        def __init__(self, a1, a2, **kwargs):
            super().__init__(**kwargs)
            self.a1 = a1
            self.a2 = a2

        def funa(self):
            print("I'm funa")

    class B:
        def __init__(self, b1, **kwargs):
            super().__init__(**kwargs)
            self.b1 = b1

        def funb(self):
            print("I'm funb")
            
    class C:
        def __init__(self, c1, c2, c3, **kwargs):
            super().__init__(**kwargs)
            self.c1 = c1
            self.c2 = c2
            self.c3 = c3

        def func(self):
            print("I'm func")

    # derived classes

    class X(B, A, C):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            
    class Y(A, B):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)


    x = X(a1=1, a2=2, b1=3, c1=4, c2=5, c3=6)
    y = Y(a1=1, a2=2, b1=3)
    print(x.a1, x.a2, x.b1, x.c1, x.c2, x.c3)
    x.funa()
    y.funb()
    print(dir(x))
    print(dir(y))

    del x,y
    gc.collect()

if VariablelengthFlag:
    def printinfo(*args ,**kwargs):
        "*vartuple : * it is VariableLength"
        print("output :")
        for var in args:
            print (var)
        return

    printinfo(10)
    printinfo(70,60,50)


### key="string" value= any 

dict01 = {"icewindful":1 ,"is great":2,"master":3}
dict02 = {"bluesky":999,"earthsea":1000}
dict03 = {"name":"wang han","age":33,"gender":"boy","job":"Manager"}


def printdictinfo(*args, **kwargs):
    print("args output :")
    for each in args:
        print(each)
    print("dict output :")
    for each in kwargs:
        print(each)
    
printdictinfo(**dict03,**dict02)

# A=[22,33,44]
# B={"name":"wang han","age":33,"gender":"boy","job":"Manager"}
# def test(a,*args,**kwargs):
# 	print("a=%s" %a)
# 	print("args:")
# 	for each in args:
# 		print(each)
# 	print("kwargs:")
# 	for each in kwargs:
# 		print(each)		

# test(1,*A,**B) 

gc.collect()