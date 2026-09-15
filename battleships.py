import random

SIZE = 3


def create_board():
    return [["." for _ in range(SIZE)] for _ in range(SIZE)]


def place_ships(board):
    # Place the 2-cell ship
    while True:
        direction = random.choice(["H", "V"])
        row = random.randint(0, SIZE - 1)
        col = random.randint(0, SIZE - 1)

        if direction == "H" and col < SIZE - 1:
            cells = [(row, col), (row, col + 1)]
        elif direction == "V" and row < SIZE - 1:
            cells = [(row, col), (row + 1, col)]
        else:
            continue

        for r, c in cells:
            board[r][c] = "S"

        break

    # Place two 1-cell ships
    ships_placed = 0

    while ships_placed < 2:
        row = random.randint(0, SIZE - 1)
        col = random.randint(0, SIZE - 1)

        if board[row][col] == ".":
            board[row][col] = "S"
            ships_placed += 1


def print_board(board, hide_ships=False):
    print("  1 2 3")
    for r in range(SIZE):
        print(r + 1, end=" ")

        for c in range(SIZE):
            cell = board[r][c]

            if hide_ships and cell == "S":
                cell = "."

            print(cell, end=" ")

        print()


def all_ships_sunk(board):
    for row in board:
        if "S" in row:
            return False
    return True


def get_shot():
    while True:
        try:
            row, col = map(
                int,
                input("Enter row and column (e.g. 1 2): ").split()
            )

            if 1 <= row <= SIZE and 1 <= col <= SIZE:
                return row - 1, col - 1

            print("Coordinates must be between 1 and 3.")

        except ValueError:
            print("Enter two numbers, for example: 2 3")


def take_turn(attacker_board):
    while True:
        row, col = get_shot()

        # Don't allow shooting the same cell twice
        if attacker_board[row][col] in ("X", "O"):
            print("You already shot there!")
            continue

        if attacker_board[row][col] == "S":
            attacker_board[row][col] = "X"
            print("Hit!")

            if all_ships_sunk(attacker_board):
                return True

            # Hit = another turn
            print("You get another shot!")
            print_board(attacker_board, hide_ships=True)

        else:
            attacker_board[row][col] = "O"
            print("Miss!")
            return False


def clear_screen():
    print("\n" * 30)


def main():
    player1_board = create_board()
    player2_board = create_board()

    place_ships(player1_board)
    place_ships(player2_board)

    current_player = 1

    print("=== 3x3 BATTLESHIPS ===")
    print("Each player has:")
    print("- 1 ship occupying 2 cells")
    print("- 2 ships occupying 1 cell")
    print()
    input("Press Enter to start...")

    while True:
        clear_screen()

        if current_player == 1:
            own_board = player1_board
            enemy_board = player2_board
        else:
            own_board = player2_board
            enemy_board = player1_board

        print(f"=== Player {current_player}'s Turn ===")
        print("\nYour board:")
        print_board(own_board)

        print("\nEnemy board:")
        print_board(enemy_board, hide_ships=True)

        print("\nMake your shot!")

        won = take_turn(enemy_board)

        if won:
            print(f"\n🎉 Player {current_player} wins!")
            break

        # Miss ends the turn
        current_player = 2 if current_player == 1 else 1

        input("\nPress Enter to continue...")


main()