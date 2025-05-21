"""
bishop.py

Implements the `Bishop` class that inherits from the abstract base class `ChessPiece`.
Bishop can move diagonally in any direction.
"""

from chess_piece import ChessPiece

class Bishop(ChessPiece):
    """
    Bishop chess piece that can move diagonally.
    """
    def can_capture(self, target: 'ChessPiece') -> bool:
        """
        The bishop can capture another piece if it is on the same diagonal. 
        This is determined by checking if the absolute difference 
        between the files and the ranks of the two pieces is the same.


        The expression abs(self.file - target.file) == abs(self.rank - target.rank) 
        checks if two pieces are on the same diagonal on a chessboard.

        1. Files are the columns (a–h), and ranks are the rows (1–8).
        2. A bishop moves diagonally, which means every step it takes changes 
           both its file and rank by the same amount (either both increase or both decrease).
        3. If the difference in files (columns) is equal to the difference in ranks (rows), 
           the two squares are on the same diagonal.

        Example:
        Bishop at c3 (file=2, rank=2)
        Target at f6 (file=5, rank=5)
        abs(2 - 5) == abs(2 - 5) → 3 == 3 → True (same diagonal)
        """
        return abs(self.file - target.file) == abs(self.rank - target.rank)
