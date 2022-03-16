#coding: utf-8
import gc

class A():
    print('all_ABCD')
    def A_fc(self):
        print('A_fc')
class C(A):
    print('C_class')        
class B(C):
    print('B_class')
class D(B , A):
    pass

print(A.__mro__,'\n',B.__mro__,'\n',C.__mro__,'\n',D.__mro__)

gc.collect()