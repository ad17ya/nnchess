import chess
import chess.pgn

class State(object):
    def __init__(self):
        self.board = chess.Board()

    def serialize(self):
        #257 bits according to https://chessprogramming.wikispaces.com/Bitboard+Data+Structures
        pass

    def edges(self):
        return list(self.board.legal_moves)

    def value(self):
        # TODO: add neural network here
        return 0


if __name__ == '__main__':
    s = State()
    print(s.edges())
