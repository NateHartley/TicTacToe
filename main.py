def game():
    # Init #
    counter = 0
    pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9 = "*", "*", "*", "*", "*", "*", "*", "*", "*"

    board = [
            [pos1, pos2, pos3],
            [pos4, pos5, pos6],
            [pos7, pos8, pos9]
    ]

    while(True):
        counter += 1

        # Board #
        print('''
            %s %s %s
            %s %s %s
            %s %s %s
            ''' 
            % (board[0][0], board[0][1], board[0][2], 
               board[1][0], board[1][1], board[1][2], 
               board[2][0], board[2][1], board[2][2]))
        
        # Check for winner
        if winnings(board) == True:
            print("Player 1 wins!") if counter % 2 == 0 else print("Player 2 wins!"); return False
        
        # Checks for no available spaces
        if ("*" not in board[0]) and ("*" not in board[1]) and ("*" not in board[2]):
            print("No more spaces available, and no winners. GAME OVER!")
            return False
        
        print("-- Player 2's Turn --") if counter % 2 == 0 else print("-- Player 1's Turn --")

        # Select row #
        row = int(input("Enter a row number: "))
        if row != 1 and row != 2 and row != 3:
            print("This is not a valid row, must be between 1 - 3")
            return False

        # Select column #
        col = int(input("Enter a column number: "))
        if col != 1 and col != 2 and col != 3:
            print("This is not a valid column, must be between 1 - 3")
            return False
        
        if board[row-1][col-1] == "X" or board[row-1][col-1] == "O":
            print("This space is already taken")
        else:
            if counter % 2 == 0:
                board[row-1][col-1] = "O"
            else:
                board[row-1][col-1] = "X"
        
def winnings(pos):
    # Rows
    if (((pos[0][0] == "X" or pos[0][0] == "O") and (pos[0][0] == pos[0][1] and pos[0][1] == pos[0][2])) or
        (pos[1][0] == "X" or pos[1][0] == "O") and (pos[1][0] == pos[1][1] and pos[1][1] == pos[1][2]) or
        (pos[2][0] == "X" or pos[2][0] == "O") and (pos[2][0] == pos[2][1] and pos[2][1] == pos[2][2])):
        return True
    
    # Columns
    if (((pos[0][0] == "X" or pos[0][0] == "O") and (pos[0][0] == pos[1][0] and pos[1][0] == pos[2][0])) or
        (pos[0][1] == "X" or pos[0][1] == "O") and (pos[0][1] == pos[1][1] and pos[1][1] == pos[2][1]) or
        (pos[0][2] == "X" or pos[0][2] == "O") and (pos[0][2] == pos[1][2] and pos[1][2] == pos[2][2])):
        return True
    
    # Diagonals
    if (((pos[0][0] == "X" or pos[0][0] == "O") and (pos[0][0] == pos[1][1] and pos[1][1] == pos[2][2])) or
        (pos[2][0] == "X" or pos[2][0] == "O") and (pos[2][0] == pos[1][1] and pos[1][1] == pos[0][2])):
        return True
    
    # No win yet
    else:
        return False

def main():
    game()

if __name__ == "__main__":
    main()