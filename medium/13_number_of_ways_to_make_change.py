# O(N) T | O(N) S
# denoms is the array of coin denominations
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for _ in range(n + 1)] # 0 to target amount n
    ways[0] = 1 # set to 0 as if our target amount is 0, there is only one way to change the amount
    
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
                # n = 10
                # denoms = [1, 5, 10, 25]
                # amount [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                # ways   [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4]
                
                # n = 9
                # denoms = [5]
                # amount [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                # ways   [1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    return ways[n]


print(str(numberOfWaysToMakeChange(9, [5])))