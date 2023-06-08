class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        number = 0
        prev = 0
        romanToInt = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        for letter in s[::-1]:
            number = romanToInt[letter]

            if number < prev:
                answer -= number
            else: 
                answer += number

            prev = number

        return answer