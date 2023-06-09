class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getResult(string):
            result = ""
            count = 0
            for i in reversed(range(0, len(string))):
                char = string[i]
                if char == '#':
                    count += 1
                else: 
                    if count > 0:
                        count -= 1
                    else:
                        result += char

            return result

        return getResult(s) == getResult(t)