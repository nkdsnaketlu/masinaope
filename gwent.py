#bot_hand = [1,2,3,4,5]
#game_ended = False

def bot_turn():
    print

class Player:
    def __init__(self, hand, name):
        self.name = name
        self.hand = hand
        self.score = 0
        self.table_score = 0
        self.passed = False

    def draw_card(self):
     self.hand.append(3) #here should be random as well

    def win(self):
        print(self.name, " won!")

    def round_pass(self):
        self.passed = True

    def turn(self):
        if len(self.hand) <= 0:
            self.round_pass()
            return
        
        elif self.passed == True:
            return
        
        print(self.name, ", your cards: \n", self.hand)
        ask_pass = input("would you like to pass? [y/n] ")

        if ask_pass == "y":
            self.round_pass()

        elif ask_pass == "n":
            chosen_card = int(input("choose your card: [value of card] "))

            if chosen_card in self.hand:
                self.table_score += chosen_card
                self.hand.remove(chosen_card)
            else:
                print("no card with this value, try again")
                self.turn()
        else:
            print("wrong input, try again")

player1 = Player([1,2,3,4,5], 'player1')
player2 = Player([1,2,3,4,5], 'player2')

players = [player1, player2]

def game_end():
    if players[1].score > players[0].score:
        players[1].win()
    elif players[0].score > players[1].score:
        players[0].win()
    else:
        print("huh")

def game_start():
    current_player_index = 0
    #game_round = 0

    while players[0].score != 2 or players[1].score != 2:
        while players[0].passed == False or players[1].passed == False:
            current_player = players[current_player_index]
            current_player.turn()
            current_player_index = (current_player_index + 1) % 2 #get next players index

        round_end()

def round_reset():
    players[0].table_score = 0
    players[1].table_score = 0
    players[0].passed = False
    players[1].passed = False
    #players[0].hand.append(4)
    #players[1].hand.append(4)
    
    #game_round += 1


def round_end():
    if players[1].table_score > players[0].table_score:
            players[1].score += 1
    elif players[0].table_score > players[1].table_score:
        players[0].score += 1
    else:
        print("huh")

    round_reset()
 




game_start()
game_end()


