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
        
        total = last_value = 0
        
        for letter in s:
            if values[letter] <= last_value: 
                print("total{total} += values{values[letter]}")
                total += values[letter]
            else:
                print("total({total} = total({total}) - ({last_value} x 2) + values[letter]({values})".format(total=total , last_value=last_value , values=values[letter]))
                total = total - (last_value * 2) + values[letter]
            last_value = values[letter]
            print("last_value={last_value}".format(last_value=last_value))
            print("{}".format(letter))
        return total


if TestRunFlag:
    Answer = Solution.romanToInt(1,TestWord01)
    print("enter String:{}\nAnswer:{}".format(TestWord01,Answer))

gc.collect()

# enter String:MCMXCIV
# first get string last = V = TotalValue = 5
# 5
# s[5]('I')(1) , s[6]('V')(5)
# total(5) = total(5) - values[s[5](1)]
# 4
# s[4]('C')(100) , s[5]('I')(1)
# total(4) = total(4) + values[s[4](100)]
# 3
# s[3]('X')(10) , s[4]('C')(100)
# total(104) = total(104) - values[s[3](10)]
# 2
# s[2]('M')(1000) , s[3]('X')(10)
# total(94) = total(94) + values[s[2](1000)]
# 1
# s[1]('C')(100) , s[2]('M')(1000)
# total(1094) = total(1094) - values[s[1](100)]
# 0
# s[0]('M')(1000) , s[1]('C')(100)
# total(994) = total(994) + values[s[0](1000)]
# enter String:MCMXCIV
# Answer:1994