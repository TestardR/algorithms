class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None
        
def traverse(root, sequence):
    if not root:
        return len(sequence) == 0
    
    return find_path_recursive(root, sequence, 0)

def find_path_recursive(currentNode, sequence, sequenceIndex):
    if currentNode is None:
        return 0
    
    seqLen = len(sequence)
    
    if sequenceIndex >= seqLen or currentNode.val != sequence[sequenceIndex]:
        return False
    
    if currentNode.left is None and currentNode.right is None and sequenceIndex == seqLen -1:
        return True
    
    return find_path_recursive(currentNode.left, sequence, sequenceIndex + 1) or \
        find_path_recursive(currentNode.right, sequence, sequenceIndex + 1)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    
    print("Total sum of path numbers: " + str(traverse(root, [1, 1, 6])))
    
main()