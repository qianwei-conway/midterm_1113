# 2. Populate parent of each node. in the binary tree
# My solution's time complexity is O(N), where N is the number of tree nodes.

class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def populateParent(self, root):
        self.helper(root, None)
        return root

    def helper(self, root, parent):
        if not root:
            return

        root.parent = parent

        self.helper(root.left, root)
        self.helper(root.right, root)

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
def printUsingParent(root):
    result = []

    def dfs(root):
        if not root:
            return

        dfs(root.left)

        parent_val = str(root.parent.val) if root.parent else 'None'
        result.append(str(root.val) + '->' + parent_val)

        dfs(root.right)

    dfs(root)
    return result

# TEST
print( printUsingParent(Solution().populateParent(listToTreeNode([1,2,3,4,5,6,7]))) )
'''
       1
  2         3
4    5    6    7
'''
print( printUsingParent(Solution().populateParent(listToTreeNode([1,9,20,11,None,None,14,17,18]))) )
'''
               1
        9            20
   11      N      N     14
17   18   N N    N N   N  N
'''