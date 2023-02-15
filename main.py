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
        print(len(self.card_fifo_queue))

    def user_3card_attack(self):
        for item in range(3):
            card_ = self.card_fifo_queue.dequeue()
            self.user_card_queue.append(card_)      

    def user_shuffle(self):
        print(self.user_card_queue)
        while self.usershuffling == True:
            user_choice = input("press 's' to shuffle and 'f' to continue the fight: ")
            if user_choice.upper() == "S":
                random.shuffle(self.user_card_queue)
                print(self.user_card_queue)
                continue
            elif user_choice.upper() == "F":
                self.usershuffling = False
   
    def computer_3card_defend(self):
        for item in range(3):
            card_ = random.choice(self.card)
            self.computer_card_list.append(card_)
        print(self.computer_card_list)

    def determine_winner(self):
        for item_ in range(len(self.user_card_queue)):
            if self.user_card_queue[item_] == self.computer_card_list[item_]:
                print(f"both players selected {self.user_card_queue[item_]}. It's a ties!")
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
            print("its a tie overall")
        elif self.score > 0:
            print("its your victory overall")
        elif self.score < 0:
            print("its your defeat overall")
                    
    def get_score(self):
        return self.score
    
    def warning_message(self):
        print("not enough cards to fight")

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
    
    LAST_TILE = 100
    
    def __init__(self, n_players, verbose = False):
        self.n_players = n_players
        self.verbose = verbose
        self.players = [0] * n_players
        self.turn = 0
        self.counter = [0] * n_players
        self.winner = None # can use to determine if game is over
    
    def die_roll(self):
        Continue = input("Press Enter to role dice")
        return randint(1,6)
    
    def move_player(self, player_i):
        print(f"____________________________")
        print(f"Player {player_i + 1} turn! ")
        prev_pos = self.players[player_i]
        new_pos = prev_pos + self.die_roll()

        old_counter = self.counter[player_i]
        new_counter = old_counter + 1
        self.counter[player_i] = new_counter
        gameSL = RockPaperScissor()
        gameSL.counter(self.counter[player_i])
        gameSL.user_card_q_algorithm()

        if new_pos >= self.LAST_TILE: # winner! game over
            self.winner = player_i
            new_pos = self.LAST_TILE
        elif new_pos in self.SNAKES:
            user_input = input("Press y/n to fight the attacking snake: ")  
            if user_input.upper() == "Y":
                if gameSL.start_fight() == True:
                    self.counter[player_i] -= 3
                if gameSL.get_score() > 0:
                    new_pos = new_pos
                else:
                    new_pos = self.SNAKES[new_pos]
            elif user_input.upper() == "N":
                    new_pos = self.SNAKES[new_pos]
        elif new_pos in self.LADDERS:
            user_input = input("Press y/n to fight for the access on the ladder: ")
            if user_input.upper() == "Y":
                if gameSL.start_fight() == True:
                    self.counter[player_i] -= 3
                if gameSL.get_score() > 0:
                    new_pos = self.LADDERS[new_pos]
                else:
                    new_pos = new_pos                        
            elif user_input.upper() == "N":
                    new_pos = new_pos       
        self.players[player_i] = new_pos
        print(f"Player {player_i + 1} landed on tile {new_pos} ")
        
    def move_players(self):
        for player_i in range(self.n_players):
            self.move_player(player_i)
            if self.winner is not None: # done with game
                break
                
    def play_game(self):
        while self.winner is None:
            self.turn += 1
            self.move_players()
            if self.verbose:
                self.print_turn()
        return f"Player #{self.winner + 1} Wins!"
    
    def print_turn(self):
        print(f"Turn {self.turn}:")
        
        # sort players by position
        pos_and_player_i = [(pos, player_i) for player_i, pos in enumerate(self.players)]
        sorter=Bubblesort()
        sorter.bubbleSort(pos_and_player_i)        
        
        # print players with position
        player_pos_str = ' | '.join([f"({player_i + 1}) {pos}" for pos, player_i in pos_and_player_i])
        print(player_pos_str)

game = SnakesAndLadders(n_players = 2, verbose=True)
print(game.play_game())