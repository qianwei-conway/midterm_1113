# 1. In a Binary Tree populate next left of a tree.

# My solution's time complexity is O(N), where N is the tree nodes number.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, prev=None):
        self.val = val
        self.left = left
        self.right = right
        self.prev = prev

class Solution:
    def populateNextRight(self, root):
        if not root:
            return root

        rightmost = root

        while rightmost:
            next, curr = None, rightmost
            rightmost = None

            while curr:
                next, rightmost = self.processChild(curr.right, next, rightmost)
                next, rightmost = self.processChild(curr.left, next, rightmost)

                curr = curr.prev

        return root

    def processChild(self, childNode, next, rightmost):
        if childNode:
            if next:
                next.prev = childNode
            else:
                rightmost = childNode
            next = childNode
        return next, rightmost

# helper function
def listToTreeNode(inputValues):
    root = TreeNode(inputValues[0])
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item:
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item:
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

# test function
def printUsingPrev(root):
    result = []

    def dfs(root):
        if not root:
            return

        dfs(root.left)

        prev_val = str(root.prev.val) if root.prev else 'None'
        result.append(str(root.val) + '->' + prev_val)

        dfs(root.right)

    dfs(root)
    return result

# TEST
print(printUsingPrev(Solution().populateNextRight(listToTreeNode([1,2,3,4,None,5,6,None,7]))))
'''
          1
     2         3
  4     N   5     6
N   7
'''

print(printUsingPrev(Solution().populateNextRight(listToTreeNode([1,9,20,11,None,None,14,17,18]))))
'''
               1
        9            20
   11      N      N     14
17   18   N N    N N   N  N
'''