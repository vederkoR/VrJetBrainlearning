import itertools
import re
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
        self.current_state = ""

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

    def snack_representation(self):
        snake_str = ""
        if len(self.snake) <= 6:
            for i in range(len(self.snake)):
                snake_str += f'{[[int(i), int(j)] for (i, j) in self.snake][i]}'
        else:
            for i in range(3):
                snake_str += f'{[[int(i), int(j)] for (i, j) in self.snake][i]}'
            snake_str += "..."
            for i in range(len(self.snake) - 3, len(self.snake)):
                snake_str += f'{[[int(i), int(j)] for (i, j) in self.snake][i]}'
        return snake_str

    def graph_representation(self):
        print('======================================================================')
        print(f"Stock size: {len(self.stock)}")
        print(f"Computer pieces: {len(self.player_2.domino_pieces)}")
        print()
        print(self.snack_representation())
        print()
        print("Your pieces:")
        for index, value in enumerate(self.player_1.domino_pieces):
            print(f"{index + 1}:{[int(value[0]), int(value[1])]}")
        print()

    def turn(self):
        if self.current_player == self.player_1:
            while True:
                piece_to_take = input()
                template = r"-?" + "[" + "".join(
                    [str(i) for i in range(0, len(self.current_player.domino_pieces) + 1)]) + "]"
                checker = re.fullmatch(template, piece_to_take)
                if checker:
                    break
                else:
                    print("Invalid input. Please try again.")
            if piece_to_take == '0':
                self.player_1.domino_pieces.append(self.stock.pop())
                return
        else:
            pool = [str(i) for i in range(1, len(self.current_player.domino_pieces) + 1)]
            shuffle(pool)
            piece_to_take = pool[0]
        if piece_to_take.startswith("-"):
            self.snake.insert(0, self.current_player.domino_pieces.pop(int(piece_to_take[-1]) - 1))
        else:
            self.snake.insert(len(self.snake), self.current_player.domino_pieces.pop(int(piece_to_take[-1]) - 1))

    def status_check(self):
        if not self.player_1.domino_pieces:
            self.current_state = "Status: The game is over. You won!"
            return True
        elif not self.player_2.domino_pieces:
            self.current_state = "Status: The game is over. The computer won!"
            return True
        elif self.snake[0][0] == self.snake[-1][-1] and list(itertools.chain(*self.snake)).count(self.snake[0][0]) >= 8:
            self.current_state = "Status: The game is over. It's a draw!"
            return True
        elif self.current_player.name == 'computer':
            self.current_state = "Status: Computer is about to make a move. Press Enter to continue..."
            return False
        else:
            self.current_state = "Status: It's your turn to make a move. Enter your command."
            return False


if __name__ == "__main__":
    game = Dominoes()
    game.start()
    while True:

        game.graph_representation()
        a = game.status_check()
        print(game.current_state)
        if a:
            break
        game.turn()
        if game.current_player.name == "computer":
            _ = input()

        game.change_player()
