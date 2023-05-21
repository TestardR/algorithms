# [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
# Sum elements and multiply them by depth
# 5 + 2 + (7 - 1) x 2 + 3 ...

# O(n) T | O(d) S
def productSum(array, multiplier = 1):
    sum = 0
    
    for element in array: 
        if type(element) is list:
            sum += productSum(element, multiplier+1)
        else:
            sum += element
    
    return sum * multiplier