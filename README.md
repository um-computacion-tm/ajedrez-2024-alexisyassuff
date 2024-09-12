# first-circleci-AlexisYassuff

Name: Alexis Yassuff

# CircleCI

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-alexisyassuff/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-alexisyassuff/tree/main)

# Maintainability

[![Maintainability](https://api.codeclimate.com/v1/badges/a7b15afd6baf64d1a8e9/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-alexisyassuff/maintainability)

# Test Coverage

[![Test Coverage](https://api.codeclimate.com/v1/badges/a7b15afd6baf64d1a8e9/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-alexisyassuff/test_coverage)

# Chess Game - Python Project

Welcome to the Chess Game project, built with Python and Docker. This project is a complete implementation of a chess game that allows users to play or run tests to ensure everything works as expected.

Chess is a two-player strategy board game where the objective is to checkmate your opponent's king. The game is played on an 8x8 grid, with each player starting with 16 pieces: one king, one queen, two rooks, two bishops, two knights, and eight pawns. Each piece has unique movement rules:

Pawns move forward one square (two squares on their first move) but capture diagonally.
Rooks move any number of squares horizontally or vertically.
Bishops move diagonally across any number of squares.
Knights move in an "L" shape: two squares in one direction and then one square perpendicular.
Queens combine the movement of rooks and bishops.
Kings move one square in any direction.

## Winning the Game

There are two ways to win:

Capture the king: Once a player’s king is captured, the game ends immediately.
Run out of pieces: If one player runs out of pieces, the opponent wins.
My implementation includes all the pieces and their movement logic, including capturing and promotion mechanics for pawns. The game concludes when one of the victory conditions is met.c.

## How to run the chess game

To build the Docker image, you first need to run the command docker build -t ajedrez-2024 .

1. To perform a test mode run so that you can make sure that all the chess game components are working correctly and verify that the code has been properly tested before deployment, you can run the following command:

docker run -it ajedrez-2024 coverage run -m unittest && coverage xml && coverage report -m
These commands will run all the unit tests using unittest and generate a coverage report to show which parts of the code are covered by the tests.

2. Running in game mode To play chess interactively from the command line, you can use the following commands:

docker run -it ajedrez-2024
This will build the Docker image for the chess game.
It will start the chess game using a terminal-based interface, allowing you to play chess using the deployed CLI.
