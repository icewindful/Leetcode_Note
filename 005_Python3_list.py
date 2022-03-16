#coding: utf-8

import gc
import pprint

listFlag = False
tupleFlag = False
dictFlag = True

if listFlag:
    alist = [1,2,3,4,5,6]
    blist = ["abc","xyz",'a','b','c']
    clist = [9,8,7,4,3,2,6,5,1,0]
    orialist = alist[:]
    oriblist = blist[:]
    oriclist = clist[:]
    x = 9999
    y = 3
    z = "Genius"
    aindex = 3
    bindex = 4

    print("{list01} .append({item02}) :{method}\n{list02} after list".format(list01 = orialist ,item02 = x ,method = alist.append(x) ,list02 = alist))
    print("{list01} .append({item02}) :{method}\n{list02} after list".format(list01 = oriblist ,item02 = z ,method = blist.append(z) ,list02 = blist))

    print("{list01} .pop() :{method}\n{list02} after list".format(list01 = orialist ,method = alist.pop() ,list02 = alist))
    print("{list01} .pop() :{method}\n{list02} after list".format(list01 = oriblist ,method = blist.pop() ,list02 = blist))

    print("{list01} .insert({item02}) :{method}\n{list02} after list".format(list01 = orialist ,item02 = x ,method = alist.insert(aindex,x) ,list02 = alist))
    print("{list01} .insert({item02}) :{method}\n{list02} after list".format(list01 = oriblist ,item02 = z ,method = blist.insert(bindex,z) ,list02 = blist))

    print("{list01} .extend({item02}) :{method}\n{list02} after list".format(list01 = orialist ,item02 = x ,method = alist.extend(blist) ,list02 = alist))
    print("{list01} .sort() :{method}\n{list02} after list".format(list01 = oriclist ,method = clist.sort() ,list02 = clist))
    print("{list01} .clear() :{method}\n{list02} after list".format(list01 = orialist ,method = alist.clear() ,list02 = alist))
    alist = orialist[:]
    print("{list01} .reverse() :{method}\n{list02} after list".format(list01 = orialist ,method = alist.reverse() ,list02 = alist))

    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    
    for q, a in zip(questions, answers):
        print('What is your {str01}?  It is {str02}.'.format(str01=q, str02=a))

    
    del alist ,blist ,x ,y ,z ,orialist ,oriblist ,aindex ,bindex
    gc.collect()

if tupleFlag:
    atuple = (1,2,3,4,5,6)
    btuple = ("abc","xyz",'a','b','c')
    x = 1
    y = 3
    z = "Genius"
    
    del atuple ,btuple ,x ,y ,z 
    gc.collect()

if dictFlag:
    adict = {"abc":9999, "xyz":7259 , 1:"icewindful" , 2:"speed" }
    bdict = {"qwe":9999, "asd":7259 , 3:"is good" , 4:"star" }
    cdict = {"tuple":("a","b",3),"int":set([1,2,3,4]) }
    aitem = "cloud"
    akey = 9527
    bitem = "sky"
    bkey = 1110

    print("{dict01} item()\n{method}".format(dict01=adict ,method=adict.items()))
    print("{dict01} keys()\n{method}".format(dict01=adict ,method=adict.keys()))
    print("{dict01} values()\n{method}".format(dict01=adict ,method=adict.values()))
    print("{dict01} update()\n{method}".format(dict01=adict ,method=adict.update(bdict)))
    pprint.pprint(cdict)
    print(cdict)

    del adict , aitem , akey , bitem ,bkey
    gc.collect()
