from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix)
        column_len = len(matrix[0])
        left = 0
        right = row_len * column_len - 1
        while left <= right:
            mid = (left + right) // 2
            mid_row = mid // column_len
            mid_col = mid % column_len

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Solution().searchMatrix(matrix, target))