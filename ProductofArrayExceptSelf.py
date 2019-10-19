#  Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#  
#  Example:
#  
#  Input:  [1,2,3,4]
#  Output: [24,12,8,6]
#  Note: Please solve it without division and in O(n).


class Solution(object):

        
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l,r,final=[0]*len(nums),[0]*len(nums),[0]*len(nums)
        l[0]=1
        r[len(nums)-1]=1
        for i in range(1,len(nums)):
            l[i]=nums[i-1]*l[i-1]
        for i in range(len(nums)-2,-1,-1):
            r[i]=nums[i+1]*r[i+1]
        for i in range(0,len(nums)):
            final[i]=l[i]*r[i]
        return final

    
