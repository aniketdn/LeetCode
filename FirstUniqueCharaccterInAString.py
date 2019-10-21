#  Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#  
#  Examples:
#  
#  s = "leetcode"
#  return 0.
#  
#  s = "loveleetcode",
#  return 2.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        l=len(s)
        if l==0:
            return -1
        if l==1:
            return 0
        else:
            for i in range(0,l):
                if i==0:
                    if s.count(s[i])==l:
                        return -1
                if s[i] in s[0:i] or s[i] in s[i+1:l]:
                    count+=1
                else:
                    return count
            if count==l:
                return -1
        
