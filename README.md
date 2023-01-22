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

When the user clicks on the 'Check' button, a new window is displayed with a message to tell them if their solution to the puzzle is correct, incorrect or incomplete. The user cannot interact with this window; it is just a message window. When the user closes this message window, the game window is displayed again and the game keeps going.

## Test Cases
Here are some example test cases for the Sudoku game.
* Positive and Functional test cases
  - **Insert a value**: Click on a cell and insert a value from 1 to 9. The cell should show the value that the user inserted.
  - **Delete a value**: Click on a filled in cell (not a clue cell) and press the '0' key. The cell should get empty.
  - **Insert a value in a different cell that was previously clicked on**: Click on a cell, click on another different cell and write a value. The latest clicked on cell should show the written value.
  - **Check the correctness of the solution**: Click on the button at any moment of the game and check that the displayed message is correct. (a) 'You have not finished yet!' when the Sudoku puzzle is unfinished. (b) 'Try again!' when the Sudoku puzzle is solved incorrectly. (c) 'It is correct!' when the Sudoku puzzle is solved correctly.
  - **Quit the message window and go back to the game window**: Click on the message window quit button and verify that the window closes correctly and the game window is displayed again looking exactly the same than when you clicked on the 'Check' button.
  - **Quit the game**: Click on the game window quit button and verify that the game finishes correctly.
* Negative test cases
  - **Insert a random character**: Click on a cell and press any key on the keyboard different than numbers from 0 to 9. The cell should stay invariable.
  - **Insert a value outside the grid**: Click on any place outside the grid and press any character on the keyboard. The space of the game window that was clicked on should stay invariable.
  - **Insert a value in a clue cell**: Click on a clue cell and try to insert any character. The clue cell should stay invariable, since its value is a clue for the puzzle.
* Boundary test cases
  - **Insert a 1 or a 9 in a cell**: Click on a cell and insert a 1 or a 9. The cell should show the written value.
* Usability test cases
  - **Try to play a game**: Try to solve the Sudoku puzzle using the given clues. Check if the solution is correct when finish.

## Issues faced
One of the issues that has been faced during the development of this project is trying to display two different windows during same game. The Pygame library does not save the features of a window when a new one is displayed. Thus, a solution has been necessary to allow the user to keep going with their game after checking the correctness of their solution.

The problem has been solved storing the game data in global variables and calling a function that displays a new game window (that looks the same than the original game window) when the quit button is clicked on the message window.

Another issue has been making the button intuitive to the user. To do so, hover effects have been added to the rectangle that represents the button.

The last and greatest challenge has been generating the sudoku puzzle itself. On the one hand, the Sudoku puzzle must be solvable and have a unique solution. Thereby, it is not enough to add random clues to the grid. The approach that has been followed in this project is creating an entire full Sudoku grid and then remove some values from it. On the other hand, the generation of the puzzle must be efficient. In this particular case, a backtracking algorithm has been suitable enough.

## Conclusion
This programming project was a nice hands-on experience to practice with the Python programming lenguage, and to learn some basics of the Pygame library and what it can provide. 
