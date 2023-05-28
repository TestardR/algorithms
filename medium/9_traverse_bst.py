# O(N) T | O(N) S
def inOrderTraverse(tree, array): # bottom left upward
    if tree is None:
        return array
    
    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)

# O(N) T | O(N) S
def preOrderTraverse(tree, array): # top left then right
    if tree is None:
        return array
    
    array.append(tree.value)
    inOrderTraverse(tree.left, array)
    inOrderTraverse(tree.right, array)

# O(N) T | O(N) S
def postOrderTraverse(tree, array): # top left then right
    if tree is None:
        return array
    
    inOrderTraverse(tree.left, array)
    inOrderTraverse(tree.right, array)
    array.append(tree.value)