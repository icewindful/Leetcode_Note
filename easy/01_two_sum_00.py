#Space complexity O(n) 
#Space complexity O(n)
#Analysis one : target - nums , get complement value save in hashmap , if complement value add up nums = target , get Answer.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
