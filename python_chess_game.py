
class Piece:
    def __init__(self, color,position, has_moved):
        self.color = color
        self.position = position
        self.has_moved = has_moved

    def get_legal_moves(self, board):
        pass


class Pawn(Piece):
    def __init__(self, color,position, has_moved):
        super().__init__(color,position, has_moved)

    def get_legal_moves(self, board):
        pass


class Rook(Piece):
    def __init__(self, color, position, has_moved):
        super().__init__(color, position, has_moved)

    def get_legal_moves(self, board):
        pass


class Knight(Piece):
    def __init__(self, color, position, has_moved):
        super().__init__(color, position, has_moved)

    def get_legal_moves(self, board):
        pass


class Bishop(Piece):
    def __init__(self, color, position, has_moved):
        super().__init__(color, position, has_moved)

    def get_legal_moves(self, board):
        pass


class Queen(Piece):
    def __init__(self, color, position, has_moved):
        super().__init__(color, position, has_moved)

    def get_legal_moves(self, board):
        pass


class King(Piece):
    def __init__(self, color, position, has_moved):
        super().__init__(color, position, has_moved)

    def get_legal_moves(self, board):
        pass
