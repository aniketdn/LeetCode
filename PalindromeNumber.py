#  Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#  
#  Example 1:
#  
#  Input: 121
#  Output: true
#  Example 2:
#  
#  Input: -121
#  Output: false
#  Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#  Example 3:
#  
#  Input: 10
#  Output: false
#  Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1=str(x)
        revx=x1[::-1]
        for i in range(len(x1)):
            if(x1[i]!=revx[i]):
                return 0
        return 1
