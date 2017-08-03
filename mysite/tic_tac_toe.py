end = False

def print_grid(num):
    print("  | " + str(grid[num]) + " | " + " |  ")
    print("-----------")
    print("  | " + " | " + " |  ")
    print("-----------")
    print("  | " + " | " + " |  ")

grid = [0, 1, 2, 3 , 4 , 5, 6, 7, 8, 9]

while end is not True: 
    p1 = int(input("input your option player 1\n"))
    print_grid(p1)
