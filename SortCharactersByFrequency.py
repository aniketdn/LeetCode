#  Given a string, sort it in decreasing order based on the frequency of characters.
#  
#  Example 1:
#  
#  Input:
#  "tree"
#  
#  Output:
#  "eert"
#  
#  Explanation:
#  'e' appears twice while 'r' and 't' both appear once.
#  So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
#  Example 2:
#  
#  Input:
#  "cccaaa"
#  
#  Output:
#  "cccaaa"
#  
#  Explanation:
#  Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
#  Note that "cacaca" is incorrect, as the same characters must be together.
#  Example 3:
#  
#  Input:
#  "Aabb"
#  
#  Output:
#  "bbAa"
#  
#  Explanation:
#  "bbaA" is also a valid answer, but "Aabb" is incorrect.
#  Note that 'A' and 'a' are treated as two different characters.

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        for i in range(0,len(s)):
            if s[i] not in d:
                a=s.count(s[i])
                d[s[i]]=a
        finals=""
        while (len(finals)!=len(s)):
            inverse = [(value, key) for key, value in d.items()]
            a=max(inverse)[0]
            for i in range(0,a):
                finals=finals+max(inverse)[1]
            d.pop(max(inverse)[1])
        return finals
            
