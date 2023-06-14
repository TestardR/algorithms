class Solution:
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # current height is greater than top value
                index, height = stack.pop() 
                maxArea = max(maxArea, height * (i - index))
                # extend index backward
                start = index
            stack.append((start, h))

        # might have entries left in the stack
        # len(heights) as we know these were extended to the end of the histogram
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea