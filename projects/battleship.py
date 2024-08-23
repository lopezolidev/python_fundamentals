class Player:
    def __init__(self, id):
        self.id = id
        self.battleships = []
        self.field = []

    def fill_field(self):
        self.field = [['.' for _ in range(10)] for _ in range(10)]
    
    def print_field(self):
        for i in range(10):
            print(self.field[i])
        print('\n')

    def attack(self, enemy_player):
        while True:
            coord_x = int(input("Select row for attack: "))
            coord_y = int(input("Select column for attack: "))
            if coord_x not in range(10) or coord_y not in range(10):
                print("Insert valid coordinates for X and Y")
            else:
                break
        
        pair = (coord_x, coord_y)

        for ship in enemy_player.battleships:
            if (ship.suffer_damage(pair, enemy_player)):
                print(f"Player {self.id} hit {ship.name} in coordinates ({pair})")
                enemy_player.print_field()
                return
        print("Water!")
        return

    def check_dead_ships(self):
        return all(ship.life_points == 0 for ship in self.battleships)
    # method to check if all of my ships are destroyed, if so the other player wins 

    def place_ships(self):
        for ship in self.battleships:
            ship.place_ship(self.field)

    def set_battleships(self):
        i = 0
        while i < 3:
            type = input("Select type of ship: \n - (A) Battleship\n - (D) Destroyer\n - (S) Submarine\n")
            ship = Ship(type)
            ship.set_coordinates_for_ship(self.battleships)
            ship.place_ship(self.field)
            self.battleships.append(ship)
            i += 1

    def set_up_game(self):
        self.fill_field()
        self.set_battleships()
        self.place_ships()
        self.print_field()
# player class 

class Ship:
    def __init__(self, type):
        self.type = type
        self.destroyed = False
        self.coordinates = []
        if self.type == 'A':
            self.life_points = 4
            self.name = "Battleship"
        if self.type == 'D':
            self.life_points = 3
            self.name = "Destroyer"
        if self.type == 'S':
            self.life_points = 2
            self.name = "Submarine"

    def suffer_damage(self, pair, owner_player):
        if pair in self.coordinates:
            self.life_points -= 1
            self.coordinates.remove(pair)
            owner_player.field[pair[0]][pair[1]] = 'X'

            if self.life_points == 0:
                owner_player.battleships.remove(self)     
                print(f"{self.name} was destroyed!")

            return True
        return False
    
    def place_ship(self, player_board):
        for pair in self.coordinates:
            player_board[pair[0]][pair[1]] = self.type

    def set_coordinates_for_ship(self, player_list_of_ships):
        while True:
            coord_x = int(input("Please insert coordinate X in a range from 0 - 9: "))
            coord_y = int(input("Please insert coordinate Y in a range from 0 - 9: "))
            if coord_x in range(10) and coord_y in range(10):
                pair = (coord_x, coord_y)
                if pair not in self.coordinates and all(pair not in ship.coordinates for ship in player_list_of_ships):
                    self.coordinates.append(pair)
                    if len(self.coordinates) == self.life_points:
                        break
                else:
                    print("The coordinates cannot repeat, please choose a different pair")
            else:
                print("Please insert a pair between 0 and 9")

class Game:
    def __init__(self):
        pass

    def game_start(self):
        print("Welcome to Battleship game!")
        id = int(input("Select your player ID: "))
        if id == 1:
            player_1 = Player(id)
            player_2 = Player(2)
        elif id == 2:
            player_2 = Player(id)
            player_1 = Player(1)

        print("Set up your game, Player 1: \n")
        player_1.set_up_game()

        print("Set up your game, Player 2: \n")
        player_2.set_up_game()

        while True:
            if not player_1.check_dead_ships():
                print("Attack turn for player 1\n")
                player_1.attack(player_2)
            else: 
                break
            if not player_2.check_dead_ships():
                print("Attack turn for player 2\n")
                player_2.attack(player_1)
            else:
                break


        if player_1.check_dead_ships():
            print("Player 2 wins the game!\n")
            return
        if player_2.check_dead_ships():
            print("Player 1 wins the game!\n")
            return

game = Game()
game.game_start()