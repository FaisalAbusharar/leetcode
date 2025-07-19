class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        numsSorted = sorted((num, i) for i, num in enumerate(nums))
    
        r, l = 0, len(nums) - 1

        while r < l:
            sumVal = numsSorted[r][0] + numsSorted[l][0]
            
            if sumVal == target:
                return [numsSorted[r][1], numsSorted[l][1]]  # Return original indices
            
            if sumVal > target:
                l -= 1
            else:
                r += 1

        return None
            
#print(Solution.twoSum("__main__", [2,7,11,15], 9))
print(Solution.twoSum("__main__", [3,2,4], 6))
print(Solution.twoSum("__main__", [3,3], 6))

