def print_board(board):
    print("+---+---+---+")
    for i in range(3):
        row = " | ".join(board[i*3:(i+1)*3])
        print(f"| {row} |")
        print("+---+---+---+")

def check_win(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # collumns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_conditions)

def check_draw(board):
    return all(space in ["X", "O"] for space in board)

def get_valid_moves(board):
    return [i for i, spot in enumerate(board) if spot not in ["X", "O"]]

def bot_move(board):
    # Bot tries to win
    for move in get_valid_moves(board):
        board_copy = board[:]
        board_copy[move] = "O"
        if check_win(board_copy, "O"):
            return move
    # Bot tries to block player
    for move in get_valid_moves(board):
        board_copy = board[:]
        board_copy[move] = "X"
        if check_win(board_copy, "X"):
            return move
    # Take center if free
    if 4 in get_valid_moves(board):
        return 4
    # Take corners if free
    for move in [0, 2, 6, 8]:
        if move in get_valid_moves(board):
            return move
    # Take sides
    for move in [1, 3, 5, 7]:
        if move in get_valid_moves(board):
            return move

def main():
    # Initialize board with numbers 1-9 for display and input reference
    board = [str(i) for i in range(1, 10)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, the bot is O.")
    print("Pick a number 1-9 to place your X on the board.")
    print_board(board)

    while True:
        # Player move
        valid_moves = get_valid_moves(board)
        while True:
            try:
                player_move = int(input("Your move (1-9): ")) - 1
                if player_move in valid_moves:
                    board[player_move] = "X"
                    break
                else:
                    print("Invalid move. That spot is taken or out of range.")
            except ValueError:
                print("Please enter a number from 1 to 9.")

        print_board(board)
        if check_win(board, "X"):
            print("You won!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # Bot move
        bot_choice = bot_move(board)
        board[bot_choice] = "O"
        print(f"Bot moves to position {bot_choice + 1}:")
        print_board(board)
        if check_win(board, "O"):
            print("You lost!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":