import random

SIZE = 3


def create_board():
    return [["." for _ in range(SIZE)] for _ in range(SIZE)]


def place_ships():
    """Create a board containing only the ships."""
    board = create_board()

    # Place the 2-cell ship
    while True:
        direction = random.choice(["H", "V"])
        row = random.randint(0, SIZE - 1)
        col = random.randint(0, SIZE - 1)

        if direction == "H":
            if col + 1 >= SIZE:
                continue
            cells = [(row, col), (row, col + 1)]

        else:
            if row + 1 >= SIZE:
                continue
            cells = [(row, col), (row + 1, col)]

        for r, c in cells:
            board[r][c] = "S"

        break

    # Place two 1-cell ships
    placed = 0

    while placed < 2:
        row = random.randint(0, SIZE - 1)
        col = random.randint(0, SIZE - 1)

        if board[row][col] == ".":
            board[row][col] = "S"
            placed += 1

    return board


def create_shot_board():
    """Create a board that stores only shots."""
    return create_board()


def print_board(ships, shots, hide_ships=False):
    print("    1 2 3")

    for row in range(SIZE):
        print(f"{row + 1}   ", end="")

        for col in range(SIZE):

            # Show shots only if there was a shot at this cell
            if shots[row][col] == "X":
                print("X", end=" ")

            elif shots[row][col] == "O":
                print("O", end=" ")

            # Show ships only on the player's own board
            elif ships[row][col] == "S" and not hide_ships:
                print("S", end=" ")

            else:
                print(".", end=" ")

        print()


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
            print("Please enter two numbers, for example: 2 3.")


def all_ships_sunk(ships, shots):
    """Check whether all ship cells have been hit."""

    for row in range(SIZE):
        for col in range(SIZE):

            if ships[row][col] == "S" and shots[row][col] != "X":
                return False

    return True


def take_turn(enemy_ships, enemy_shots, player_number):
    """Player takes shots until they miss."""

    while True:

        row, col = get_shot()

        # Don't allow shooting the same cell twice
        if enemy_shots[row][col] != ".":
            print("You already shot there!")
            continue

        print(
            f"Player {player_number} strikes "
            f"row {row + 1}, column {col + 1}!"
        )

        if enemy_ships[row][col] == "S":

            # The X is stored ONLY in the attacker's shot board.
            enemy_shots[row][col] = "X"

            print("HIT!")

            if all_ships_sunk(enemy_ships, enemy_shots):
                return True

            print("You get another shot!")

        else:

            # The O is also stored ONLY in the attacker's shot board.
            enemy_shots[row][col] = "O"

            print("MISS!")

            return False


def clear_screen():
    print("\n" * 30)


def main():

    # Player 1's ships
    player1_ships = place_ships()

    # Player 2's ships
    player2_ships = place_ships()

    # What Player 1 knows about Player 2's board
    player1_shots = create_shot_board()

    # What Player 2 knows about Player 1's board
    player2_shots = create_shot_board()

    current_player = 1

    print("================================")
    print("        3x3 BATTLESHIPS")
    print("================================")
    print()
    print("Each player has:")
    print("- 1 ship occupying 2 cells")
    print("- 2 ships occupying 1 cell")
    print()
    print("S = Ship")
    print("X = Hit")
    print("O = Miss")
    print()

    input("Press Enter to start...")

    while True:

        clear_screen()

        if current_player == 1:

            print("================================")
            print("          PLAYER 1 TURN")
            print("================================")

            print("\nPLAYER 1 BOARD:")
            print_board(
                player1_ships,
                player2_shots,
                hide_ships=False
            )

            print("\nPLAYER 2 BOARD:")
            print_board(
                player2_ships,
                player1_shots,
                hide_ships=True
            )

            print()
            print("Player 1, make your shot.")

            won = take_turn(
                player2_ships,
                player1_shots,
                1
            )

        else:

            print("================================")
            print("          PLAYER 2 TURN")
            print("================================")

            print("\nPLAYER 2 BOARD:")
            print_board(
                player2_ships,
                player1_shots,
                hide_ships=False
            )

            print("\nPLAYER 1 BOARD:")
            print_board(
                player1_ships,
                player2_shots,
                hide_ships=True
            )

            print()
            print("Player 2, make your shot.")

            won = take_turn(
                player1_ships,
                player2_shots,
                2
            )

        if won:

            clear_screen()

            print("================================")
            print(f"       PLAYER {current_player} WINS!")
            print("================================")
            print()

            print("PLAYER 1 BOARD:")
            print_board(
                player1_ships,
                player2_shots,
                hide_ships=False
            )

            print("\nPLAYER 2 BOARD:")
            print_board(
                player2_ships,
                player1_shots,
                hide_ships=False
            )

            break

        # A miss ends the turn
        current_player = 2 if current_player == 1 else 1

        input("\nPress Enter to pass the turn...")


main()
