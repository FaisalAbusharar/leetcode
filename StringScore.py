class Solution(object):
    def scoreOfString(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        stringList= list(s)
        for i in range(len(stringList)-1):
            if (len(stringList)-1) != i:
                stringList[i] = abs(ord(stringList[i]) - ord(stringList[i+1]))
           
        stringList.pop()
        return sum(stringList)
    
sol = Solution()

print(sol.scoreOfString("hello"))