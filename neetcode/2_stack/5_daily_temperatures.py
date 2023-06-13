class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # top of the stack, first element in the array
                _, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res