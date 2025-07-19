class Solution(object):
    def romanToInt(s):
        """
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        """
        
        cases = [["I","X","V"], ["X","L","C"], ["C","D","M"]]
        
        cnt = 0
        list_string = list(s)
        maxRange = len(list_string)
        
       
        for i in range(maxRange):
            
            if i == maxRange:
                break
            
            lastLetter = False
       
            if i == maxRange-1:
                lastLetter = True
            
            if list_string[i] == "M":
                cnt += 1000
            elif list_string[i] == "D":
                cnt += 500
                
            elif list_string[i] == "C":
                    if lastLetter == True:
                        cnt += 100
                        return cnt
                    if list_string[i+1] == "D": cnt += 400; del list_string[i+1]; maxRange -= 1;
                    elif list_string[i+1] == "M": cnt += 900; del list_string[i+1]; maxRange -= 1
                    else: cnt += 100
          
            elif list_string[i] == "L":
                    cnt += 50
                    
            elif list_string[i] == "X":
                    if lastLetter == True:
                        cnt += 10
                        return cnt
                    if list_string[i+1] == "L": cnt += 40; del list_string[i+1]; maxRange -= 1
                    elif list_string[i+1] == "C": cnt += 90; del list_string[i+1]; maxRange -= 1
                    else: cnt += 10
                    
            elif list_string[i] == "V":
                cnt += 5
            
            elif list_string[i] == "I":
                    if lastLetter == True:
                        cnt += 1
                        return cnt
                    if list_string[i+1] == "X": cnt += 9; del list_string[i+1]; maxRange -= 1
                    elif list_string[i+1] == "V": cnt += 4; del list_string[i+1]; maxRange -= 1
                    else: cnt += 1
                    
         
           
            
           
        return cnt
            
                
        
        
#print(Solution.romanToInt("MCMXCIV"))








#! --- BETTER CODE --- #!

class Solution:
    def BetterromanToInt(s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]: #% this shit is way to hard to explain. but basically, lets say we have "IX", since I < X is true, we -1 from ans, and then X adds 10, which becomes 9.
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans
    


##!!-----------------------------------!!##



#@ Writing my own version/replica of the code @#

class Solution:
    def ownVersionRomanToInt(s: str) -> int:
        m = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            } #!Here is the list, in correct order from greatest to smallest.

        ans = 0

        for i in range(len(s)):
            if i < len(s) -1 and m[s[i]] < m[s[i+1]]: #* if our string is letter "IX", we check if I(1) < X(10), which it is! we subtract 1 from the ans, leaving us with -1, then add 10 becoming 9.
                ans -= m[s[i]]
            else:
                ans += m[s[i]] #@ And if its not the case, such as "XI", X(10) < I(I), is false, so we want to add 10 to the ans and then add 1.
                
        return ans
    
    
print(
    Solution.ownVersionRomanToInt("VIVIVIMCIVIX")
    )
