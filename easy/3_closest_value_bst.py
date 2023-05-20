import math

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def findClosest(root, target):
    closest = math.inf
    currentNode = root
    
    while currentNode:
        if abs(closest - target) > abs(currentNode.val - target):
            closest = currentNode.val
        
        if target > currentNode.val:
            currentNode = currentNode.right
        elif target < currentNode.val:
            currentNode = currentNode.left
        else:
            break
        
    return closest

    
""" def findClosest(tree, target):
    return findClosestValueBSThelper(tree, target, math.inf)

def findClosestValueBSThelper(tree, target, closest):
    if tree is None:
        return closest
    
    if abs(target - tree.val) < abs(target - closest):
        closest = tree.val
        
    if target > tree.val:
        return findClosestValueBSThelper(tree.right, target, closest)
    elif target < tree.val:
        return findClosestValueBSThelper(tree.left, target, closest)
    else:
        return closest """
         
# TC O(logN) -> removing half of the tree
# SC O(1) 


def main():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(1)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(22)
    root.right.left.right = TreeNode(14)
    
    print("Level order traversal: " + str(findClosest(root, 4)))
    
main()
    