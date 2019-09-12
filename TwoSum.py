class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[]
        for i in range(0,len(nums)):
            rem=target-nums[i]
            print rem
            if rem in nums and nums.index(rem)!=i:
                l.append(i)
                l.append(nums.index(rem))
                break
        l.sort()
        return l
