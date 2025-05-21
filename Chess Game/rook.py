"""
rook.py

Implements the `Rook` class that inherits from `ChessPiece`.
Rook moves horizontally or vertically and supports toroidal wrapping movement.
"""

from chess_piece import ChessPiece

BOARD_SIZE = 8 # Defines BOARD_SIZE = 8 for an 8x8 chessboard.

class Rook(ChessPiece): # Rook extends ChessPiece, so it gets position handling and formatting from the base class.
    """
    Rook chess piece that moves horizontally or vertically.
    """
    def can_capture(self, target: 'ChessPiece') -> bool:
        """
        Returns True if the target (Bishop, in this case) is on the same file or rank.

        The rook can capture any piece on the same file (column) or rank (row).
        """
        return self.file == target.file or self.rank == target.rank

    def move(self, direction: str, steps: int):
        """
        Moves the rook either "up" (increasing rank or advancing upward) or "right" (increasing file or advancing rightward).
        
        Uses modulo (% BOARD_SIZE) for toroidal wrapping—if the rook moves past the edge, 
        it wraps around to the other side of the board.
        """
        if direction == 'up':
            self.rank = (self.rank + steps) % BOARD_SIZE
        elif direction == 'right':
            self.file = (self.file + steps) % BOARD_SIZE
