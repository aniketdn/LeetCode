#  Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.
#  
#  Return a list of all powerful integers that have value less than or equal to bound.
#  
#  You may return the answer in any order.  In your answer, each value should occur at most once.
#  
#   
#  
#  Example 1:
#  
#  Input: x = 2, y = 3, bound = 10
#  Output: [2,3,4,5,7,9,10]
#  Explanation: 
#  2 = 2^0 + 3^0
#  3 = 2^1 + 3^0
#  4 = 2^0 + 3^1
#  5 = 2^1 + 3^1
#  7 = 2^2 + 3^1
#  9 = 2^3 + 3^0
#  10 = 2^0 + 3^2


class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        final=[]
        count=0
        innercount=0
        for i in range(0,100):
            if count>2:
                break
            else:
                o1=pow(x,i)
                if(o1>bound):
                    count=count+1
                    break
                else:
                    for j in range(0,100):
                        o2=pow(y,j)
                        if(o2>bound):
                            break
                        else:
                            if(bound>o1 or bound>o2):
                                out=o1+o2
                                if(out<=bound and out not in final):
                                    final.append(out)
                            else:
                                continue


        final.sort()
        return final

        
