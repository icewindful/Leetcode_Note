#import sys
import gc
#import os

zigzagflag01 = True
zigzagflag02 = False
test_str_01 = "PAYPALISHIRING"

#【★★★】
class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        N = (numRows - 1) * 2
        print("N = {} , numRows = {}".format(N,numRows))
        ### Max example 4 = (4-1) * 2 = 6 
        res = [""] * numRows
        for i in range(0, len(s)):
            pos = i % N if i % N < numRows else N - (i % N)
            # if (i%N) == 0 :
            #     print("no use check 【if i % N < numRows else N - (i % N )")
            #     pass
            print("i % N = {} , N - (i%N) = {}".format((i%N),(N-(i%N))))
            print("str = {str}, i={char} , pos = {array}".format(str = s[i] , char = i, array = pos))
            res[pos] += s[i]
            #print(res)
        return ''.join(res)

class Solution2:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lin = 0
        pl = 1
        outp = [""] * numRows
        for i in range(len(s)):
            outp[lin] += s[i]
            print("str = {str} , i = {char} , pos = {array}".format(str = s[i] , char = i , array = lin))
            if numRows > 1:
                lin += pl
                if lin == 0 or lin == numRows -1:
                    pl *= -1
        outputStr = ""
        for j in range(numRows):
            outputStr += outp[j]
        return outputStr        

if zigzagflag01:
    tmpstr = ""
    receive_str = Solution1.convert(tmpstr,test_str_01,4)
    print(receive_str)

    
if zigzagflag02:
    tmpstr = ""
    receive_str = Solution2.convert(tmpstr,test_str_01,4)
    print(receive_str)

gc.collect()