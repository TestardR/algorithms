# def validateSubsequence(array, seq):
#     seqIdx = 0
#     for element in array:
#         if element == seq[seqIdx]:
#             seqIdx += 1
        
#         if seqIdx == len(seq):
#             return True
    
#     return False
        
def validateSubsequence(array, seq):
    seqIdx = 0
    arrIdx = 0
    
    while seqIdx < len(seq) and arrIdx < len(array):
        if seq[seqIdx] == array[arrIdx]:
            seqIdx += 1
            
        arrIdx += 1
        
    return seqIdx == len(seq)
        
# TC O(n)
# SC O(1)   
        
def main():
     print("Pair target sum: ", str(validateSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])))
         
main()