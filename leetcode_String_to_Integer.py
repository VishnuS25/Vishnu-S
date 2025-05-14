class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        sign=1
        i=0
        n=len(s)
        while i<n and s[i]==' ':
            i+=1
        if i<n and (s[i]=='-' or s[i]=='+'):
            sign=-1 if s[i]=='-' else 1
            i+=1
        while i<n and s[i].isdigit():
            ans=ans*10+int(s[i])
            if ans *sign<= -2**31:
                return -2**31
            if ans*sign >= 2**31 -1:
                return 2**31 -1
            i+=1
        return ans*sign
