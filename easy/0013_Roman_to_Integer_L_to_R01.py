#import sys
import gc
#import os

TestRunFlag = True
TestWord01 = "MCMXCIV"

values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        print("enter String:{}".format(TestWord01))
        total = values.get(s[-1])
        for i in reversed(range(len(s) - 1)):
            print("{}".format(i))
            if values[s[i]] < values[s[i + 1]]:
                print("s[{i01}]('{strNow}')({val01}) , s[{i02}]('{strNext}')({val02})".format(strNow=s[i],strNext=s[i+1],i01=i, i02=(i+1) , val01=values[s[i]] ,val02=values[s[i + 1]]))
                print("total({total}) = total({total}) - values[s[{i}]({values})]".format(total=total,i=i,values=values[s[i]]))
                total -= values[s[i]]
            else:
                print("s[{i01}]('{strNow}')({val01}) , s[{i02}]('{strNext}')({val02})".format(strNow=s[i],strNext=s[i+1],i01=i, i02=(i+1) , val01=values[s[i]] ,val02=values[s[i + 1]]))
                print("total({total}) = total({total}) + values[s[{i}]({values})]".format(total=total,i=i,values=values[s[i]]))
                total += values[s[i]]
        return total

if TestRunFlag:
    Answer = Solution.romanToInt(1,TestWord01)
    print("enter String:{}\nAnswer:{}".format(TestWord01,Answer))

gc.collect()
