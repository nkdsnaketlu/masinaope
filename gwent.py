#edited with AI
class Player:

    def __init__(self, hand, name):
        self.name = name
        self.hand = hand
        self.score = 0
        self.table_score = 0
        self.passed = False

    def win(self):
        print(self.name, "won!")

    def round_pass(self):
        self.passed = True

    def turn(self):
        if len(self.hand) <= 0:
            self.round_pass()
            return

        if self.passed == True:
            return

        print(self.name, ", your cards:")
        print(self.hand)

        ask_pass = input("Would you like to pass? [y/n] ")

        if ask_pass == "y":
            self.round_pass()

        elif ask_pass == "n":
            chosen_card = int(input("Choose your card: [value of card] "))

            if chosen_card in self.hand:
                self.table_score += chosen_card
                self.hand.remove(chosen_card)
            else:
                print("No card with this value, try again")
                self.turn()

        else:
            print("Wrong input, try again")
            self.turn()


player1 = Player([], "player1")
player2 = Player([], "player2")

players = [player1, player2]


def game_start():

    # Number of the current round
    game_round = 1

    # Starting cards
    players[0].hand = [1, 2, 3, 4, 5]
    players[1].hand = [1, 2, 3, 4, 5]

    current_player_index = 0

    while game_round <= 3:

        print("\n====================")
        print("ROUND", game_round)
        print("====================")

        # One round
        while players[0].passed == False or players[1].passed == False:

            current_player = players[current_player_index]

            current_player.turn()

            current_player_index = (current_player_index + 1) % 2

        round_end()

        # Stop the game if somebody has already won 2 rounds
        if players[0].score >= 2 or players[1].score >= 2:
            break

        game_round += 1


def round_end():

    print("\nRound ended!")
    print("Player 1:", players[0].table_score)
    print("Player 2:", players[1].table_score)

    # Player 1 wins
    if players[0].table_score > players[1].table_score:

        players[0].score += 1
        print("Player 1 won the round!")

        round_reset(winner=players[0])

    # Player 2 wins
    elif players[1].table_score > players[0].table_score:

        players[1].score += 1
        print("Player 2 won the round!")

        round_reset(winner=players[1])

    # Draw
    else:

        players[0].score += 1
        players[1].score += 1

        print("Draw!")

        round_reset(winner=None)


def round_reset(winner):

    # Reset table scores
    players[0].table_score = 0
    players[1].table_score = 0

    # Reset passed state
    players[0].passed = False
    players[1].passed = False

    # Give one basic card to each player
    players[0].hand.append(1)
    players[1].hand.append(1)

    # Winner gets one additional card
    if winner is not None:
        winner.hand.append(1)


def game_end():

    print("\n====================")
    print("GAME ENDED")
    print("====================")

    print("Player 1 score:", players[0].score)
    print("Player 2 score:", players[1].score)

    if players[0].score > players[1].score:
        players[0].win()

    elif players[1].score > players[0].score:
        players[1].win()

    else:
        print("The game is a draw!")


game_start()
game_end()