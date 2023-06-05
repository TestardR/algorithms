class Solution:
    def validPalindrome(self, s: str) -> bool:
        leftIdx = 0
        rightIdx = len(s) - 1

        while leftIdx < rightIdx:
            if s[leftIdx] != s[rightIdx]:
                return self.validPalindromeHelper(s, leftIdx+1, rightIdx) or self.validPalindromeHelper(s, leftIdx, rightIdx-1)
            leftIdx += 1
            rightIdx -= 1

        return True


    def validPalindromeHelper(self, string, leftIdx, rightIdx):
        while leftIdx < rightIdx:
            if string[leftIdx] != string[rightIdx]:
                return False
            leftIdx += 1
            rightIdx -= 1

        return True