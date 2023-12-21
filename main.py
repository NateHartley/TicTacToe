def game():
    # Init #
    str1 = "*"
    str2 = "*"
    str3 = "*"
    str4 = "*"
    str5 = "*"
    str6 = "*"
    str7 = "*"
    str8 = "*"
    str9 = "*"

    board = [
            [str1, str2, str3],
            [str4, str5, str6],
            [str7, str8, str9]
    ]

    counter = 0

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
            print("Win")
            return False
        
        # ALSO NEED TO CHECK IF ALL SPACES HAVE BEEN USED
        
        if counter % 2 == 0:
            print("-- Player 2's Turn --")
        else:
            print("-- Player 1's Turn --")

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
    if (((pos[0][0] == pos[1][1] and pos[1][1] == pos[2][2]) or 
        (pos[2][0] == pos[1][1] and pos[1][1] == pos[0][2])) and
        (pos[0][0] != "*" and pos[2][0] != "*")):
        print("DIAGS")
        return True
    
    # No win yet
    else:
        return False

def main():
    game()

if __name__ == "__main__":
    main()