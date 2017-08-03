def print_grid():
    print(" " + str(grid[0]) + " | " + str(grid[1]) + " | " + str(grid[2]))
    print("-----------")
    print(" " + str(grid[3]) + " | " + str(grid[4]) + " | " + str(grid[5]))
    print("-----------")
    print(" " + str(grid[6]) + " | " + str(grid[7]) + " | " + str(grid[8]))

def win_or_lose(end):
    if grid[0] == 'X' and grid[1] == 'X' and grid[2] =='X':
        print("Player 1 wins!")
        end = True

grid = [' ']*9

end = False

while end is not True:
    p1 = int(input("input your option player 1\n"))
    grid[p1] = 'X'
    win_or_lose(end)
    print_grid()
