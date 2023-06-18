class Solution:
    def minWindow(self, s, t):
        if t == "":
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
            
        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float("inf")
        
        start = 0
        for end in range(len(s)):
            c = s[end]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
                
            while have == need:
                if (end - start + 1) < resLen:
                    res = [start, end]
                    resLen = end - start + 1
                    
                window[s[start]] -= 1
                if s[start] in countT and window[s[start]] < countT[s[start]]:
                    have -= 1
                
                start +=1
        
        start, end = res
        return s[start:end+1] if resLen != float("inf") else ""
                
            
            