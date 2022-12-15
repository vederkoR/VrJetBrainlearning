from collections import Counter
from enum import Enum


class Game:
    class Figure(Enum):
        O_FIG = [[4, 14, 15, 5]]
        I_FIG = [[4, 14, 24, 34], [3, 4, 5, 6]]
        S_FIG = [[5, 4, 14, 13], [4, 14, 15, 25]]
        Z_FIG = [[4, 5, 15, 16], [5, 15, 14, 24]]
        L_FIG = [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]
        J_FIG = [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]
        T_FIG = [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]

    empty_board = 20 * "- - - - - - - - - -\n"

    def __init__(self, figure, dims):
        self.moves = []
        self.figure = figure
        self.current_figure_dots = figure[0]
        self.dims = dims
        self.empty_board = dims[1] * ("- " * (dims[0] - 1) + "-\n")

    @staticmethod
    def fill_fields(figure_dots, e_board):
        board_to_return = e_board
        for i in figure_dots:
            board_to_return = board_to_return[:i * 2] + '0' + board_to_return[i * 2 + 1:]

        return board_to_return

    @staticmethod
    def side_mover(figure_dots, times, width):
        return [int(dot / width) * width + (dot + times) % width for dot in figure_dots]

    @staticmethod
    def down_mover(figure_dots, times):
        return [dot + 10 * times for dot in figure_dots]

    def current_position_definer(self):
        if max(self.current_figure_dots) >= self.dims[0] * (self.dims[1] - 1):
            return
        if (self.moves[-1] == 'left' and any([True for i in self.current_figure_dots if
                                              i in range(0, self.dims[0] * self.dims[1], self.dims[0])])) or (
                self.moves[-1] == 'right' and any([True for i in self.current_figure_dots if
                                                   i in range(self.dims[0] - 1, self.dims[0] * self.dims[1],
                                                              self.dims[0])])):
            self.moves = self.moves[:-1]
            self.moves.append('down')

        all_moves_dist = Counter(self.moves)
        num_of_rotations = all_moves_dist.get('rotate', 0)
        start_position = self.figure[num_of_rotations % len(self.figure)]
        sided_position = Game.side_mover(start_position,
                                         all_moves_dist.get('right', 0) - all_moves_dist.get('left', 0), self.dims[0])
        leveled_position = Game.down_mover(sided_position, len(self.moves))
        self.current_figure_dots = leveled_position


options = {'O': Game.Figure.O_FIG,
           'I': Game.Figure.I_FIG,
           'S': Game.Figure.S_FIG,
           'Z': Game.Figure.Z_FIG,
           'L': Game.Figure.L_FIG,
           'J': Game.Figure.J_FIG,
           'T': Game.Figure.T_FIG}


def main():
    option = input()
    dimensions = [int(i) for i in input().split()]
    game = Game(options[option].value, dimensions)
    print(game.empty_board)
    print(Game.fill_fields(game.current_figure_dots, game.empty_board))
    while True:
        move = input()
        if move == 'exit':
            exit()
        game.moves.append(move)
        game.current_position_definer()
        print(Game.fill_fields(game.current_figure_dots, game.empty_board))


if __name__ == '__main__':
    main()
