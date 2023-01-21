# Sudoku Game - Programming Project

## Introduction
Sudoku is a number puzzle game that is played on a 9x9 grid. The grid is divided into 9 smaller 3x3 grids, called boxes. The objective of the game is to fill in the grid with the numbers 1-9 such that each row, column, and box contains all of the numbers 1-9 without repetition.

The game starts with some of the squares in the grid already filled in. These are called "clues" and are used as a starting point to solve the puzzle. Players must use logical reasoning and deduction to fill in the rest of the grid.

To play, players must first scan the grid for any obvious moves, such as a number that can only go in one specific square. They can then use this information to deduce where other numbers should go. They can also use the process of elimination to determine which numbers can be placed in a particular square.

The game is won when the player has successfully filled in the entire grid without breaking any of the rules.

This project aims to recreate the Sudoku game using Python and the Pygame library.

## Technical Details
The project has been developed using Python 3.10.9 and the Pygame library version 2.1.2. Pygame is a set of Python modules designed for game development and other multimedia applications. In this project particular case, it provides functionality for creating 2D graphics, and handling input events.

The Sudoku puzzle is generated using a backtracking (recursive) algorithm. Firstly, a full 9x9 grid is generated, following the Sudoku game rules. Secondly, some values are removed from the grid, always ensuring that the puzzle has one unique solution. The values that remain in the grid are the clues that the user must use to solve the puzzle. A game window is displayed to show the user the puzzle to solve and allow them to play the game. Finally, when the user wants to check if their solution to the Sudoku puzzle is valid and correct, they can click on the 'Check' button and a window will be displayed to show the correctness judgment. If the user closes this window, they will go back to the game.

## Libraries Used
* Pygame
* Defaultdict (from Collections)
* Randint (from Random)
* Shuffle (from Random)

## Installation and Playing the Game
1. Install Python 3.10
2. Install Pygame
```
pip3 install pygame
```
3. Download the project source code (you can clone this repository)
```
git clone https://github.com/isabelplaza/sudoku-game.git
```
4. Run the file named sudoku.py
```
cd sudoku-game
python3 sudoku.py
```
5. Play the Sudoku game
      1. Click on the cell you want to fill in and press a key on your keyboard
            * Press the number (from 1 to 9) you want to insert in the cell
            * Press the number '0' if you want to delete a value you previously inserted in the cell
      2. Click on the button whenever you want to check if your solution is correct
            * A new window will be displayed to tell you if (a) your solution is incomplete, (b) your solution is incorrect, or (c) your solution is correct
      4. Close this window to go back to the game window
      5. Close the game window whenever you want to quit the game.
  
## User Interface
The User Interface of the game is greatly intuitive. The game window shows the Sudoku grid and a button. The clues in the grid are written in blue Times New Roman. When the user fills in a cell, the value is written in black Comics Sans MS. The button says 'Check' and gets darker when the mouse hovers over it, to show the user that it can be clicked on.

When the user clicks on the 'Check' button, a new window is displayed with a message to tell the user if theis solution to the puzzle is correct, incorrect or incomplete. The user cannot interact with this window, it is just a message window. When the user closes this message window, the game window is displayed again and the game keeps going.
