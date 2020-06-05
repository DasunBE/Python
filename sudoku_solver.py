# DasunBE
from numpy import * # import all the functions via numpy ( you have to install this library first)

puzzle = [[1, 0, 0, 2, 0, 0, 3, 0, 5],
          [9, 0, 0, 0, 8, 5, 0, 0, 0],
          [8, 0, 0, 0, 0, 0, 0, 0, 0],
          [7, 0, 0, 6, 0, 0, 0, 1, 0],
          [6, 2, 0, 8, 0, 0, 0, 0, 0],
          [5, 0, 0, 0, 0, 0, 0, 2, 0],
          [4, 0, 0, 0, 0, 0, 7, 0, 0],
          [3, 1, 0, 5, 0, 0, 0, 0, 0],
          [2, 0, 0, 4, 0, 0, 1, 0, 3]]
mat = matrix(puzzle)  # convert the list to matrix using numpy library function call matrix('list name')
print(mat)  # print the befor solving puzzle


def check(row, col, val):
    global puzzle
    for i in range(9):  # check whether same value in the Row
        if puzzle[row][i] == val:
            return False
    for a in range(9):  # check whether same value in the column
        if puzzle[a][col] == val:
            return False
    y = (row // 3) * 3
    x = (col // 3) * 3
    for i in range(0, 3):  # check whether same value in same square
        for j in range(3):
            if puzzle[y + i][x + j] == val:
                return False
    return True


def solve():  # This function is used to solve the sudoku puzzle
    global puzzle  # global list convert as local list
    for y in range(9):
        for x in range(9):
            if puzzle[x][y] == 0:
                q: int
                for q in range(1, 10):
                    if check(x, y, q):  # condition will be true when send the function(check) return as true
                        puzzle[x][y] = q
                        #print("recursion") # for debug
                        solve()  # Recursion the function until get best solver
                        puzzle[x][y] = 0
                # print("return") # for debug
                return
    print("Soled puzzle is ")
    print(matrix(puzzle))  # print the solved puzzle
    input("Hit the Enter ")  # It's use to pause the loop but you hit the enter loop is start again


solve()  # call the function
