class Figure:
    def __init__(self, type, colour, position):
        self.type = type
        self.colour = colour
        self.position = position
        self.moved = False
        self.checked = False
        self.moves = {}
        self.legal = {}
    
    def get_moves(self,position,moved):
        moves = {}
        file = position[0]
        rank = int(position[1])
        if type == "pawn":
            if file < ord(68):
                moves.append(ord(file+1),rank)
            if file < ord(67) and moved == False:
                moves.append(ord(file+2),rank)
        if type == "rook":
            for i in range (61,68):
                moves.append(chr(i),rank)
            for i in range (1,8):
                moves.append(file,i)
        if type == "bishop":
        if type == "knight": 
        if type == "queen": 
        if type == "king":
            left=ord(file)-1
            for i in range (3):
                moves.append(left,rank-1+i)
            moves.append(file,rank-1)
            moves.append(file,rank+1)
            right=ord(file)+1
            for i in range (3):
                moves.append(right,rank-1+i)
        moves.pop(position)

    def legalize_moves(self,board):
        #remove ocupied, etc.

def setup_board():
    white_pawns = []
    for i, col in enumerate("abcdefgh"):
        white_pawns.append(Figure("pawn", "white", f"{col}2"))

    white_pieces = {
        "rook1": Figure("rook", "white", "a1"),
        "knight1": Figure("knight", "white", "b1"),
        "bishop1": Figure("bishop", "white", "c1"),
        "queen": Figure("queen", "white", "d1"),
        "king": Figure("king", "white", "e1"),
        "bishop2": Figure("bishop", "white", "f1"),
        "knight2": Figure("knight", "white", "g1"),
        "rook2": Figure("rook", "white", "h1")
    }

    black_pawns = []
    for i, col in enumerate("abcdefgh"):
        black_pawns.append(Figure("pawn", "black", f"{col}7"))

    black_pieces = {
        "rook1": Figure("rook", "black", "a8"),
        "knight1": Figure("knight", "black", "b8"),
        "bishop1": Figure("bishop", "black", "c8"),
        "queen": Figure("queen", "black", "d8"),
        "king": Figure("king", "black", "e8"),
        "bishop2": Figure("bishop", "black", "f8"),
        "knight2": Figure("knight", "black", "g8"),
        "rook2": Figure("rook", "black", "h8")
    }
    return white_pawns + list(white_pieces.values()) + black_pawns + list(black_pieces.values())

if __name__ == "__main__":
    board = setup_board()
