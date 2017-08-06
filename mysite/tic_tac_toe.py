def print_grid():
    print(" " + str(grid[0]) + " | " + str(grid[1]) + " | " + str(grid[2]))
    print("-----------")
    print(" " + str(grid[3]) + " | " + str(grid[4]) + " | " + str(grid[5]))
    print("-----------")
    print(" " + str(grid[6]) + " | " + str(grid[7]) + " | " + str(grid[8]))

def win_or_lose():
    if grid[0] and grid[1] and grid[2] =='X':
        print("Player 1 wins!")
        end = True
        return end

    if grid[3] and grid[4] and grid[5] =='X':
        print("Player 1 wins!")
        end = True
        return end

    if grid[6] and grid[7] and grid[8] =='X':
        print("Player 1 wins!")
        end = True
        return end


    if grid[0] and grid[3] and grid[6] =='X':
        print("Player 1 wins!")
        end = True
        return end

    if grid[1] and grid[4] and grid[7] =='X':
        print("Player 1 wins!")
        end = True
        return end

    if grid[2] and grid[5] and grid[8] =='X':
        print("Player 1 wins!")
        end = True
        return end

    if grid[0] and grid[4] and grid[8] =='X':
        print("Player 1 wins!")
        end = True
        return end

    if grid[2] and grid[4] and grid[6] =='X':
        print("Player 1 wins!")
        end = True
        return end

    if grid[0] and grid[1] and grid[2] =='O':
        print("Player 2 wins!")
        end = True
        return end

    if grid[3] and grid[4] and grid[5] =='O':
        print("Player 2 wins!")
        end = True
        return end

    if grid[6] and grid[7] and grid[8] =='O':
        print("Player 2 wins!")
        end = True
        return end

    if grid[0] and grid[3] and grid[6] =='O':
        print("Player 2 wins!")
        end = True
        return end

    if grid[1] and grid[4] and grid[7] =='O':
        print("Player 2 wins!")
        end = True
        return end

    if grid[2] and grid[5] and grid[8] =='O':
        print("Player 2 wins!")
        end = True
        return end

    if grid[0] and grid[4] and grid[8] =='O':
        print("Player 2 wins!")
        end = True
        return end

    if grid[2] and grid[4] and grid[6] =='O':
        print("Player 2 wins!")
        end = True
        return end



grid = [' ']*9

end = False

while end is not True:
    p1 = int(input("input your option player 1\n"))
    grid[p1] = 'X'
    end = win_or_lose()
    print_grid()
    if end == True:
        break

    p2 = int(input("input your option player 2\n"))
    grid[p2] = 'O'
    end = win_or_lose()
    print_grid()
    if end == True:
        break
