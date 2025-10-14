def print_board(board):
    print("+---+---+---+")
    for i in range(3):
        row = " | ".join(board[i*3:(i+1)*3])
        print(f"| {row} |")
        print("+---+---+---+")


def check_win(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_conditions)


def check_draw(board):
    return all(space in ["X", "O"] for space in board)


def get_valid_moves(board):
    return [i for i, spot in enumerate(board) if spot not in ["X", "O"]]


def play_game():
    # Initialize board
    board = [str(i) for i in range(1, 10)]
    print("\nWelcome to Tic-Tac-Toe!")
    print("Player 1 is X and Player 2 is O.")
    print("Pick a number 1-9 to place your mark on the board.")
    print_board(board)

    current_player = "X"

    while True:
        valid_moves = get_valid_moves(board)
        while True:
            try:
                move = int(input(f"Player {current_player} move (1-9): ")) - 1
                if move in valid_moves:
                    board[move] = current_player
                    break
                else:
                    print("Invalid move. That spot is taken or out of range.")
            except ValueError:
                print("Please enter a number from 1 to 9.")

        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing Tic-Tac-Toe! Goodbye!")
            break


if __name__ == "__main__":
    main()
