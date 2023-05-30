# O(N^2*N!) T | O(N*N!) S
# def getPermutations(array):
#     permutations = []
#     permutationsHelper(array, [], permutations)    
#     return permutations

# def permutationsHelper(array, currentPermutation, permutations):
#     if not len(array):
#         permutations.append(currentPermutation)
#     else: 
#         for i in range(len(array)):
#             newArray = array[i+1:] + array[:i] # remove current array[i] => remaining number O(N)
#             newPermutation = currentPermutation + [array[i]] # append num to permutation
#             permutationsHelper(newArray, newPermutation, permutations)

# O(N*N!) T | O(N*N!) S   
def getPermutations(array):
    permutations = []
    permutationsHelper(0, array, permutations)    
    return permutations

def permutationsHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else: 
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationsHelper(i + 1, array, permutations)
            swap(array, i, j)
              
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    
print(str(getPermutations([1, 2, 3])))