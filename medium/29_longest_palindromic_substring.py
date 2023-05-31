# 0(N^2) T | O(1) S
def longestPalindromicSubstring(string):
    currentLongest = [0, 1] # for slicing at the end [0:1], 1 is exclusive
    for i in range(1, len(string)):
        # we check every center of palindromes, a palindrome must have a center
        odd = getLongestPalindromeFrom(string, i - 1, i + 1) # 02 aa
        even = getLongestPalindromeFrom(string, i - 1, i) # 01 ab
        
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
    
    print(currentLongest)
    return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx]
        

print(str(longestPalindromicSubstring("abaxyzzyxf")))