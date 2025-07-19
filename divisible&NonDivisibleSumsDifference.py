class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        nonDivisble, divisible = [], []

        for i in range(n+1):
            if (i % m) != 0: nonDivisble.append(i)
            else: divisible.append(i)
        
        return sum(nonDivisble) - sum(divisible)
        

    
sol = Solution()

print(sol.differenceOfSums(10, 3)) # expect 19