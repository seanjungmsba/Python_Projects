# Rook vs Bishop Chess Simulation

This project simulates a chess scenario where a stationary Bishop tries to capture a Rook that moves according to random coin tosses and dice rolls. The simulation is structured around several core classes, each with a clear responsibility and interface.

---

## Class Overview

### 1. `ChessPiece` (Abstract Base Class)
- **Purpose:**  
  Provides a common interface and shared logic for all chess pieces.  
  Handles position storage, algebraic notation conversion, and enforces a `can_capture` method for subclasses.
- **Design Rationale:**  
  Using an abstract base class ensures all chess pieces implement their own capture logic, promoting code reuse and consistency.
- **Tradeoffs:**  
  - **Pros:** Enforces a uniform interface, reduces code duplication.
  - **Cons:** Slightly more complex for beginners; requires understanding of inheritance and abstract methods.

---

### 2. `Bishop`
- **Purpose:**  
  Represents a Bishop chess piece. Implements diagonal movement and capture logic.
- **Design Rationale:**  
  Inherits from `ChessPiece` and implements `can_capture` to check for diagonal alignment using the mathematical property:  
  `abs(self.file - target.file) == abs(self.rank - target.rank)`
- **Tradeoffs:**  
  - **Pros:** Simple, efficient diagonal check; leverages base class for position handling.
  - **Cons:** Only models capturing, not full movement or color restrictions (e.g., only one color square).

---

### 3. `Rook`
- **Purpose:**  
  Represents a Rook chess piece. Implements horizontal (rightward)/vertical (upward) movement, capture logic, and toroidal (wrapping) movement.
- **Design Rationale:**  
  Inherits from `ChessPiece`. The `move` method uses modulo arithmetic to wrap around the board edges, making the simulation more interesting and less predictable.
- **Tradeoffs:**  
  - **Pros:** Simple movement logic; toroidal wrapping prevents the rook from getting "stuck" at the board edge.
  - **Cons:** Toroidal movement is not standard chess; chosen for simulation variety and challenge.

---

### 4. `ChessGame`
- **Purpose:**  
  Manages the overall game state, including piece placement, turn simulation, move execution, capture detection, logging, and board visualization.
- **Design Rationale:**  
  Encapsulates all game logic, making it easy to run interactive or automated simulations. Uses composition to manage pieces and logs rounds for analysis.
- **Tradeoffs:**  
  - **Pros:** Centralizes game logic; easy to extend or modify rules; supports both interactive and automated play.
  - **Cons:** Slightly monolithic; could be further split for larger projects (e.g., separate board and logger classes).

---

## Design Considerations

- **Object-Oriented Design:**  
  Classes are used to encapsulate state and behavior, making the code modular and extensible.
- **Abstraction and Inheritance:**  
  The abstract base class (`ChessPiece`) ensures all pieces share a common interface, while subclasses implement specific logic.
- **Simplicity vs. Realism:**  
  Some rules (like toroidal rook movement) are not standard chess but are chosen to make the simulation more engaging and to avoid edge-case handling.
- **Extensibility:**  
  The design allows for easy addition of new piece types or game rules by subclassing `ChessPiece` and extending `ChessGame`.

---

## Summary

This chess game implementation balances clarity, modularity, and simulation fun. The use of abstract base classes and inheritance promotes code reuse and consistency, while the toroidal movement and simple capture logic keep the simulation engaging and easy to understand. Tradeoffs were made to favor educational value and extensibility over strict adherence to chess rules.