import random

SIZE = 3


def create_board():
    return [["." for _ in range(SIZE)] for _ in range(SIZE)]


def place_ships():
    """Create a separate board containing only ships."""
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
    """Board containing only the player's shots."""
    return create_board()


def print_board(ships, shots, hide_ships=False):
    print("    1 2 3")

    for row in range(SIZE):
        print(f"{row + 1}   ", end="")

        for col in range(SIZE):
            # Show shot result first
            if shots[row][col] == "X":
                print("X", end=" ")
            elif shots[row][col] == "O":
                print("O", end=" ")
            # Show ships only on your own board
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


def take_turn(enemy_ships, enemy_shots, player_number):
    """Take shots until the player misses."""

    while True:
        row, col = get_shot()

        # Don't allow shooting the same cell twice
        if enemy_shots[row][col] != ".":
            print("You already shot there!")
            continue

        # Show exactly where the player is striking
        print(
            f"Player {player_number} strikes "
            f"row {row + 1}, column {col + 1}!"
        )

        if enemy_ships[row][col] == "S":
            enemy_shots[row][col] = "X"
            print("HIT!")

            if all_ships_sunk(enemy_ships, enemy_shots):
                return True

            print("You get another shot!")

        else:
            enemy_shots[row][col] = "O"
            print("MISS!")
            return False


def all_ships_sunk(ships, shots):
    """Check whether every ship cell has been hit."""

    for row in range(SIZE):
        for col in range(SIZE):
            if ships[row][col] == "S" and shots[row][col] != "X":
                return False

    return True


def clear_screen():
    print("\n" * 30)


def main():
    # Each player has TWO separate boards:
    #
    # ships = where their ships actually are
    # shots = where they have been shot
    #
    # This prevents the two boards from interfering with each other.

    player1_ships = place_ships()
    player2_ships = place_ships()

    player1_shots = create_shot_board()
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
    print("X = Hit")
    print("O = Miss")
    print("S = Your ship")
    print()

    input("Press Enter to start...")

    while True:
        clear_screen()

        if current_player == 1:
            own_ships = player1_ships
            own_shots = player1_shots

            enemy_ships = player2_ships
            enemy_shots = player1_shots

        else:
            own_ships = player2_ships
            own_shots = player2_shots

            enemy_ships = player1_ships
            enemy_shots = player2_shots

        print("================================")
        print(f"        PLAYER {current_player}")
        print("================================")

        print("\nYOUR BOARD:")
        print_board(own_ships, enemy_shots, hide_ships=False)

        print("\nENEMY BOARD:")
        print_board(enemy_ships, own_shots, hide_ships=True)

        print()
        print(f"Player {current_player}, it's your turn.")

        won = take_turn(enemy_ships, enemy_shots, current_player)

        if won:
            clear_screen()

            print("================================")
            print(f"      PLAYER {current_player} WINS!")
            print("================================")
            print()

            print("Your final board:")
            print_board(own_ships, enemy_shots)

            print("\nEnemy board:")
            print_board(enemy_ships, own_shots)

            break

        # A miss ends the turn
        current_player = 2 if current_player == 1 else 1

        input("\nPress Enter to pass the turn...")


main()