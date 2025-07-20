# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Converts linked list to Python list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Converts Python list to linked list
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

import math

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        curr = head
        dummy = ListNode(0)
        tail = dummy


        tail.next = ListNode(curr.val)
        tail = tail.next

        if curr.next is None: return dummy.next

        
        while curr and curr.next:
            greatestCommonFacotr = math.gcd(curr.val,curr.next.val)

            tail.next  = ListNode(greatestCommonFacotr)
            tail = tail.next

            tail.next = ListNode(curr.next.val)
            tail = tail.next

            curr = curr.next         

        return dummy.next   





        # if len(head) == 1: return abs(head[0])

        # newList = []

        # for i in range(len(head)-1):
        #     greatestCommonFacotr = math.gcd(head[i],head[i+1])
        #     if i == 0: newList.append(head[i])
        #     newList.append(greatestCommonFacotr)
        #     newList.append(head[i+1])

        # return newList

# ====== MAIN TEST ======

sol = Solution()

# Input as ListNode
# linked_input = list_to_linked_list([18,6,10,3])
linked_input = list_to_linked_list([7])



# Call the function
result = sol.insertGreatestCommonDivisors(linked_input)


print(result)  # Output will be a regular Python list
