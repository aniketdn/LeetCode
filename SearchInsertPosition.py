#  Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#  
#  You may assume no duplicates in the array.
#  
#  Example 1:
#  
#  Input: [1,3,5,6], 5
#  Output: 2
#  Example 2:
#  
#  Input: [1,3,5,6], 2
#  Output: 1
#  Example 3:
#  
#  Input: [1,3,5,6], 7
#  Output: 4
#  Example 4:
#  
#  Input: [1,3,5,6], 0
#  Output: 0


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        for i in range(0,len(nums)):
            if(i==0 and target<=nums[i]):
                nums.insert(i,target)
                return i
            elif(i==len(nums)-1 and nums[i]<=target):
                nums.insert(i,target)
                return len(nums)-1
            elif(nums[i]<=target and nums[i+1]>=target):
                nums.insert(i+1,target)
                return i+1
            else:
                continue
