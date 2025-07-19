class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        NumberList = [int(num) for num in str(x)]
        
        ReversedList = NumberList[::-1]  # Reverse the list
        
        return NumberList == ReversedList
        

Solution().isPalindrome(1212)