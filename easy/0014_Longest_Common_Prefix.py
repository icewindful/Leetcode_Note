#import sys
import gc
#import os

TestFlag = True
TestStrs01 = ["flower","flow","flight"]
TestStrs02 = ["dog","racecar","car"]

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        strs = sorted(strs,key = len)
        
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if strs[0][i] != strs[j][i]:
                    return res
            res += strs[0][i]
        return res

if TestFlag :
    print("{}".format(Solution.longestCommonPrefix(1,TestStrs01)))

gc.collect()