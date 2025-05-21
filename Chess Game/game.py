"""
game.py

Contains the `ChessGame` class that manages gameplay between a stationary Bishop
and a Rook that moves based on random coin tosses and dice rolls.

 It handles:
    1 - piece placement
    2 - turn-by-turn simulation
    3 - move execution
    4 - capture detection 
    5 - logging
    6 - board visualization
"""

import random
import pandas as pd
from bishop import Bishop
from chess_piece import FILES
from rook import Rook

ROUNDS = 15

class ChessGame:
    """
    Manages the Rook vs Bishop game with simulated movement and capture logic.

    Purpose:
        Orchestrates the Rook vs Bishop game, handling all rules, moves, and display.
    
    Responsibilities: 
        Piece management, round simulation, capture logic, logging, and board printing.
    
    Usage: 
        Used as the main engine for both interactive and automated play in this chess simulation project.
    """
    def __init__(self, bishop_pos: str, rook_pos: str):
        """
        Initializes the game with the starting positions for Bishop and Rook.

        Args:
            bishop_pos (str): Algebraic notation (e.g., "c3")
            rook_pos (str): Algebraic notation (e.g., "h1")
        """
        self.bishop = Bishop(FILES.index(bishop_pos[0]), int(bishop_pos[1]) - 1)
        self.rook = Rook(FILES.index(rook_pos[0]), int(rook_pos[1]) - 1)
        self.logs = []

    def simulate_round(self, round_num: int):
        """
        Simulates one round: toss coin, roll dice, move rook, and check for capture.

        Returns:
            str or None: "Bishop" if bishop captures rook this round, else None.
        """
        coin = random.choice(['heads', 'tails'])
        direction = 'up' if coin == 'heads' else 'right'
        dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
        steps = dice1 + dice2

        self.rook.move(direction, steps)

        self.logs.append({
            "round": round_num,
            "coin": coin,
            "dice": (dice1, dice2),
            "steps": steps,
            "rook_position": self.rook.pos_str()
        })

        print(f"\n🎲 Round {round_num}")
        print(f"Coin Toss: {coin} → Move {direction}")
        print(f"Dice Roll: {dice1} + {dice2} = {steps}")
        print(f"Rook Position: {self.rook.pos_str()}")
        self.print_board()

        if self.bishop.can_capture(self.rook):
            print("\n💥 Bishop captured the Rook!")
            return "Bishop"
        return None

    def play_game(self):
        """
        Runs up to 15 rounds, calling simulate_round each time.
        Stops early if the bishop captures the rook.    

        Returns:
            str: The winner, either "Bishop" or "Rook"
        """
        for round_num in range(1, ROUNDS + 1):
            result = self.simulate_round(round_num)
            if result:
                return result
        return "Rook"

    def get_game_log(self):
        """
        Returns a pandas DataFrame of all rounds played, including 
        coin toss, dice rolls, steps, and rook positions.
        """
        return pd.DataFrame(self.logs)

    def print_board(self, highlight_bishop=False):
        """
        Prints an ASCII representation of the 8x8 chessboard.
        Optionally highlights the bishop’s diagonal threat zones.
        Shows the current positions of the bishop (B) and rook (R).
        """
        # Initializes an 8x8 grid filled with "·" (dot) characters, representing empty squares.
        board = [["·" for _ in range(8)] for _ in range(8)]

        # Retrieves the current file (column) and rank (row) for both the bishop and the rook.
        b_file, b_rank = self.bishop.position()
        r_file, r_rank = self.rook.position()


        '''
        If highlight_bishop is True, this section marks all squares on the bishop’s diagonals with "✱".
        It does this by iterating in all four diagonal directions (dr and dc are either -1 or 1).
        For each direction, it steps outward from the bishop’s position, marking each square until it reaches the edge of the board.
        The expression board[7 - r][c] is used because the board is printed with rank 8 at the top (so row 0 is the bottom of the board).
        '''
        if highlight_bishop:
            for dr in [-1, 1]:
                for dc in [-1, 1]:
                    r, c = b_rank + dr, b_file + dc
                    while 0 <= r < 8 and 0 <= c < 8:
                        board[7 - r][c] = "✱"
                        r += dr
                        c += dc

        # Places the bishop ("B") and rook ("R") on the board, overwriting any diagonal highlights if they overlap.
        board[7 - b_rank][b_file] = "B"
        board[7 - r_rank][r_file] = "R"

        '''
        Prints column labels (a to h) and a horizontal border.
        Iterates through each row, printing the rank number (from 8 down to 1) and the row’s contents.
        Prints a closing border.        
        '''
        print("\n   a b c d e f g h")
        print("  -----------------")
        for i, row in enumerate(board):
            print(f"{8 - i} | {' '.join(row)}")
        print("  -----------------")


