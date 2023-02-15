from random import randint
from collections import deque
import random

class Queue: #this will handle the queueing of the rock and paper scissor cards that the players will use to access the ladder#
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self)>0:
            yield self.dequeue()
    
    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()    

class Bubblesort():
    def bubbleSort(self,numbers):
        itemCount = len(numbers)
        for index in range(itemCount-1):
            for value in range(itemCount-1):
                if numbers[value] < numbers[value+1]:
                    temp = numbers[value], numbers[value+1]
                    numbers[value+1], numbers[value] = temp

class RockPaperScissor:
    def __init__(self):
        self.card = ["rock","paper","scissor"]
        self.usershuffling = True
        self.user_card_queue = []
        self.computer_card_list = []
        self.score = 0
        self.card_fifo_queue = Queue()

    def counter(self,counter):
        self.counter = counter

    def user_card_q_algorithm(self):
        while self.counter >= 1:
            card = random.choice(self.card)
            self.card_fifo_queue.enqueue(card)
            self.counter -= 1
        print(f"Number of cards in possession: {len(self.card_fifo_queue)}")

    def user_3card_attack(self):
        for item in range(3):
            card_ = self.card_fifo_queue.dequeue()
            self.user_card_queue.append(card_)      

    def user_shuffle(self):
        print(f"Your deck: {self.user_card_queue}")
        while self.usershuffling == True:
            user_choice = input("Enter 's' to shuffle or 'f' to proceed to the fight: ")
            print("\n")
            if user_choice.upper() == "S":
                random.shuffle(self.user_card_queue)
                print(f"Your shuffled deck: {self.user_card_queue}")
                continue
            elif user_choice.upper() == "F":
                self.usershuffling = False
   
    def computer_3card_defend(self):
        for item in range(3):
            card_ = random.choice(self.card)
            self.computer_card_list.append(card_)

    def determine_winner(self):
        for item_ in range(len(self.user_card_queue)):
            if self.user_card_queue[item_] == self.computer_card_list[item_]:
                print(f"Both players selected {self.user_card_queue[item_]}. It's a tie!")
            elif self.user_card_queue[item_] == self.card[0]:
                if self.computer_card_list[item_] == self.card[2]:
                    print("Rock smashes Scissors! you win!")
                    self.score += 1
                else:
                    print("Paper covers Rock! you lose")
                    self.score -= 1
            elif self.user_card_queue[item_] == self.card[1]:
                if self.computer_card_list[item_] == self.card[0]:
                    print("Paper covers Rock! you win!")
                    self.score += 1
                else: 
                    print("Scissor cuts Paper! you lose")
                    self.score -= 1
            elif self.user_card_queue[item_] == self.card[2]:
                if self.computer_card_list[item_] == self.card[1]:
                    print("Scissor cuts Paper! you win!")
                    self.score += 1
                else: 
                    print("Rock smashes Scissors! you lose")     
                    self.score -= 1       
        if self.score == 0:
            print("\nIts a tie overall")
        elif self.score > 0:
            print("\nIts your victory overall!")
        elif self.score < 0:
            print("\nIts your defeat overall")
                    
    def get_score(self):
        return self.score
    
    def warning_message(self):
        print("You lack the necessary numbers of card to fight")

    def start_fight(self):
        if len(self.card_fifo_queue) >= 3 :
            self.user_3card_attack()
            self.user_shuffle()
            self.computer_3card_defend()
            self.determine_winner()
            return True
        else:
            self.warning_message()
            return False   

class SnakesAndLadders: #handles the algorithm for the Snakes and ladder game#
    SNAKES = {
        27: 8,
        34: 7,
        29: 3,
        69: 31,
        72: 36,
        77: 46,
        80: 41,
        96: 48,
        98: 79,
    }

    LADDERS = {
        4: 16,
        6: 25,
        12: 49,
        20: 40,
        38: 88,
        58: 62,
        71: 93,
        78: 84,
        86: 95,
    }
    bitten_by_snake=[
        "Aw you got bit by a snake",
        "sheeeeeeeeeesh~ that looks painful",
        "Better be careful next time",
        "oh noooooo!",
        "daaaaaamn, it must have hurt",
        "OMG!"
    ]

    defeated_by_guardian=[
        "Better luck next time",
        "Defeat never comes to any man until he admits it. -Joseph Daniels",
        "We learn little from victory, much from defeat. -Japanese proverb",
        "He who fears being conquered is sure of defeat. -Napoleon Bonaparte",
        "Believe you can and your're halfway there. -Theodore Roosevelt",
        "Victory is sweetest when you've known defeat. -Malcolm Forbes",
    ]

    defended_against_snake=[
        "Yesss!",
        "woooow",
        "let's gooooooooo!!!",
        "That was a close call",
        "That was scary, HAHAHA!",
        "Nailed it, nice try snake",
    ]

    victory_over_guardian = [
        "That was a good match",
        "Nice one",
        "LET'S GOOOOOOOOOOO! FOR THE TOP",
        "WOP! WOP!",
        "WEEEEEEEEE!",
        "Incredible WIN!"
    ]


    LAST_TILE = 100
    
    def __init__(self, n_players, verbose = False):
        self.n_players = n_players
        self.verbose = verbose
        self.players = [0] * n_players
        self.turn = 0
        self.counter = [0] * n_players
        self.winner = None # can use to determine if game is over
    
    def die_roll(self):
        Continue_ = input("Press Enter to role dice: ")
        return randint(1,6)
    
    def move_player(self, player_i):
        print(f"\n\n\n\nPlayer {player_i + 1} turn! ")
        print(f"____________________________")
        prev_pos = self.players[player_i]
        die_roll_result = self.die_roll()
        print(f"You get a {die_roll_result}!")
        new_pos = prev_pos + die_roll_result


        old_counter = self.counter[player_i]
        new_counter = old_counter + 1
        self.counter[player_i] = new_counter
        gameRPS = RockPaperScissor()
        gameRPS.counter(self.counter[player_i])
        gameRPS.user_card_q_algorithm()
        if new_pos >= self.LAST_TILE: # winner! game over
            self.winner = player_i
            new_pos = self.LAST_TILE
        print(f"Player {player_i + 1} landed on tile {new_pos} ")
        if new_pos in self.SNAKES:
            user_input = input("Enter 'y' to fight the attacking snake or 'n'/any key to disregard: ")  
            if user_input.upper() == "Y":
                if gameRPS.start_fight() == True:
                    self.counter[player_i] -= 3
                    if gameRPS.get_score() > 0:
                        new_pos = new_pos
                        print(f"{self.defended_against_snake[randint(0,5)]}")
                        print(f"Player {player_i + 1} will stay on tile {new_pos} ")
                    else:
                        new_pos = self.SNAKES[new_pos]
                        print(f"{self.bitten_by_snake[randint(0,5)]}")
                        print(f"Player {player_i + 1} landed on tile {new_pos} ")
            elif (user_input.upper()) == "N" or (user_input.upper() != "Y"):
                    new_pos = self.SNAKES[new_pos]
                    print(f"{self.bitten_by_snake[randint(0,5)]}")
                    print(f"Player {player_i + 1} landed on tile {new_pos} ")
        elif new_pos in self.LADDERS:
            user_input = input("\nEnter 'y' to fight for the access on the ladder or 'n'/any key to disregard: ")
            if user_input.upper() == "Y":
                if gameRPS.start_fight() == True:
                    self.counter[player_i] -= 3
                    if gameRPS.get_score() > 0:
                        new_pos = self.LADDERS[new_pos]
                        print(f"{self.victory_over_guardian[randint(0,5)]}")
                        print(f"Player {player_i + 1} landed on tile {new_pos} ")
                    else:
                        new_pos = new_pos
                        print(f"{self.defeated_by_guardian[randint(0,5)]}")
                        print(f"Player {player_i + 1} will stay on tile {new_pos} ")                        
            elif (user_input.upper() == "N") or (user_input.upper() != "Y"):
                    new_pos = new_pos
                    print(f"Player {player_i + 1} will stay on tile {new_pos} ")       
        self.players[player_i] = new_pos

        
    def move_players(self):
        for player_i in range(self.n_players):
            self.move_player(player_i)
            if self.winner is not None: # done with game
                break
                
    def play_game(self):
        condition = True
        while condition is True:
            while self.winner is None:
                self.turn += 1
                self.move_players()
                if self.verbose:
                    self.print_turn()
            return f"Player #{self.winner + 1} Wins!"
            
    
    def print_turn(self):
        print(f"\n\nThats the end of Turn {self.turn}:")
        print("-------------------------------------------------------------")        
        
        # sort players by position
        pos_and_player_i = [(pos, player_i) for player_i, pos in enumerate(self.players)]
        sorter=Bubblesort()
        sorter.bubbleSort(pos_and_player_i)        
        
        # print players with position
        player_pos_str = ' | '.join([f"(P#{player_i + 1}) in tile {pos}" for pos, player_i in pos_and_player_i])
        print(f"Turn {self.turn} placement rankings: {player_pos_str}")

class GAMEmsg:
 
    def intro(self):
        intro_msg = """
        Welcome to my Text Based Snake and ladder game with rock, paper and scissors twist
        Modified by: Christian Kevin P. De Vega

        Goal of the game:
            Be the first player to reach the final tile or the 100th tile.

        Rules and Mechanics:
            1. Roll the dice to advance from your initial position. You can move from 1-6 tile in each turn depending from the dice roll.
            2. Every turn each player will gain one rock/paper/scissor card that they can use on the snake or ladder tile.
            3. If you land on a ladder tile you can choose to fight the ladder guardian for access on the ladder or you can ignore it.
            4. If you land on a snake tile you can choose to defend yourself from the snake or let it slide you down.
            5. Each fight will require a player to deduc 3 cards from his inventory.
            6. In a match the player and the ladder guardian or snake will engage in a 3 rounds rock, paper, and scissor game.
            7. Each turn a placement board will be shown to indicate the players position in the race.
        """
        print(intro_msg)

    def options(self):
        option_="""
        Options:
        Press [0]play or [1]Exit """
        choice_= int(input(f"{option_}"))
        if choice_ == 0:
            return True
        if choice_ == 1:
            return False


    def player_amount(self):
        condition = True
        num_player = """
        How many players will participate? """
        while condition == True:
            num_Player = int(input(f"{num_player}"))
            if num_Player != 0 and num_Player > 0:
                condition = False
                print(f"""
                \n\nWelcome to the {num_Player} players that will participate in this game! """)
                return num_Player

    def INTRO(self):
        self.intro()
        condition = True
        while condition == True:
            if self.options() == True:
                n_players = self.player_amount()
                gameSNL = SnakesAndLadders(n_players, verbose=True)
                print(gameSNL.play_game())
            else:
                condition = False
            


def gamestarter():    
        gamemsg = GAMEmsg()
        gamemsg.INTRO()

if __name__ == '__main__':
    gamestarter()