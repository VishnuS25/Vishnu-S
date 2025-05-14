class Solution(object):
    def reverse(self, x):
        strX=str(x)
        lenstrX=len(strX)
        reverseInt=""
        for i in range(1,lenstrX+1):
            if x<0 and i== lenstrX:
                continue
            reverseInt +=strX[-i]
        if int(reverseInt)>-(2**31) and int(reverseInt)<(2**31 -1):
            if x<0: return -(int(reverseInt))
            else: return int(reverseInt)
        return 0
