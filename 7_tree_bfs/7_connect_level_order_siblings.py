from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None


def traverse(root):
    if root is None:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        previousNode = None
        levelSize = len(queue)

        for _ in range(levelSize):
            currentNode = queue.popleft()
            if previousNode:
                previousNode.next = currentNode
            previousNode = currentNode
            
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
            
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    traverse(root)

main()
