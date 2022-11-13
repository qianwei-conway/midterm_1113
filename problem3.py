# 3. In a Binary search tree print values which are inside of range. Optimize it if possible

# My solution's time complexity is about O(H) in average, where H is the height of the tree.
# But it could be O(N) if the tree is very skewed.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insideRange(self, root, min, max):
        result = []

        def dfs(root):
            if not root:
                return

            if min < root.val < max:
                result.append(root.val)
                dfs(root.left)
                dfs(root.right)
            elif root.val == min:
                result.append(root.val)
                dfs(root.right)
            elif root.val == max:
                result.append(root.val)
                dfs(root.left)
            elif root.val < min:
                dfs(root.right)
            else:
                dfs(root.left)

        dfs(root)
        return result

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
print( Solution().insideRange(listToTreeNode([7,3,13,1,5,9,20]), 4, 10) )
'''
      7
  3       13
1   5   9   20
'''