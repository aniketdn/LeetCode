#  We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
#  
#  Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
#  Example:
#  Input: 28
#  Output: True
#  Explanation: 28 = 1 + 2 + 4 + 7 + 14


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        temp=[]
        h=num/2
        if num<=1:
            return 0
        sum=1
        for i in range(2,int(math.sqrt(num) + 1)):
            if(num%i==0):
                sum=sum+(num/i)+i
                print sum
        if(sum==num):
            return 1
        else:
            return 0
