#coding: utf-8
import sys

#this module in workspace G:\Leetcode_py\package
#get now dir G:\Leetcode_py
#py -3 .\000_Python3_init_mymodule.py
print("Base :")
print(sys.path)

import MyModule02 as MM02

sys.path.append('./package')
#print("Path add package folder")
#print(sys.path)
"""
sys.path.append('G:/Leetcode_py/package')
"""

#import myModule01
#print(myModule01.totalsum(10,30))

try:
    import myModule01 as myM
except ImportError:
    print("myModule01 Module not found!!")


print(myM.totalsum(10,30))
print(MM02.AxB(2,4))

a1 = MM02.Math2(3,3)

a1.addanswer()

print("add a , b : {answer}".format(answer = a1))

a1.divanswer()

print("divaid a , b : {answer}".format(answer = a1))

a1.__doc__()
#print(a1)

