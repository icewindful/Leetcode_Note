#import sys
import gc
#import os

TestFlag = True
TestSample01 = "()"
TestSample02 = "()[]{}"
TestSample03 = "(]"
TestSample04 = "(][)"
TestSample05 = "]["

class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        d = {'(':')', '{':'}','[':']'} #directory set like c++ maple
        stack = []
        print("string : {}".format(s))
        for i in s:
            print("i = {} ".format(i))
            if i in d:  # 1
                stack.append(i)
                print("get i '{}' push '{}' stack len={}".format(i,d[i],len(stack)))
            #elif len(stack) == 0 or d[stack.pop()] != i:  # 2
            #    return False
            elif len(stack) == 0 :
                return False
            else:
                tmp = d[stack.pop()]
                print("stack pop '{}' stack len={}".format(tmp,len(stack)))
                if tmp != i:
                    return False
        
        return len(stack) == 0 # 3

# 1. if it's the left bracket then we append it to the stack
# 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
# 3. finally check if the stack still contains unmatched left bracket

if TestFlag:
    print("{}{}\n".format(TestSample01,Solution.isValid(1,TestSample01)))
    
    print("{}{}\n".format(TestSample02,Solution.isValid(2,TestSample02)))
    # this sample d = '(' or ')' = 1 , '{' or '}' = 2 , '[' or ']' = 3

    # TestSample02 RunStep
    # 01 = stack.append (push) 1 get '(' , push ')'  , stack Len = 1
    # 02 = statk.pop (pop) 1 out , check ')' = ')' , stack Len = 0
    # 03 = stack.append (push) 1 get '[' , push ']'  , stack Len = 1
    # 04 = statk.pop (pop) 1 out , check ')' = ')' , stack Len = 0
    # 05 = stack.append (push) 1 get '{' , '}'  , stack Len = 1
    # 06 = statk.pop (pop) 1 out , check '}' = '}' , stack Len = 0
    # 07 check stack Len == 0 , Ture

    print("{}{}\n".format(TestSample03,Solution.isValid(3,TestSample03)))
    # TestSample03 RunStep
    # 01 = stack.append (push) 1 get '(' , push ')'  , stack Len = 1
    # 02 = statk.pop (pop) 1 out , check ']' != ')' , stack Len = 0
    # return False

    print("{}{}\n".format(TestSample04,Solution.isValid(3,TestSample04)))

    # TestSample04 RunStep
    # 01 = stack.append (push) 1 get '(' , push ')'  , stack Len = 1
    # 02 = statk.pop (pop) 1 out , check ']' != ')' , stack Len = 0
    # return False

    print("{}{}\n".format(TestSample05,Solution.isValid(3,TestSample05)))
    
gc.collect()