#  Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#  
#  Note: For the purpose of this problem, we define empty string as valid palindrome.
#  
#  Example 1:
#  
#  Input: "A man, a plan, a canal: Panama"
#  Output: true
#  Example 2:
#  
#  Input: "race a car"
#  Output: false


import re 

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=re.sub(r'\W+', '', s)
        print a
        b=a[::-1]
        if a.upper()==b.upper():
            return 1
        else:
            return 0
        
