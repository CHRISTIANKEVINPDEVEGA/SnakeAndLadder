from random import randint
from collections import deque
import random
import sys, time, os

def type_wr(letter):#function for the delay in text 

    for text in letter:
        sys.stdout.write(text)
        sys.stdout.flush()
        time.sleep(0.02)



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



class Bubblesort():# function for sorting the placement in every turn

    def bubbleSort(self,numbers):
        itemCount = len(numbers)
        for index in range(itemCount-1):
            for value in range(itemCount-1):
                if numbers[value] < numbers[value+1]:
                    temp = numbers[value], numbers[value+1]
                    numbers[value+1], numbers[value] = temp

card_fifo_queue = Queue() #queue init

class RockPaperScissor:

    def __init__(self):
        self.card = ["rock","paper","scissor"]
        self.usershuffling = True
        self.user_card_queue = []
        self.computer_card_list = []
        self.score = 0
        self.card_fifo_queue = card_fifo_queue


    def counter(self,counter):# def for the counter of card/per turn base on the queue
        self.counter = counter

    def COUNTER(self,COUNTER):# def for the counter of the card/per turn but based on the list
        self.COUNTER = COUNTER

    def user_card_q_algorithm(self):# def for the enqueuein of cards in the queue class
        while self.counter >= 1:
            card = random.choice(self.card)
            self.card_fifo_queue.enqueue(card)
            self.counter -= 1

        


    def user_3card_attack(self):# def for the dequeueing 3cards at a time from class into an empty list
        for item in range(3):
            card_ = self.card_fifo_queue.dequeue()
            self.user_card_queue.append(card_)      


    def user_shuffle(self):
        type_wr(f"\nYour deck: {self.user_card_queue}")#def for shuffling the cards of 3

        while self.usershuffling == True:
            type_wr("\nEnter 's' to shuffle or 'f' to proceed to the fight: ")
            user_choice = input()
            print("\n")
            if user_choice.upper() == "S":
                random.shuffle(self.user_card_queue)
                type_wr(f"\nYour shuffled deck: {self.user_card_queue}")
                continue
            elif user_choice.upper() == "F":
                self.usershuffling = False


    def computer_3card_defend(self):#def for the cards the computer will use against the players
        for item in range(3):
            card_ = random.choice(self.card)
            self.computer_card_list.append(card_)


    def victor_conditions(self): #def for the conditions in winning the rock, paper and scissor(RPS) game
        for item_ in range(len(self.user_card_queue)):
            if self.user_card_queue[item_] == self.computer_card_list[item_]:
                type_wr(f"\nBoth participants selected {self.user_card_queue[item_]}. \033[93;1;4mIt's a tie!\033[0m")
            elif self.user_card_queue[item_] == self.card[0]:
                if self.computer_card_list[item_] == self.card[2]:
                    type_wr("\nYour Rock smashes the \033[31;1mOpponents\033[0m Scissors! \033[92;1;4mYou win\033[0m!")
                    self.score += 1
                else:
                    type_wr("\n\033[31;1mOpponents\033[0m Paper covers Your Rock! \033[31;1;4mYou lose\033[0m.")
                    self.score -= 1
            elif self.user_card_queue[item_] == self.card[1]:
                if self.computer_card_list[item_] == self.card[0]:
                    type_wr("\nYour Paper covers the \033[31;1mOpponents\033[0m Rock! \033[92;1;4mYou win\033[0m!")
                    self.score += 1
                else: 
                    type_wr("\n\033[31;1mOpponents\033[0m Scissor cuts Your Paper! \033[31;1;4mYou lose\033[0m.")
                    self.score -= 1
            elif self.user_card_queue[item_] == self.card[2]:
                if self.computer_card_list[item_] == self.card[1]:
                    type_wr("\nYour Scissor cuts the \033[31;1mOpponents\033[0m Paper! \033[92;1;4mYou win\033[0m!")
                    self.score += 1
                else: 
                    type_wr("\n\033[31;1mOpponents\033[0m Rock smashes Your Scissors! \033[31;1;4mYou lose\033[0m.")     
                    self.score -= 1    

        if self.score == 0: #coring system for the overall match of 3 rounds of RPS game
            type_wr("\n\n\n\033[93;1;4mIts a tie overall\033[0m")
        elif self.score > 0:
            type_wr("\n\n\n\033[92;1;4mIts your victory overall!\033[0m")
        elif self.score < 0:
            type_wr("\n\n\n\033[31;1;4mIts your defeat overall\033[0m")


    def get_score(self):# def for the score int value
        return self.score
    

    def warning_message(self): #def for the warning when a player initiate a fight without enough card
        type_wr("You lack the necessary numbers of card to fight.")


    def start_fight(self): #def for starting the whole class
        if self.COUNTER >= 3 :
            self.user_3card_attack()
            self.user_shuffle()
            self.computer_3card_defend()
            self.victor_conditions()
            return True
        else:
            self.warning_message()
            return False   



class SnakesAndLadders: #handles the algorithm for the Snakes and ladder game#
 
    SNAKES_tiles = {
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


    LADDERS_tiles = {
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


    FINAL_TILE = 100
    

    def __init__(self, num_players, verbose = False):
        self.num_players = num_players
        self.verbose = verbose
        self.players = [0] * num_players
        self.n_turn = 0
        self.counter = [0] * num_players
        self.counterRSP= [0] * num_players
        self.winner = None # can use to determine if game is over
    

    def die_roller(self):
        type_wr("Press Enter to role dice: ")
        Continue_ = input()
        return randint(1,6)
    

    def move_a_player(self, player_i): #def for the movement of one player
        type_wr(f"\n\n\n\n\033[96;1;4mPlayer {player_i + 1}\033[0m turn! ")
        print(f"\n____________________________")
        old_counter = self.counter[player_i]
        new_counter = old_counter + 1
        self.counter[player_i] = new_counter
        self.counterRSP[player_i] = new_counter - (new_counter-1)

        type_wr(f"Number of cards in possession: \033[93;1m{self.counter[player_i]}\033[0m\n")

        initial_pos = self.players[player_i]
        die_roll_result = self.die_roller()

        type_wr(f"\nRolling............................")
        type_wr(f"\nYou get a \033[93;1m{die_roll_result}\033[0m!")

        updated_pos = initial_pos + die_roll_result

        gameRPS = RockPaperScissor()#condition for the RPS mechanic to start
        gameRPS.COUNTER(self.counter[player_i])
        gameRPS.counter(self.counterRSP[player_i])
        gameRPS.user_card_q_algorithm()

        if updated_pos >= self.FINAL_TILE: # winner! game over
            self.winner = player_i
            updated_pos = self.FINAL_TILE
        type_wr(f"\n\033[96;1;4mPlayer {player_i + 1}\033[0m landed on \033[97;1;4mtile {updated_pos}\033[0m ")

        if updated_pos in self.SNAKES_tiles:
            type_wr(f"\n\n\033[96;1;4mPlayer {player_i + 1}\033[0m encounters an \033[31;1magrresive snake\033[0m....")
            type_wr("\n\nEnter '\033[94;1my\033[0m' to fight the attacking snake or '\033[34;1mn\033[0m'/any key to disregard: ")
            user_input = input()  
            if user_input.upper() == "Y":
                if gameRPS.start_fight() == True:
                    self.counter[player_i] -= 3
                    if gameRPS.get_score() > 0:
                        updated_pos = updated_pos
                        type_wr(f"\n{self.defended_against_snake[randint(0,5)]}")
                        type_wr(f"\n\n\033[96;1;4mPlayer {player_i + 1}\033[0m will stay on \033[97;1;4mtile {updated_pos}\033[0m. ")
                    else:
                        updated_pos = self.SNAKES_tiles[updated_pos]
                        type_wr(f"\n{self.bitten_by_snake[randint(0,5)]}")
                        type_wr(f"\n\n\033[96;1;4mPlayer {player_i + 1}\033[0m landed on \033[97;1;4mtile {updated_pos}\033[0m. ")
            elif (user_input.upper()) == "N" or (user_input.upper() != "Y"):
                    updated_pos = self.SNAKES_tiles[updated_pos]
                    type_wr(f"\n{self.bitten_by_snake[randint(0,5)]}")
                    type_wr(f"\n\n\033[96;1;4mPlayer {player_i + 1}\033[0m landed on \033[97;1;4mtile {updated_pos}\033[0m. ")

        elif updated_pos in self.LADDERS_tiles:
            type_wr(f"\n\n\033[96;1;4mPlayer {player_i + 1}\033[0m encounters a \033[32;1mladder guardian\033[0m....")
            type_wr("\n\nEnter '\033[94;1my\033[0m' to fight for the access on the ladder or '\033[34;1mn\033[0m'/any key to disregard: ")
            user_input = input()
            if user_input.upper() == "Y":
                if gameRPS.start_fight() == True:
                    self.counter[player_i] -= 3
                    if gameRPS.get_score() > 0:
                        updated_pos = self.LADDERS_tiles[updated_pos]
                        type_wr(f"\n{self.victory_over_guardian[randint(0,5)]}")
                        type_wr(f"\n\n\033[96;1;4mPlayer {player_i + 1}\033[0m landed on \033[97;1;4mtile {updated_pos}\033[0m. ")
                    else:
                        updated_pos = updated_pos
                        type_wr(f"\n{self.defeated_by_guardian[randint(0,5)]}")
                        type_wr(f"\n\n\033[96;1;4mPlayer {player_i + 1}\033[0m will stay on \033[97;1;4mtile {updated_pos}\033[0m. ")                        
            elif (user_input.upper() == "N") or (user_input.upper() != "Y"):
                    updated_pos = updated_pos
                    type_wr(f"\n\n\033[96;1;4mPlayer {player_i + 1}\033[0m will stay on \033[97;1;4mtile {updated_pos}\033[0m. ")    

        self.players[player_i] = updated_pos

        
    def move_all_players(self):#def for the movement of all players
        for player_i in range(self.num_players):
            self.move_a_player(player_i)
            if self.winner is not None: # done with game
                break


    def play_SNL_game(self):# def for the SNL game as the starter
        while self.winner is None:
            self.n_turn += 1
            self.move_all_players()
            if self.verbose:
                self.print_turn()
        return f"\n\n\033[93;1m=====Congratulations Player #{self.winner + 1} you Win! And that concludes this epic Snake and Ladder match.=====\033[93;1m"
       
    
    def print_turn(self): # for the announcement every turn
        type_wr(f"\n\n\033[95;1mThats the end of Turn {self.n_turn}:\033[0m")
        print("\n-------------------------------------------------------------")   

        # sort players by position
        position_and_player_index = [(pos, player_i) for player_i, pos in enumerate(self.players)]
        sorter=Bubblesort()
        sorter.bubbleSort(position_and_player_index) 

        # print players with position
        player_position_string = ' | '.join([f"(Player {player_i + 1}) in \033[97;1;4mtile {pos}\033[0m" for pos, player_i in position_and_player_index])
        type_wr(f"\033[95;1;4mTurn {self.n_turn} placement rankings:\033[0m {player_position_string}")



class GAMEholder: #STARTS the whole game including the intro and options
 
    def intro(self):
        intro_msg = """
        \033[96;1;4mWelcome to my Text Based Snake and ladder game with rock, paper and scissors twist\033[0m
        \033[96;1;4mModified by: Christian Kevin P. De Vega\033[0m

         \033[93;1;4mGoal of the game:\033[0m
             \033[93;1mBe the first player to reach the final tile or the 100th tile.\033[0m

        \033[92;1;4mRules and Mechanics:\033[0m
            \033[32;1m1. Roll the dice to advance from your initial position. You can move from 1-6 tile in each turn depending from the dice roll.\033[0m
            \033[32;1m2. Every turn each player will gain one rock/paper/scissor card that they can use on the snake or ladder tile.\033[0m
            \033[32;1m3. If you land on a ladder tile you can choose to fight the ladder guardian for access on the ladder or you can ignore it.\033[0m
            \033[32;1m4. If you land on a snake tile you can choose to defend yourself from the snake or let it slide you down.\033[0m
            \033[32;1m5. Each fight will require a player to deduc 3 cards from his inventory.\033[0m
            \033[32;1m6. In a match the player and the ladder guardian or snake will engage in a 3 rounds rock, paper, and scissor game.\033[0m
            \033[32;1m7. Each turn a placement board will be shown to indicate the players position in the race.\033[0m
        """
        type_wr(intro_msg)

        

    def options(self):
        option_="""
        \033[93;1;4mOptions:\033[0m
        Press [0]play or [1]Exit: """

        type_wr(option_)
        choice_= int(input())
        if choice_ == 0:
            return True
        elif choice_ == 1:
            return False


    def player_amount(self):
        condition = True

        num_player = """
        \033[32;1mHow many\033[0m \033[96;1mplayers\033[0m \033[32;1mwill participate?\033[0m """

        while condition == True:
            type_wr(num_player)
            num_Player = int(input())
            if num_Player != 0 and num_Player > 0:
                condition = False
                type_wr(f"""
                \n\n\n\n\n\n    \033[93;1mWelcome to the\033[0m \033[96;1m{num_Player} player/s\033[0m \033[93;1mthat will participate in this game!\033[0m """)
                return num_Player


    def IntroCompiler(self): # def for starting the SNL and its arguements 
        self.intro()
        condition = True

        while condition == True:
            if self.options() == True:
                num_players = self.player_amount()
                gameSNL = SnakesAndLadders(num_players, verbose=True)
                print(gameSNL.play_SNL_game())
                type_wr(f"\n\n\n\n\n---- Enter \033[93;1;4m'0'\033[0m in the options to play another session of Snake and Ladder.Thank You For Playing! ----\n\n\n")
            else:
                condition = False
            


def gamestarter():    
        gameholder = GAMEholder()
        gameholder.IntroCompiler()

if __name__ == '__main__':
    gamestarter()