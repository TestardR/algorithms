# s2[] = abcdefg
# s1[] = fg

class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2): return False
        
        s1Count = {}
        s2Count = {}
        for i in range(len(s1)):
            s1Count[s1[i]] = 1 + s1Count.get(s1[i], 0)
            s2Count[s2[i]] = 1 + s2Count.get(s2[i], 0)
            
        matches = 0
        for letter in "abcdefghijklmnopqrstuvwxyz":
            matches += 1 if s1Count.get(letter, 0) == s2Count.get(letter, 0) else 0
            
        if matches == 26:
                return True
            
        start = 0
        for end in range(len(s1), len(s2)):
            if matches == 26:
                return True

            s2Count[end] = 1 + s2Count.get(end, 0)
            
            if s1Count.get(s1[end], 0) == s2Count[end]:
                matches += 1
            elif s1Count.get(s1[end], 0) + 1 == s2Count[end]:
                matches -= 1
                
            s2Count[start] = s2Count.get(start, 0) - 1
            if s1Count.get(s1[start], 0) == s2Count[start]:
                matches += 1
            elif s1Count.get(s1[start], 0) - 1 == s2Count[start]:
                matches -= 1
            
            start += 1
            
        return matches == 26

# class Solution:
#     def checkInclusion(self, s1, s2):
#         if len(s1) > len(s2): return False
        
#         s1Count, s2Count = [0] * 26, [0] * 26
#         for i in range(len(s1)):
#             s1Count[ord(s1[i]) - ord("a")] += 1
#             s2Count[ord(s2[i]) - ord("a")] += 1
            
#         matches = 0
#         for i in range(26):
#             matches += 1 if s1Count[i] == s2Count[i] else 0
            
#         start = 0
#         for end in range(len(s1), len(s2)):
#             if matches == 26:
#                 return True

#             index = ord(s2[end]) - ord("a")
#             s2Count[index] += 1
            
#             if s1Count[index] == s2Count[index]:
#                 matches += 1
#             elif s1Count[index] + 1 == s2Count[index]:
#                 matches -= 1
                
#             index = ord(s2[start]) - ord("a")
#             s2Count[index] -= 1
#             if s1Count[index] == s2Count[index]:
#                 matches += 1
#             elif s1Count[index] - 1 == s2Count[index]:
#                 matches -= 1
            
#             start += 1
            
#         return matches == 26
            