from collections import Counter
import heapq
class Solution(object):
    def reorganizeString(s):
        count = Counter(s)
        maxHeap = [[-cnt,char] for char, cnt in count.items()] #Python dosent have a maxHeap function, so we want to use a minHeap but have the count in negative.
        heapq.heapify(maxHeap) #heapify the maxHeap
        
        res = "" 
        prev = None
        
        while maxHeap or prev:
            if not maxHeap and prev: #if the prev is not empty and the maxHeap is, then we cannot do anything so we will instead return ""
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1
            
            if prev: #if the prev is not empty, then push the prev back into the maxHeap
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0: #if the count isnt equal to 0, meaning there are letters still left, set the prev = [cnt,char]
                prev = [cnt,char]
        return res
        



print(Solution.reorganizeString(s="aab"))