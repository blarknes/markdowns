from typing import List


class Solution:
    numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)

    def solve(self, board: List[List[str]]) -> bool:
        i, j = self.nextEmptyCell(board)
        if i == -1:
            return True

        possible_values = self.possibleValues(i, j, board)
        if len(possible_values) == 0:
            return False

        for x in possible_values:
            board[i][j] = x
            if self.solve(board):
                return True
            board[i][j] = '.'

        return False

    def nextEmptyCell(self, board: List[List[str]]) -> int:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return i, j
        return -1, -1

    def getRow(self, i: int, board: List[List[str]]) -> set[str]:
        return set(board[i])

    def getColumn(self, j: int, board: List[List[str]]) -> set[str]:
        return set([x[j] for x in board])

    def getQuadrant(self, i: int, j: int, board: List[List[str]]) -> set[str]:
        return set([board[x][y] for x in self.customRange(i) for y in self.customRange(j)])

    def customRange(self, pos: int) -> range:
        return range((pos // 3 * 3), (pos // 3 * 3) + 3)

    def possibleValues(self, i: int, j: int, board: List[List[str]]) -> set[str]:
        return self.numbers - self.getRow(i, board) - self.getColumn(j, board) - self.getQuadrant(i, j, board)

    def prettyPrint(self, board: List[List[str]]) -> None:
        print()
        row_count = 0
        for row in board:
            line = ""
            cell_count = 0
            for cell in row:
                line += cell + " "
                cell_count += 1
                if cell_count == 3:
                    line += "| "
                    cell_count = 0
            line = line[:-2]
            if row_count == 3:
                print("------+-------+------")
                row_count = 0
            row_count += 1
            print(line)

if __name__ == "__main__":
    board_1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Solution().solveSudoku(board_1)
    Solution().prettyPrint(board_1)

    board_2 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    Solution().solveSudoku(board_2)
    Solution().prettyPrint(board_2)
