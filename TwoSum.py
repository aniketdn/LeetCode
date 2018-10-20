class Solution:
    def twoSum(self, nums, target):
        lookup={}
        for i in range(0,len(nums)):
            if(target-nums[i] in lookup):
                return [lookup[target-nums[i]],i]
            lookup[nums[i]]=i
