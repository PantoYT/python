class Figure:
    def __init__(self, type, colour, position):
        self.type = type
        self.colour = colour
        self.position = position
        self.moved = False
        self.checked = False
        self.legal = {}

class Board:
    def __init__(self):
        self.squares = {
            f"{col}{row}": None
            for col in "abcdefgh"
            for row in range(1, 9)
        }

class MoveCalculator:
    
    @staticmethod
    def calculate(figure, squares):
        match figure.type:
            case "rook":   return MoveCalculator._rook(figure, squares)
            case "bishop": return MoveCalculator._bishop(figure, squares)
            case "queen":  return MoveCalculator._queen(figure, squares)
            case "knight": return MoveCalculator._knight(figure, squares)
            case "king":   return MoveCalculator._king(figure, squares)
            case "pawn":   return MoveCalculator._pawn(figure, squares)
            case _:        return []

    @staticmethod
    def _slide(figure, squares, directions):
        """Wspólna logika dla wieży, gońca, hetmana."""
        moves = []
        c = ord(figure.position[0]) - ord('a')
        r = int(figure.position[1]) - 1

        for dc, dr in directions:
            nc, nr = c + dc, r + dr
            while 0 <= nc <= 7 and 0 <= nr <= 7:
                pos = f"{chr(ord('a') + nc)}{nr + 1}"
                target = squares[pos]
                if target is None:
                    moves.append(pos)
                elif target.colour != figure.colour:
                    moves.append(pos)
                    break
                else:
                    break
                nc += dc
                nr += dr
        return moves

    @staticmethod
    def _rook(figure, squares):
        return MoveCalculator._slide(figure, squares, [(0,1),(0,-1),(1,0),(-1,0)])
    

    @staticmethod
    def _bishop(figure, squares):
        return MoveCalculator._slide(figure, squares, [(1,1),(1,-1),(-1,1),(-1,-1)])
    

    @staticmethod
    def _queen(figure, squares):
        return MoveCalculator._slide(figure, squares, [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)])
    
    @staticmethod
    def _knight(figure, squares):
        moves = []
        c = ord(figure.position[0]) - ord('a')
        r = int(figure.position[1]) - 1

        offsets = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

        for dc, dr in offsets:
            nc, nr = c + dc, r + dr
            if 0 <= nc <= 7 and 0 <= nr <= 7:
                pos = f"{chr(ord('a') + nc)}{nr + 1}"
                target = squares[pos]
                if target is None or target.colour != figure.colour:
                    moves.append(pos)

        return moves

    @staticmethod
    def _king(figure, squares):
        moves = []
        c = ord(figure.position[0]) - ord('a')
        r = int(figure.position[1]) - 1

        for dc in [-1, 0, 1]:
            for dr in [-1, 0, 1]:
                if dc == 0 and dr == 0:
                    continue
                nc, nr = c + dc, r + dr
                if 0 <= nc <= 7 and 0 <= nr <= 7:
                    pos = f"{chr(ord('a') + nc)}{nr + 1}"
                    target = squares[pos]
                    if target is None or target.colour != figure.colour:
                        moves.append(pos)

        return moves

    @staticmethod
    def _pawn(figure, squares):
        moves = []
        c = ord(figure.position[0]) - ord('a')
        r = int(figure.position[1]) - 1
        direction = 1 if figure.colour == "white" else -1

        nr = r + direction
        if 0 <= nr <= 7:
            pos = f"{figure.position[0]}{nr + 1}"
            if squares[pos] is None:
                moves.append(pos)

                start_row = 1 if figure.colour == "white" else 6
                if r == start_row:
                    nr2 = r + 2 * direction
                    pos2 = f"{figure.position[0]}{nr2 + 1}"
                    if squares[pos2] is None:
                        moves.append(pos2)

        for dc in [-1, 1]:
            nc, nr = c + dc, r + direction
            if 0 <= nc <= 7 and 0 <= nr <= 7:
                pos = f"{chr(ord('a') + nc)}{nr + 1}"
                target = squares[pos]
                if target is not None and target.colour != figure.colour:
                    moves.append(pos)

        return moves