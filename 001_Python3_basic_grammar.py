#coding: utf-8
#Python3 basic grammar
import gc #import garbagecollection.
#multi-line

item_one ,item_two ,item_three = 1,2,3

total = item_one + \
        item_two + \
        item_three 

#PS: if linklist , Tuple , Sets , Dictionary . usen't it.

input("\n\n input enter exit!!!")

import sys; x = 'w3big'; sys.stdout.write(x + '\n')

del item_one ,item_two ,item_three
gc.collect()
