class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

                box_index = (i // 3) * 3 + (j // 3)

                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False

                rows[i].append(num)
                cols[j].append(num)
                boxes[box_index].append(num)

        return True