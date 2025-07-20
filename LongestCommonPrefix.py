class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = []

        for i in range(len(strs)):
            for c1, c2 in zip(str[i], str[i+1]):
                if c1==c2:
                    prefix.append(c1)
                else:
                    break
            return ''.join(prefix)


        




sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
# print(sol.longestCommonPrefix(["racecar", "car", "dog"]))
