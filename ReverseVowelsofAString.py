#  Write a function that takes a string as input and reverse only the vowels of a string.
#  
#  Example 1:
#  
#  Input: "hello"
#  Output: "holle"
#  Example 2:
#  
#  Input: "leetcode"
#  Output: "leotcede"
#  Note:
#  The vowels does not include the letter "y".

def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel=['a','e','i','o','u','A','E','I','O','U']
        v=[]
        sa=[]
        for i in range(0,len(s)):
            sa.append(str(s[i]))
            if s[i] in vowel:
                v.append(str(s[i]))   
        v.reverse()
        
        #print v
        vcount=0
        for i in range(0,len(sa)):
            if sa[i] in vowel:
                sa[i]=v[vcount]
                vcount+=1
        
        return ''.join(sa)
