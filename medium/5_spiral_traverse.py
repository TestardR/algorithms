# O(N) T | O(N) S
def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        # top row
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        # right column
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        # bottom row
        # endCol wihtout + 1 to exclude ending column
        for col in reversed(range(startCol, endCol)):
            result.append(array[endRow][col])

        # left column
        for row in reversed(range(startRow + 1, endRow)):
            result.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result

# array[row][column]

# loop from SC to EC (incl.)
# top row array[SR][col]

# loop from SR + 1 to ER (incl.)
# right column array[row][EC]

# loop from SC to EC (excl.)
# bottom row array[ER][col]

# loop from SR + 1 to ER (excl.)
# left column array[row][SC]

# SC + 1
# EC - 1
# SR + 1
# ER - 1


[  # SC        #EC
    #SR  [ 1,  2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    #ER  [10,  9,  8, 7],
]


def spiralTraverse(array):
    result = []

    spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)

    return result


def spiralFill(array, startRow, endRow, startCol, endCol, result):
    if startRow > endRow or startCol > endCol:
        return

    while startRow <= endRow and startCol <= endCol:
        # top row
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        # right column
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        # bottom row
        # endCol wihtout + 1 to exclude ending column
        for col in reversed(range(startCol, endCol)):
            result.append(array[endRow][col])

        # left column
        for row in reversed(range(startRow + 1, endRow)):
            result.append(array[row][startCol])

        spiralFill(array, startRow+1, endRow - 1,
                   startCol+1, endCol+1, endCol - 1, result)
