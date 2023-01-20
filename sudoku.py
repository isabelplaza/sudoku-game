# SUDOKU GAME

# Set up pygame
import pygame
from collections import defaultdict

# Fix the size of the window that will be displayed to play the Sudoku game
WINDOW_SIZE = (550, 650)
CELL_SIZE = 50
OFFSET = 5

# Set up a background color for the window
BACKGROUND_COLOR = (250,250,250) # white-grey
LINES_COLOR = (0,0,0) # black
CLUES_COLOR = (52, 31, 151) # blue
VALUES_COLOR = (0,0,0) # black


# Populated grid (as an example until developing the sudoku generator module)
grid = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]

# Solved grid: to edit to make tests
#grid = [[7, 8, 5, 4, 3, 9, 1, 2, 6],
#        [6, 1, 2, 8, 7, 5, 3, 4, 9],
#        [4, 9, 3, 6, 2, 1, 5, 7, 8],
#        [8, 5, 7, 9, 4, 3, 2, 6, 1],
#        [2, 6, 1, 7, 5, 8, 9, 3, 4],
#        [9, 3, 4, 1, 6, 2, 7, 8, 5],
#        [5, 7, 8, 3, 9, 4, 6, 1, 2],
#        [1, 2, 6, 5, 8, 7, 4, 9, 3],
#        [3, 4, 9, 2, 1, 6, 8, 5, 7]]

# Solved grid: to keep as a reference when editing the solved grid above
#grid = [[7, 8, 5, 4, 3, 9, 1, 2, 6],
#        [6, 1, 2, 8, 7, 5, 3, 4, 9],
#        [4, 9, 3, 6, 2, 1, 5, 7, 8],
#        [8, 5, 7, 9, 4, 3, 2, 6, 1],
#        [2, 6, 1, 7, 5, 8, 9, 3, 4],
#        [9, 3, 4, 1, 6, 2, 7, 8, 5],
#        [5, 7, 8, 3, 9, 4, 6, 1, 2],
#        [1, 2, 6, 5, 8, 7, 4, 9, 3],
#        [3, 4, 9, 2, 1, 6, 8, 5, 7]]

# Copy the grid for later comparison
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]


# Function to insert values in the grid
def insert_value(window, button, position):
    # Y coordinate (position[1]) is the row and X coordinate (position[0]) is the column
    row,column = position[1], position[0]
    # Select a font for the values that the user writes on the grid
    font = pygame.font.SysFont('Comic Sans MS', 32)

    # Infinite loop to to detect user actions (quit the game, write on a cell, click on another cell, click on the button)
    while True:

        for event in pygame.event.get():
            # Quit the game (finish the program) whenever the user presses Sudoku game window QUIT button
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # There are three cases when the user presses a key
            if event.type == pygame.KEYDOWN:
                # (1) The user tries to edit a clue (values written (!= 0) on the original grid)
                # This action is not allowed ('return')
                if (grid_original[row-1][column-1] != 0):
                    return

                # (2) The user wants to clear the cell (erase the written value) they clicked on
                if (event.key == ord('0')):
                    # Store the (0) value in the grid
                    grid[row-1][column-1] = chr(event.key)
                    # Draw a blank cell
                    pygame.draw.rect(window, BACKGROUND_COLOR, (position[0]*CELL_SIZE + OFFSET, position[1]*CELL_SIZE + OFFSET, CELL_SIZE - 2*OFFSET, CELL_SIZE - 2*OFFSET))

                # (3) The user wants to add or edit a value on the grid
                # This action is allowed if the value is valid (between 1 and 9)
                if (ord('1') <= event.key <= ord('9')):
                    # Store the value in the grid
                    grid[row-1][column-1] = chr(event.key)
                    # Store the written value to insert it on the cell
                    value = font.render(str(chr(event.key)), True, VALUES_COLOR)
                    # Draw a blank cell
                    pygame.draw.rect(window, BACKGROUND_COLOR, (position[0]*CELL_SIZE + OFFSET, position[1]*CELL_SIZE + OFFSET, CELL_SIZE - 2*OFFSET, CELL_SIZE - 2*OFFSET))
                    # Write the value on the cell
                    window.blit(value, (position[0]*CELL_SIZE + 16, position[1]*CELL_SIZE+2))

                # Update what is being displayed
                pygame.display.update()
                return

            # The user could click on another cell or on the button before writing a value
            # The mouse position should be updated
            #(and either the function to insert a value or the button's function (check_corretness) should be called again)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                position = pygame.mouse.get_pos()
                # If the mouse position is in the button's area, the user clicked on the button
                if button.collidepoint(position):
                    # Call the button's function to check the correctness of the user's puzzle solution
                    check_corretness()
                    return
                # If the mouse position is anywhere else, call insert_value again
                else:
                    # Devide the mouse position by the cell size to get the cell position
                    insert_value(window, button, (position[0]//CELL_SIZE, position[1]//CELL_SIZE))
                    return


# Function to check if the user's solution for the sudoku puzzle is correct
# A sudoku solution is valid if it follows the following three rules:
# (1) Each row must contain the digits from 1-9 without repetition.
# (2) Each column must contain the digits from 1-9 without repetition.
# (3) Each of the 9 (3x3) sub-boxes of the grid must contain the digits from 1-9 without repetition.
def check_corretness():
    # Call the function that performs the algorithm to check the correctness
    message_code = _check_correctness()

    # The function returns a message code depending on the correctness of the solution:
    # (1) The solution is incomplete
    # (2) The solution is incorrect
    # (3) The solution is correct
    # Depending on this message code, the program displays the corresponding message
    if message_code == 1:
        print('You have not finished yet!')
    elif message_code == 2:
        print('Try again!')
    elif message_code == 3:
        print('It is correct!')


# Function that performs the algorithm to check if the user's puzzle solution is correct
def _check_correctness():
    # Create dictionaries to store the values in each row, column and block (3x3 grid)
    row_values = defaultdict(set)
    column_values = defaultdict(set)
    block_values = defaultdict(set)

    # Initialize the message code to correct solution ('3')
    message_code = 3

    # Check every cell on the grid
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            # If the cell is empty (value = 0), the puzzle is incomplete (message_code = 1)
            if grid[row][column] == 0:
                message_code = 1
                return message_code
            # If the value in the cell has already appear for its row, column or block, the puzzle is incorrect (message_code = 2)
            elif grid[row][column] in row_values[row] or grid[row][column] in column_values[column] or grid[row][column] in block_values[(row//3,column//3)]:
                message_code = 2
                return message_code
            # Add every value to each dictionary
            block_values[(row//3,column//3)].add(grid[row][column])
            row_values[row].add(grid[row][column])
            column_values[column].add(grid[row][column])

    # If all the values are correct, then the puzzle is correct (message_code = 3)
    return message_code


# Main function
def main():

    # Initialize pygame
    pygame.init()

    # Display the window (with 'Sudoku Game' caption) and fill it with the chosen background color
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Sudoku Game")
    window.fill(BACKGROUND_COLOR)

    # Add a font for the numbers populating the sudoku grid (and for the text of the button)
    font = pygame.font.SysFont('Times New Roman', 35)

    # Draw the grid (9x9) --> 'for' from 0 to 9.
    for i in range(10):
        if (i % 3 != 0):
            # Draw a black vertical line in the displayed window.
            # Third and fourth parameters are starting and ending coordinates respectively.
            # Fifth parameter is the width of the line
            pygame.draw.line(window, LINES_COLOR, (CELL_SIZE + CELL_SIZE*i, CELL_SIZE), (CELL_SIZE + CELL_SIZE*i, 10*CELL_SIZE), 2)

            # Draw a horizontal line with the same format than the vertical one
            pygame.draw.line(window, LINES_COLOR, (CELL_SIZE, CELL_SIZE + CELL_SIZE*i), (10*CELL_SIZE, CELL_SIZE + CELL_SIZE*i), 2)
        # Every 3 lines (i % 3 == 0), the drawn lines should be in bold (width x2)
        # To differenciate the 3x3 grids and make the grid easier for the user (sudoku player)
        else:
            # Lines in bold
            pygame.draw.line(window, LINES_COLOR, (CELL_SIZE + CELL_SIZE*i, CELL_SIZE), (CELL_SIZE + CELL_SIZE*i, 10*CELL_SIZE), 4)
            pygame.draw.line(window, LINES_COLOR, (CELL_SIZE, CELL_SIZE + CELL_SIZE*i), (10*CELL_SIZE, CELL_SIZE + CELL_SIZE*i), 4)

    # Populate the displayed grid
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            # Check if the value is valid (between 1 and 9)
            if (1 <= grid[row][column] <= 9):
                # If valid, write the value on the grid
                clue = font.render(str(grid[row][column]), True, CLUES_COLOR)
                window.blit(clue, ((column+1)*CELL_SIZE + 17, (row+1)*CELL_SIZE + 6))

    # Set up features of a button (the button will allow the user to check the correctness of their solution)
    color_button = (0,177,26) # green
    color_hover_button = (1,142,21) # darker green
    color_text_button = (255,255,255) #white
    button_size = (WINDOW_SIZE[0]//3, WINDOW_SIZE[1]//10)
    button_position = (WINDOW_SIZE[0]//3, 5*WINDOW_SIZE[1]//6)
    text_button = font.render('Check', True, color_text_button) # the text on the button will be 'Check'

    # Create the button that allows the user to check the correctness of their solution
    button = pygame.Rect(button_position[0], button_position[1], button_size[0], button_size[1])
    pygame.draw.rect(window, color_button, button)
    window.blit(text_button, (button.x + 9*OFFSET, button.y + 2*OFFSET))

    # Update what is being displayed
    pygame.display.update()

    # Infinite loop to detect user actions (click on a cell, click on the button, quit the game)
    while True:
        for event in pygame.event.get():
            # Get the mouse position when the user clicks on a cell (left click is button == 1)
            # And call either the insert_value function to insert the written value in the grid
            # Or the check_corretness function to check if the user's puzzle solution is correct
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                position = pygame.mouse.get_pos()
                # If the mouse position is in the button's area, the user clicked on the button
                if button.collidepoint(position):
                    # Call the button's function to check the correctness of the user's puzzle solution
                    check_corretness()
                # If the mouse position is anywhere else, call insert_value again
                else:
                    # Devide the mouse position by the cell size to get the cell position
                    insert_value(window, button, (position[0]//CELL_SIZE, position[1]//CELL_SIZE))

            # Quit the game (finish the program) whenever the user presses Sudoku game window QUIT button
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Change the color of the button when mouse hovers over it
        position = pygame.mouse.get_pos()
        # If the mouse position is in the button's area, draw the button in a darker color (color_hover_button)
        if button.x <= position[0] <= button.x + button_size[0] and button.y <= position[1] <= button.y + button_size[1]:
            pygame.draw.rect(window, color_hover_button, button)
        # If the mouse is anywhere else, keep the usual color (color_button)
        else:
            pygame.draw.rect(window, color_button, button)

        # Write the text on the button ('Check')
        window.blit(text_button, (button.x + 9*OFFSET, button.y + 2*OFFSET))

        # Update what is being displayed
        pygame.display.update()


main()
