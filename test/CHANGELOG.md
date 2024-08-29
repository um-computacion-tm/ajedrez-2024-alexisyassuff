# Changelog

## [13-08-2024]

### Added

Implemented Piece and Queen classes with basic methods.
Added unit tests to verify functionality for both classes.

## [14-08-2024]

### Added

The King and Rook classes were implemented, defining their basic attributes and methods.
Unit tests were added to verify the functionality of both classes.

## [15-08-2024]

### Added

Implemented classes Bishop and Horse, their attributes and methods, Added Unit tests.

## [16-08-2024]

### Added

With the creation of the Pawn class, the definition of all the pieces with their respective attributes and unit tests was completed.
The file structure was organized for greater clarity and maintainability.

## [17-08-2024]

### Added

Implemented the Board class, initializing an 8x8 matrix with empty positions.
Added functionality to place pieces on the board using the place_piece method.
Created unit tests to verify the correct initialization of the board and the proper placement of pieces.

## [18-08-2024]

### Added

Implemented move_piece in Board: Added the ability to move a piece on the board, including handling piece capture.
Enhanced Pawn functionality: Added movement logic specific to the Pawn piece, including initial double-step and single-step movements.
Created unit tests for Board.move_piece and Pawn: Verified valid and invalid movements of the Pawn piece on the board.

## [19-08-2024]

### Added

Added methods to the Board class for printing the board, retrieving pieces by position, and converting chess notation to board coordinates.
Unit tests were created to verify the functionality of these methods.

## [20-08-2024]

### Edited

Implemented Pawn class movement rules, including initial moves, diagonal captures, and restrictions.
Added tests to ensure that these rules work correctly.
Refactored complex functions due to their large size based on the proposal from CodeClimate.

## [21-08-2024]

### Edited

Refactored the print_board method of the Board class by splitting its logic into three separate methods: mark_superior, mark_inferior, and for_print_board to improve clarity and maintainability.

## [22-08-2024] and [23-08-2024]

### Edited

Refactored Pawn movement logic and print_board.
Refactored is_valid_move method: separated logic for white and black pawns into distinct methods to enhance readability and maintainability.
Added helper methods: introduced methods like is_initial_move, is_forward_move, is_capture_move, and others to simplify the pawn movement logic.
Fixed code smells in print_board: refactored print_board method to improve code quality and reduce complexity.
Achieved 100% test coverage: added additional tests in the Piece class to ensure complete test coverage and verify all scenarios.

## [27-08-2024]

### Added

The AjedrezCli class was implemented: to facilitate interaction with the chess game.
The Chess class was introduced to manage the game logic, including piece initialization and turn handling.
The initial positions for the white and black pieces on the board were established.

## [28-08-2024]

### Added

Turn-based play has been implemented: added functionality to alternate turns between players,
validate moves and update the board state accordingly.

## [29-08-2024]

### Added

Valid move tests were implemented for vertical and horizontal moves.
Invalid move tests included diagonal moves, moves obstructed by other pieces, capturing own pieces, and moves to the same position.

### Edited

Corrected the name of the Horse Class to Knight Class

## [30-08-2024]

### Added

Added movement functionality for the Rook class
