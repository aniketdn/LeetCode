class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        final=""
        for i in range(0,len(address)):
            if(address[i]=="."):
                final=final+"[.]"
            else:
                final=final+address[i]
        return final
        
