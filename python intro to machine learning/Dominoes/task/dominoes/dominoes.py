from itertools import combinations_with_replacement
from random import shuffle


class Player:
    def __init__(self, name, domino_pieces):
        self.name = name
        self.domino_pieces = domino_pieces


class Dominoes:
    def __init__(self):
        self.species = list(combinations_with_replacement("0123456", 2))
        self.player_1 = None
        self.player_2 = None
        self.stock = None
        self.current_player = None
        self.snake = list()

    def shuffle_species(self):
        shuffle(self.species)
        while not any([(str(i), str(i)) in self.species[0:14] for i in range(6)]):
            shuffle(self.species)

    def distribute_species(self):
        self.player_1 = Player("player", self.species[0:7])
        self.player_2 = Player("computer", self.species[7:14])
        self.stock = self.species[14:]

    def change_player(self):
        self.current_player = self.player_1 if (self.current_player == self.player_2) else self.player_2

    def initiate_current_player(self):
        for i in reversed(range(7)):
            if (str(i), str(i)) in self.player_1.domino_pieces:
                self.current_player = self.player_1
                break
            elif (str(i), str(i)) in self.player_2.domino_pieces:
                self.current_player = self.player_2
                break
        self.current_player.domino_pieces.remove((str(i), str(i)))
        self.snake.append((str(i), str(i)))
        self.change_player()

    def start(self):
        self.shuffle_species()
        self.distribute_species()
        self.initiate_current_player()


if __name__ == "__main__":
    game = Dominoes()
    game.start()
    print('======================================================================')
    print(f"Stock size: {len(game.stock)}")
    print(f"Computer pieces: {len(game.player_2.domino_pieces)}")
    print()
    print(f'{[[int(i), int(j)] for (i, j) in game.snake][0]}')
    print()
    print("Your pieces:")
    for index, value in enumerate(game.player_1.domino_pieces):
        print(f"{index + 1}:{[int(value[0]), int(value[1])]}")
    print()
    if game.current_player.name == 'computer':
        print("Status: Computer is about to make a move. Press Enter to continue...")
    else:
        print("Status: It's your turn to make a move. Enter your command.")

    # # stage 1
    # game = Dominoes()
    # game.start()
    # print(f"Stock pieces: {[[int(i), int(j)] for (i, j) in game.stock]}")
    # print(f"Computer pieces: {[[int(i), int(j)] for (i, j) in game.player_2.domino_pieces]}")
    # print(f"Player pieces: {[[int(i), int(j)] for (i, j) in game.player_1.domino_pieces]}")
    # print(f"Domino snake: {[[int(i), int(j)] for (i, j) in game.snake]}")
    # print(f"Status: {game.current_player.name}")
