def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    
    #% Sort the list to make it easier to avoid duplicates and use two pointers
    nums.sort()
    res = []  #* This will store the unique triplets that sum to zero
    
    #& Loop through each number, treating it as the first element of the triplet
    for i in range(len(nums)):

        #! If the current number is the same as the previous, skip to avoid duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        #? Set up two pointers, one at the next element (j) and one at the end (k)
        j  = i + 1
        k = len(nums) - 1
        
        #! While the left pointer is less than the right pointer, keep checking for triplets
        while j < k:
            sum = nums[i] + nums[j] + nums[k]  #* Calculate the sum of the three numbers
            
            #? If the sum is too small, move the left pointer to the right (increase the sum)
            if sum < 0:
                j += 1
                
            #? If the sum is too large, move the right pointer to the left (decrease the sum)
            elif sum > 0:
                k -= 1
                
            #! If the sum is exactly 0, we found a valid triplet
            else:
                res.append([nums[i], nums[j], nums[k]])  #* Add the triplet to the result list
                j += 1  #? Move the left pointer to the right to look for new pairs
                
                #! Skip over duplicate values to avoid duplicate triplets
                while j < k and nums[j] == nums[j-1]:
                    j += 1
        
    return res  #* Return the list of unique triplets


#& Example usage:
print(threeSum([-1, 0, 1, 2, -1, -4]))
