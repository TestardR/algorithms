# n = 6
# denoms = [1, 2, 4]
# amount          [0, 1, 2, 3, 4, 5, 6]
# numberOfCoins   [0, 1, 1, 2, 1, 2, 2]

# O(N*d) T | O(N) S
def minNumberOfCoinsForChange(n, denoms):
    numberOfCoins = [float("inf") for amount in range(n + 1)]
    numberOfCoins[0] = 0
    
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                numberOfCoins[amount] = min(numberOfCoins[amount], 1 + numberOfCoins[amount - denom])
                
    return numberOfCoins[n] if numberOfCoins[n] != float("inf") else -1


print(minNumberOfCoinsForChange(6, [1, 2, 4]))