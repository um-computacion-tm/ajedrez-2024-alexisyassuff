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

### Added

Pawn class movement rules have been implemented, including initial moves, diagonal captures, and restrictions.
Tests have been added to ensure that these rules work correctly
All this, considering the refactoring proposed by CodeClimate when dealing with complex functions due to their large size

## [21-08-2024]

### Added

Due to CodeClimate's proposal, the print_board method of the Board class has been refactored by splitting its logic into three separate methods: mark_superior, mark_inferior and for_print_board, which improves the clarity and maintainability of the code.

## [22-08-2024] and [23-08-2024]

### Added

Refactor Pawn Movement Logic and Print Board
Refactored is_valid_move method: Separated logic for white and black pawns into distinct methods to enhance readability and maintainability.
Added helper methods: Introduced methods like is_initial_move, is_forward_move, is_capture_move, and others to simplify the pawn movement logic.
Fixed code smells in print_board: Refactored print_board method to improve code quality and reduce complexity.
Achieved 100% test coverage: Added additional tests in the Piece class to ensure complete test coverage and verify all scenarios.

## [27-08-2024]

### Added

The AjedrezCli class was implemented: to facilitate interaction with the chess game.
The Chess class was introduced to manage the game logic, including piece initialization and turn handling.
The initial positions for the white and black pieces on the board were established.
