class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColor = image[sr][sc]

        def floodFillHelper(row, col):
            if row < 0 or row > len(image) - 1: return
            if col < 0 or col > len(image[0]) -1: return

            if image[row][col] == color: return
            if image[row][col] != startColor: return

            image[row][col] = color

            floodFillHelper(row-1, col)
            floodFillHelper(row+1, col)
            floodFillHelper(row, col+1)
            floodFillHelper(row, col-1)

        floodFillHelper(sr, sc)
        return image