from random import randint 
class SnakesAndLadders:
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
        self.winner = None # can use to determine if game is over
    
    def die_roll(self):
        Continue = input("Press Enter to role dice")
        return randint(1,6)
    
    def move_player(self, player_i):
        print(f"____________________________")
        print(f"Player {player_i + 1} turn! ")
        prev_pos = self.players[player_i]
        new_pos = prev_pos + self.die_roll()
        
        if new_pos >= self.LAST_TILE: # winner! game over
            self.winner = player_i
            new_pos = self.LAST_TILE
        elif new_pos in self.SNAKES:
            new_pos = self.SNAKES[new_pos]
        elif new_pos in self.LADDERS:
            new_pos = self.LADDERS[new_pos]
        
        self.players[player_i] = new_pos
        
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
        pos_and_player_i.sort(reverse=True)
        
        # print players with position
        player_pos_str = ' | '.join([f"({player_i + 1}) {pos}" for pos, player_i in pos_and_player_i])
        print(player_pos_str)

game = SnakesAndLadders(n_players = 2, verbose=True)
print(game.play_game())