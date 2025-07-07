import random

def print_board(board):
    print("+---+---+---+")
    for i in range(3):
        row = f"| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |"
        print(row)
        print("+---+---+---+")

def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combinations)

def available_moves(board):
    return [i for i, spot in enumerate(board) if spot not in ['X', 'O']]

def bot_move_easy(board):
    return random.choice(available_moves(board))

def bot_move_hard(board, bot, human):
    # Try to win
    for move in available_moves(board):
        copy = board[:]
        copy[move] = bot
        if check_winner(copy, bot):
            return move
    # Try to block human
    for move in available_moves(board):
        copy = board[:]
        copy[move] = human
        if check_winner(copy, human):
            return move
    # Take center if available
    if board[4] not in ['X', 'O']:
        return 4
    # Take a corner if available
    for move in [0, 2, 6, 8]:
        if board[move] not in ['X', 'O']:
            return move
    # Else, pick random
    return bot_move_easy(board)

def bot_move(board, bot, human):
    difficulty = random.choice(['easy', 'medium', 'hard'])
    print(f"[Bot difficulty: {difficulty.upper()}]")
    if difficulty == 'easy':
        return bot_move_easy(board)
    elif difficulty == 'medium':
        return bot_move_hard(board, bot, human) if random.random() > 0.5 else bot_move_easy(board)
    else:
        return bot_move_hard(board, bot, human)

def play_game():
    board = [str(i+1) for i in range(9)]  # Numbered initial board
    human = 'X'
    bot = 'O'
    current = human if random.choice([True, False]) else bot
    print(f"You are {human}. Bot is {bot}.\n")

    for _ in range(9):
        print_board(board)
        if current == human:
            while True:
                try:
                    move = int(input("Choose a position (1-9): ")) - 1
                    if move in available_moves(board):
                        board[move] = human
                        break
                    else:
                        print("Invalid or occupied position.")
                except ValueError:
                    print("Enter a valid number from 1 to 9.")
        else:
            move = bot_move(board, bot, human)
            print(f"Bot chooses {move + 1}")
            board[move] = bot

        if check_winner(board, current):
            print_board(board)
            print(f"{'You win!' if current == human else 'Bot wins!'}")
            return
        current = bot if current == human else human

    print_board(board)
    print("It's a draw!")

play_game()