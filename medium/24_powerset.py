# O(2^N * N) T | O(2^N * N) S
# T for each element we double the amount of subsets O(2^N)
# T the subsets are in average N / 2 length
# T O(2^N * N)

# Storing O(2^N) subsets of sizes N / 2 length
def powerSet(array):
    subsets = [[]]
    
    for element in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [element])
            
    return subsets


print(str(powerSet([1, 2, 3])))