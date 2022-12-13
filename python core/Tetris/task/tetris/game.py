from itertools import cycle


class Game:
    O = [[5, 6, 9, 10]]
    I = [[1, 5, 9, 13], [4, 5, 6, 7]]
    S = [[6, 5, 9, 8], [5, 9, 10, 14]]
    Z = [[4, 5, 9, 10], [2, 5, 6, 9]]
    L = [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [4, 5, 6, 8]]
    J = [[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]]
    T = [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]

    empty_board = 4 * "- - - -\n"

    @staticmethod
    def fill_fields(figure_dots):
        board_to_return = Game.empty_board
        for i in figure_dots:
            board_to_return = board_to_return[:i * 2] + '0' + board_to_return[i * 2 + 1:]

        return board_to_return


options = {'O': Game.O,
           'I': Game.I,
           'S': Game.S,
           'Z': Game.Z,
           'L': Game.L,
           'J': Game.J,
           'T': Game.T}


def main():
    option = input()
    print(Game.empty_board)
    positions = cycle(options[option])

    for _ in range(4):
        print(Game.fill_fields(next(positions)))
    print(Game.fill_fields(options[option][0]))


if __name__ == '__main__':
    main()