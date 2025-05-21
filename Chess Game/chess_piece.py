"""
chess_piece.py

Defines an abstract base class `ChessPiece` that provides an interface for all chess pieces.
It includes common position logic and enforces a `can_capture` method for subclass implementations.

Benefits: Ensures consistency and code reuse for all chess piece types in this chess simulation.
"""

from abc import ABC, abstractmethod

FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

class ChessPiece(ABC): # Inherits from ABC (Abstract Base Class) and uses the @abstractmethod decorator.
    """
    Abstract base class for all chess pieces.
    Since it's an abstract bass class, it cannot be instantiated directly; 
    only subclasses (like Bishop or Rook) can be created.

    Handles common behavior like position formatting.
    """
    def __init__(self, file: int, rank: int):
        self.file = file # The column index (0–7, corresponding to 'a'–'h').
        self.rank = rank # The row index (0–7, corresponding to 1–8).

    def position(self):
        """Returns the (file, rank) tuple of the piece's position."""
        return self.file, self.rank

    def pos_str(self):
        """Returns the algebraic notation (e.g., 'c3') of the piece's position."""
        return f"{FILES[self.file]}{self.rank + 1}"

    @abstractmethod
    def can_capture(self, target: 'ChessPiece') -> bool:
        """
        This method must be implemented by any subclass such as Rook and Bishop.
        It defines the logic for whether this piece can capture another piece.
        Returns True if this piece can capture the given target.
        """
        pass
