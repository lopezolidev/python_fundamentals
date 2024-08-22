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

# player_1 = Player(1)
# player_1.fill_field()
# player_1.print_field()

