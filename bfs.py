from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # Implement BFS for level order traversal here
        if not root:
            return
        
        res = []
        
        res.append([root.val])
        
        queue = deque([root])
        while queue:
            node = queue.popleft()  # Remove first element
            #print(node.val, end=" ")  # Visit node
            

            if node.left:
                queue.append(node.left)  # Add left child
            if node.right:
                queue.append(node.right)  # Add right child
        return res

# Test cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    sol = Solution()
    print(sol.levelOrder(root1))  # Expected output: [[3], [9, 20], [15, 7]]

    # Example 2
    root2 = TreeNode(1)
    print(sol.levelOrder(root2))  # Expected output: [[1]]
    
    # Example 3
    root3 = None
    print(sol.levelOrder(root3))  # Expected output: []