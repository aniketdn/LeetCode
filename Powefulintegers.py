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

        
