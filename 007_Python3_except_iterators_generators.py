#coding: utf-8

#★★★★★#

import sys
import gc
from typing import Generator

exceptFlag = False
iternextFlag = False
generatorFalg = False
yieldFlag = False
masteryieldFlag = True

if exceptFlag :
    try:
        mm = 9 / 0
    except:
        # sys.exc_info()[0] get except why error type message
        print("Unexpected error:", sys.exc_info()[0])

    def divide(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            print("can't Division : Zero (0)")
        except Exception as e:
            print("other error :{}".format(e))
            print("sys.exc_info()[0]: {err}".format(err = sys.exc_info()[0]))
        else:
            print("no error run end :", result)
        finally:
            print("finally : allways run it!!!")
    
    divide(2, 1)
    print("======")
    divide(2, 0)
    print("======")
    divide('x', 'y')

    # try:
    #     raise NameError("This is Name Error!")
    # except NameError:
    #     print("We got Name Error!")
    #     raise

if iternextFlag :
    list = [i for i in range(5,20)]
    
    print(list)

    nlist = iter(list)

    print("nlist for loop list:")
    for n in nlist:
        print("\nn = {item}".format(item = n) ,end=" ")

    print("\nnext() nlist while loop list:")
    list = [i for i in range(0,10)]
    nlist = iter(list)

    while True:
        try:
            print("n = {item}".format(item = next(nlist)))
        except StopIteration:
            sys.exit()


if generatorFalg:
    class Node:
        def __init__(self,value):
            self.root = value
            self.left = None
            self.right = None

        def add_leftChild(self,node):
            if type(node) != type(Node(0)):
                raise TypeError
            else:
                self.left = node
            
        def add_rightChild(self,node):
            if type(node) != type(Node(0)):
                raise TypeError
            else:
                self.right = node

        def __repr__(self):
            return 'Node({!r}).format(self.root)'

        def post_order(self):
            yield self.root
            if self.left!=None:
                yield from self.left.post_order()
            if self.right!=None:
                yield from self.right.post_order()

        def in_order(self):
            if self.left!=None:
                yield from self.left.in_order()
            yield self.root 
            if self.right!=None:
                yield from self.right.in_order()

        def pre_order(self):
            if self.left!=None:
                yield from self.left.pre_order()
            if self.right!=None:
                yield from self.right.pre_order()
            yield self.root

    root = Node(8)
    node3 = Node(3)
    node1 = Node(1)
    node4 = Node(4)
    node6 = Node(6)
    node7 = Node(7)
    node10 = Node(10)
    node14 = Node(14)
    node13 = Node(13)
    root.add_leftChild(node3)
    node3.add_leftChild(node1)
    node3.add_rightChild(node6)
    node6.add_leftChild(node4)
    node6.add_rightChild(node7)
    root.add_rightChild(node10)
    node10.add_rightChild(node14)
    node14.add_leftChild(node13)

    for node in root.post_order():
        print("\npost_order:{}".format(node),end=' ')
    print('')
    for node in root.in_order():
        print("\nin_order :{}".format(node),end=' ')
    print('')
    for node in root.pre_order():
        print("\npre_order :{}".format(node),end=' ')
    print('')

if yieldFlag:
    def gen_list():
        for i in range(10,16):
            yield i
        for j in range(5):
            yield j * j
        for k in[100,200,300]:
            yield k

#★★★★★# combo multi list etc. reduce memory use
    for item in gen_list():
        print(item)

if masteryieldFlag:

    def consumer():
        i = None
        while True:    # 拿到 producer 發來的資料
            j = yield i
            print("consume {j}".format(j=j))

    def producer(c):
        c.__next__()
        for i in range(5):
            print("produce {i}".format(i=i))    # 發資料給 consumer
            c.send(i)
        c.close()

    c = consumer()          
    producer(c)

gc.collect()