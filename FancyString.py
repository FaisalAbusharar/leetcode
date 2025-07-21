class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # stringList = list(s)
        # listToRemove = []
      
        # for i in range(len(stringList) -2 ):
        #     if stringList[i] == stringList[i+1] == stringList[i+2]:
        #         listToRemove.append(i+1)         

        # return ''.join([value for i, value in enumerate(stringList) if i not in listToRemove]) #! This is the main bottleneck.

        #? Method above works, but is regarded too slow for large strings, so gotta make a new one.

        stringList = list(s)
        result = [stringList[0]]
        count = 1

        for i in range(1, len(stringList)):
            if stringList[i] == stringList[i - 1]:
                count += 1
            else:
                count = 1

            if count < 3:
                result.append(stringList[i])

        return ''.join(result)


        #! This method lightning fast, its crazyy..



sol = Solution()


print(sol.makeFancyString("leeetcode")) #& Expected: leetcode
print(sol.makeFancyString("aaabaaaa")) #& Expected: aabaa
print(sol.makeFancyString("aab")) #& Expected: aab

