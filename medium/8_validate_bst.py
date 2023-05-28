def validateBST(tree):
    return dfs(tree, float("-inf"), float("inf"))

def dfs(tree, lower, upper):
    if tree is None: # bottom of a branch
        return True
    
    if tree.value <= lower or tree.value >= upper:
        return False
    
    leftIsValid = dfs(tree.left, lower, tree.value)
    rightIsValid = dfs(tree.right, tree.value, upper)
    
    return leftIsValid and rightIsValid
