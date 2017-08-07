def print_grid():
    print(" " + str(grid[0]) + " | " + str(grid[1]) + " | " + str(grid[2]) + "          " + " 1 " + " | " + " 2 "  + " | " + " 3 ")
    print("-----------")
    print(" " + str(grid[3]) + " | " + str(grid[4]) + " | " + str(grid[5]) + "          " + " 4 " + " | " + " 5 "  + " | " + " 6 ")
    print("-----------")
    print(" " + str(grid[6]) + " | " + str(grid[7]) + " | " + str(grid[8]) + "          " + " 7 " + " | " + " 8 "  + " | " + " 9 ")

def win_or_lose():
    if (grid[0] == 'X' and grid[1] == 'X' and grid[2]) == 'X' or    \
            (grid[3] == 'X' and grid[4] == 'X' and grid[5]) == 'X' or   \
            (grid[6] == 'X' and grid[7] == 'X' and grid[8]) == 'X' or   \
            (grid[0] == 'X' and grid[3] == 'X' and grid[6]) == 'X' or   \
            (grid[1] == 'X' and grid[4] == 'X' and grid[7]) == 'X' or   \
            (grid[2] == 'X' and grid[5] == 'X' and grid[8]) == 'X' or   \
            (grid[0] == 'X' and grid[4] == 'X' and grid[8]) == 'X' or   \
            (grid[2] == 'X' and grid[4] == 'X' and grid[6]) == 'X':
        print("Player 1 wins!")
        return True

    if (grid[0] == 'O' and grid[1] == 'O' and grid[2]) == 'O' or   \
            (grid[3] == 'O' and grid[4] == 'O' and grid[5]) == 'O' or  \
            (grid[6] == 'O' and grid[7] == 'O' and grid[8]) == 'O' or  \
            (grid[0] == 'O' and grid[3] == 'O' and grid[6]) == 'O' or  \
            (grid[1] == 'O' and grid[4] == 'O' and grid[7]) == 'O' or  \
            (grid[2] == 'O' and grid[5] == 'O' and grid[8]) == 'O' or  \
            (grid[0] == 'O' and grid[4] == 'O' and grid[8]) == 'O' or  \
            (grid[2] == 'O' and grid[4] == 'O' and grid[6]) == 'O':
        print("Player 2 wins!")
        return True

grid = [' ']*9
print_grid()

while True:
    p1 = int(input("input your option player 1\n"))
    
    grid[p1-1] = 'X'
    print_grid()
    if win_or_lose():
        break

    p2 = int(input("input your option player 1\n"))

    grid[p2-1] = 'O'
    print_grid()
    if win_or_lose():
        break
