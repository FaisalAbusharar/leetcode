class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                

        return prefix

        

sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
# print(sol.longestCommonPrefix(["racecar", "car", "dog"]))


