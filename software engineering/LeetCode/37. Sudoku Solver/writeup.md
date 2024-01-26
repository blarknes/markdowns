# 37. Sudoku Solver

## Information

**Difficulty**: Hard

## Description

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules:**

1. Each of the digits `1-9` must occur exactly once in each row.
2. Each of the digits `1-9` must occur exactly once in each column.
3. Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

The `'.'` character indicates empty cells.

**Example 1:**

![sudoku](./sudoku.png)

**Input:** board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
**Output:** [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
**Explanation:** The input board is shown above and the only valid solution is shown below:

![solution](./solution.png)

## Solution

The first step is to understand how Sudoku works, that being, there must be a number from 1 to 9 in each cell of the board, and there cannot be any repeated numbers in any row, column or quadrant.

So the first thing we must do is know which numbers are seeing a cell at any given moment, so let's make a function for each restriction:

```py
def getRow(self, i: int, board: List[List[str]]) -> set[str]:
    return set(board[i])

def getColumn(self, j: int, board: List[List[str]]) -> set[str]:
    return set([x[j] for x in board])

def getQuadrant(self, i: int, j: int, board: List[List[str]]) -> set[str]:
    return set([board[x][y] for x in self.customRange(i) for y in self.customRange(j)])
```

That being said, we also need to know which numbers are possible to each cell, which can be done by subtracting the seeing numbers from all the possible numbers (1 to 9):

```py
def possibleValues(self, i: int, j: int, board: List[List[str]]) -> set[str]:
    return self.numbers - self.getRow(i, board) - self.getColumn(j, board) - self.getQuadrant(i, j, board)
```

The next step is the backbone of the algorithm, the solving. Which will take some preparation, let's start by finding out the next empty cell starting from [0, 0]:

> note that in this case when there is no empty cell the function will return -1, -1, so that we can know when the sudoku is solved

```py
def nextEmptyCell(self, board: List[List[str]]) -> int:
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                return i, j
    return -1, -1
```

And down we go to the main function, which will consist of three (4) main steps:

```py
def solve(self, board: List[List[str]]) -> bool:
    # first we check for the coordinates of the next empty cell
    i, j = self.nextEmptyCell(board)
    # if there are none, we return True, our board is completely filled
    if i == -1:
        return True

    # here we check how many numbers from 1 - 9 are valid for the cell
    possible_values = self.possibleValues(i, j, board)
    # if there are 0 possible numbers to fill the cell, our solution is wrong and we need to backtrack a bit
    if len(possible_values) == 0:
        return False

    # for each of the possible numbers, we will recursively try and fill the board
    for x in possible_values:
        board[i][j] = x
        # if the number filled was valid, this will return true each time, thus solving our board
        if self.solve(board):
            return True
        # if we hit the possible_values == 0, we need to backtrac, so we fill the cell with the previous dot
        board[i][j] = '.'

    # if we got to this part we got 0 possible values in the cell, so our solution is wrong, and we need to go back one step and try the next possible value
    return False
```

And that is it, a handmade Sudoku solver!