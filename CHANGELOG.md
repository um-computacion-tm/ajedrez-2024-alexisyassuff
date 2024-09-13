# Changelog

## [13-08-2024]

### Added

I implemented the Piece and Queen classes with basic methods.
Unit tests have been added to verify the functionality of both classes.

## [14-08-2024]

### Added

The King and Rook classes were implemented, defining their basic attributes and methods.
Unit tests were added to verify the functionality of both classes.

## [15-08-2024]

### Added

I implemented the Bishop and Horse classes, defining their attributes and methods. I also added unit tests.

## [16-08-2024]

### Added

The Pawn class was created, completing the definition of all the pieces with their respective attributes and unit tests.
The file structure was reorganized for optimal clarity and maintainability.

## [17-08-2024]

### Added

I implemented the Board class, which initializes an 8x8 matrix with empty positions.
I added the ability to place pieces on the board using the place_piece method.
I created unit tests to verify the correct initialization of the board and the proper placement of pieces.

## [18-08-2024]

### Added

I implemented move_piece in Board, which allows you to move a piece on the board, including handling piece capture.
I enhanced Pawn functionality by adding movement logic specific to the Pawn piece, including initial double-step and single-step movements.
I created unit tests for Board.move_piece and Pawn, which verify the valid and invalid movements of the Pawn piece on the board.

[19-08-2024]

### Added

I have added new methods to the Board class. These include the ability to print the board, retrieve pieces by position, and convert chess notation to board coordinates.
Unit tests have been created to verify the functionality of these methods.

## [20-08-2024]

### Edited

I implemented the pawn class movement rules, including initial moves, diagonal captures, and restrictions.
These rules are now tested and guaranteed to work correctly.
I refactored the complex functions to make them more efficient based on the proposal from CodeClimate.

## [21-08-2024]

### Edited

I refactored the print_board method of the Board class. I split its logic into three separate methods: mark_superior, mark_inferior, and for_print_board. This improves clarity and maintainability.

## [22-08-2024] and [23-08-2024]

### Edited

I refactored the pawn movement logic and print_board.
I refactored the is_valid_move method. I separated the logic for white and black pawns into distinct methods, enhancing readability and maintainability.
I added helper methods to simplify the pawn movement logic. These include is_initial_move, is_forward_move, is_capture_move, and others.
I fixed the code smells in print_board. I refactored the print_board method to improve code quality and reduce complexity.
I achieved 100% test coverage by adding additional tests in the Piece class to ensure complete test coverage and verify all scenarios.

## [27-08-2024]

### Added

The AjedrezCli class was implemented to facilitate interaction with the chess game.
The Chess class was introduced to manage the game logic, including piece initialization and turn handling.
The initial positions for the white and black pieces on the board were established.
[28-08-2024]

### Added

I have implemented turn-based play. I added functionality to alternate turns between players, validate moves, and update the board state accordingly.

## [29-08-2024]

### Added

I have implemented valid move tests for vertical and horizontal moves.
Invalid move tests included diagonal moves, moves obstructed by other pieces, capturing own pieces, and moves to the same position.

### Edited

The Horse Class has been renamed to Knight Class.

## [30-08-2024]

### Added

The Rook class now has movement functionality.

## [31-08-2024]

### Added

Users can now input moves. User moves in standard chess notation (e.g., "D2" to "D3") are now integrated.
We have implemented basic error handling. We have included error handling for invalid inputs and invalid moves to enhance the user experience.
Print the board state. The current state of the board is now printed after each turn.

### Edited

I refactored the complex functions due to their large size, following the proposal from CodeClimate.

## [01-09-2024]

### Added

I added methods to declare a winner when the opposing player retires.

I edited and refactored the complex functions in the Rook Class.

## [02-09-2024]

### Added

I added movement functionality for the Bishop class.

## [03-09-2024]

### Added

I added movement functionality for the King class.

## [04-09-2024]

### Added

I added unit tests for the functionality in the King and Bishop class.

## [05-09-2024]

### Added

Added movement functionality for the Knight class

### Edited

Fixed attributes to comply with the requirement where class attributes must contain the symbols "\_\_" as prefix and postfix

## [06-09-2024]

### Added

Added missing coverage for the Knight class and unit tests for the Queen class moves

## [07-09-2024]

### Added

I have added movement functionality for the Queen class.

## [08-09-2024]

### Added

I have added functionality to declare victory when one of the players runs out of pieces.

## [09-09-2024]

### Added

I have refactored the function that declares a winner when one of the players runs out of pieces to reduce cognitive complexity.
I have fixed the Queen, Rook, and Bishop code by moving it to the parent Piece class. This eliminates code duplication and ensures that they inherit functionality.

## [10-09-2024]

### Edited

I fixed the feature so that there is no winner if one of the players quits the game. Currently, the game must end in a draw if both players agree. If one player quits, the other must accept it.
We have added child class functions to the Piece class to reuse functions.

## [11-09-2024]

### Edited

Edit the icons of the pieces for a more pleasant and intuitive visual experience.

### Added

Add a function that determines if there is a pawn on the opposite first row.
Add an input function that, if this is true, gives the user options to exchange the pawn for another piece (other than another pawn or a king).
On the board, add a function so that if this is true, the piece on the board is changed
To the Winner_move function that already ended the game if one of the players ran out of pieces, I added an additional function has_king to declare a winner and end the game if any of the players has their king piece captured
Separate the tests so that each piece has its own file independent of the others, achieving easier access to each one and better readability

## [12-09-2024]

### Edited

README.md, with an introduction to the planned project dedicated to the GIT community and a detailed explanation of how Chess should be configured for test mode and for game mode, both deployed with Docker
Fixed pawn movement logic, which incorrectly enabled vertical capture. Now only captures diagonally.
Code refactoring in ChessCli to reduce the logical complexity of the has_king and attempt_move functions
Minor fix in the board code to comply with SOLID principles
Refactored the du functions to make them more efficient based on the proposal from CodeClimate.

### Added

Added DockerFile to be able to deploy applications inside virtual containers

## [13-09-2024]

### Edited

Fixed the last pawn function, which on initial move moved regardless of whether there was a friendly or enemy piece. It now checks that the square is empty.
Fixed duplication issues reported by Code Climate when defining piece colors and icons
Renamed files that were incorrectly named ChessCli.py and Chess.py, which should have been named Cli.py
Initialization of pieces is now the responsibility of the board, which takes responsibility away from the controller and reduces the huge amount of functionality Code Climate reports.
Refactored functions so that the Rook and Queen share functionality and duplication is removed.

### Added

Created the Player class to be responsible for checking if the player still has pieces on the board and if their king is present on the board. This was done because the Chess.py class had more functionality than Code Climate suggested
