#  Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#  
#  Note: The algorithm should run in linear time and in O(1) space.
#  
#  Example 1:
#  
#  Input: [3,2,3]
#  Output: [3]
#  Example 2:
#  
#  Input: [1,1,1,3,3,2,2,2]
#  Output: [1,2]

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        final=[]
        for i in range(0,len(nums)):
            if(nums[i] not in l):
                a=nums.count(nums[i])
                if a > (len(nums)/3):
                    final.append(nums[i])
                    l.append(nums[i])
                else:
                    l.append(nums[i])
        return final
