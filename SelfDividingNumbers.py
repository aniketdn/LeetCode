#  A self-dividing number is a number that is divisible by every digit it contains.
#  
#  For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
#  
#  Also, a self-dividing number is not allowed to contain the digit zero.
#  
#  Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
#  
#  Example 1:
#  Input: 
#  left = 1, right = 22
#  Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]


def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        out=[]
        for i in range(left,right+1):
            b=str(i)
            if '0' in b:
                continue
            else:
                a=i
                flag=1
                n=a%10
                while(n!=0 and i%n==0):
                    a=a/10
                    n=a%10
                if(n!=0 and i%n!=0):
                    flag=0
                if(flag==1):
                    out.append(i)
        return(out)
    
