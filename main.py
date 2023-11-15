def utility(board):
    return board.count('B')

def terminal_state(board):
    return '0' not in board

def print_board(board):
    print("Current Board:", board)

def flip_coins(board, position, player):
    opposite_player = 'W' if player == 'B' else 'B'

    i = position - 1
    while i >= 0 and board[i] == opposite_player:
        board[i] = player
        i -= 1

    i = position + 1
    while i < len(board) and board[i] == opposite_player:
        board[i] = player
        i += 1

def mini_max(board, depth, maximizing_player):
    if terminal_state(board) or depth == 0:
        return utility(board)

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(len(board)):
            if board[i] == '0':
                new_board = list(board)
                new_board[i] = 'B'
                flip_coins(new_board, i, 'B')
                max_eval = max(max_eval, mini_max(''.join(new_board), depth - 1, False))
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(len(board)):
            if board[i] == '0':
                new_board = list(board)
                new_board[i] = 'W'
                flip_coins(new_board, i, 'W')
                min_eval = min(min_eval, mini_max(''.join(new_board), depth - 1, True))
        return min_eval

# Get user input for initial state
initial_state = input("Enter the initial state: ")

# Set the initial state and print the board
current_board = initial_state
print_board(current_board)

# Calculate utility for the initial state
initial_utility = utility(current_board)
print("Utility of Player 1 (MAX) for initial state:", initial_utility)

# Simulate moves and calculate utility for different scenarios
for move in range(1, len(initial_state)+1):  # Simulate moves for each player until the board is full
    player = move % 2  # Alternating players (0 for Player 1, 1 for Player 2)
    coin = 'B' if player == 0 else 'W'

    # Get user input for the next move
    next_move = int(input(f"Enter the position (0-{len(current_board)-1}) for {coin}'s move: "))

    # Make the move and print the updated board
    current_board = list(current_board)
    current_board[next_move] = coin
    flip_coins(current_board, next_move, coin)
    current_board = ''.join(current_board)
    print_board(current_board)

    # Calculate utility for the updated state
    current_utility = mini_max(current_board, depth=3, maximizing_player=True)
    print(f"Utility of Player 1 (MAX) after {move} moves: {current_utility}")

    # Check for terminal state
    if terminal_state(current_board):
        print("Terminal state reached. Game over.")
        break
