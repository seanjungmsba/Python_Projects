"""
main.py

Runs the Rook vs Bishop simulation game in interactive mode.

Each round involves 3 ENTER presses:
  1. Start the round
  2. Flip the coin
  3. Roll the dice
  4. Move the Rook piece

The board highlights the Bishop's diagonal threat zone with asterisks.
"""

import random
import time
from game import ChessGame

def play_interactive(game: ChessGame):
    """
    Interactive mode: user presses ENTER 4 times per round to proceed
    through start, coin toss, dice roll, and move rook piece phases.
    Bishop's threat area is visually highlighted as an asterisk on the board.
    """
    print("\n🔰 Initial Positions")
    print(f"♗ Bishop: {game.bishop.pos_str()}")
    print(f"♜ Rook:   {game.rook.pos_str()}")
    game.print_board(highlight_bishop=True)

    for round_num in range(1, 16):
        input(f"\n🔄 Press ENTER to begin round {round_num}...")

        input("🪙 Press ENTER to flip the coin...")
        time.sleep(1.0)  # Add this line for a short delay
        coin = random.choice(['heads', 'tails'])
        direction = 'up' if coin == 'heads' else 'right'
        print(f"🪙 Coin Toss: {coin} → Move {direction}")

        input("🎲 Press ENTER to roll the dice...")
        time.sleep(1.0)  # Add this line for a short delay
        d1, d2 = random.randint(1, 6), random.randint(1, 6)
        steps = d1 + d2
        print(f"🎲 Dice Roll: {d1} + {d2} = {steps}")

        input(f"🎲 Press ENTER to move the Rook {steps} steps {direction}")
        game.rook.move(direction, steps)

        print(f"📍 Rook Position: {game.rook.pos_str()}")
        game.print_board(highlight_bishop=True)

        if game.bishop.can_capture(game.rook):
            print("\n💥 Bishop captured the Rook! Bishop wins.")
            return

    print("\n✅ Rook survived all 15 rounds! Rook wins.")

def main():
    """Main entry point for the fully interactive Rook vs Bishop game."""
    print("♜ Welcome to Rook vs Bishop ♗")
    print("🧩 Bishop is fixed at c3. Rook starts at h1.")
    print("🎮 You'll press ENTER three times each round to simulate play.\n")

    game = ChessGame("c3", "h1")
    play_interactive(game)

if __name__ == "__main__":
    main()
