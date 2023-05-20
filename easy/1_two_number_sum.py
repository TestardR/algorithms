""" def pair_with_target_sum(arr, k):
    diffMap = {}
    
    for el in arr:
        if el in diffMap:
            return (el, k-el)
        
        diffMap[k - el] = True
    
    return (-1, -1)

# TC O(n)
# SP O(n) """

def pair_with_target_sum(arr, k):
    arr.sort()
    left = 0
    right = len(arr) - 1
    
    while left < right:
        currSum = arr[left] + arr[right]
        
        if currSum == k:
            return (arr[left], arr[right])

        if k > currSum:
            left += 1
        else: 
            right -= 1
            
    return (-1, -1)    
        

# TC O(nlog(n)) from arr sort
# SC O(1)
    
    

def main():
    print("Pair target sum: ", str(pair_with_target_sum([3, 5, -4, 8, 11, 1, -1, 6], 10)))
     
        
main()