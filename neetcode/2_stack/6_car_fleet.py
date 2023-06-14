class Solution:
    def carFleet(self, target, position, speed):
        pair = [(p, s) for p, s in zip(position, speed)]
        # sorted by position, highest first
        # relative position will not change
        pair.sort(reverse=True, key = lambda x: x[0]) 
        stack = []
        
        # [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s) # Time to arrival
            # no while loop, we will be checking each car as we traverse in reverse order
            # [1.0, 7.0, 3.0]
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()
        return len(stack)


print(Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
