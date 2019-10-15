#  Given a non-empty array of integers, return the k most frequent elements.
#  
#  Example 1:
#  
#  Input: nums = [1,1,1,2,2,3], k = 2
#  Output: [1,2]
#  Example 2:
#  
#  Input: nums = [1], k = 1
#  Output: [1]

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l=[]
        c=[]
        for i in nums:
            if i not in l:
                a=nums.count(i)
                l.append(i)
                c.append(a)
                
        final=[]
        for i in range(0,k):
            elem=c.index(max(c))
            final.append(l[elem])
            l.remove(l[elem])
            c.remove(c[elem])
        
        return final
            
