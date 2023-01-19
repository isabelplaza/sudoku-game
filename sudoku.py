# SUDOKU GAME

# Set up pygame
import pygame

# Fix the size of the window that will be displayed to play the Sudoku game
WINDOW_SIZE = (550, 550)

# Set up a background color for the window
background_color = (250,250,250) # white-grey
lines_color = (0,0,0) # black
clues_color = (52, 31, 151) # blue


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

# Copy the grid for later comparison
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]


def main():

    # Initialize pygame
    pygame.init()

    # Display the window and fill it with the chosen background color
    window = pygame.display.set_mode(WINDOW_SIZE)
    window.fill(background_color)

    # Add a font for the numbers populating the sudoku grid
    font = pygame.font.SysFont('Times New Roman', 35)

    # Draw the grid (9x9) --> 'for' from 0 to 9.
    for i in range(10):
        if (i % 3 != 0):
            # Draw a black vertical line in the displayed window.
            # Third and fourth parameters are starting and ending coordinates respectively.
            # Fifth parameter is the width of the line
            pygame.draw.line(window, lines_color, (50 + 50*i, 50), (50 + 50*i, 500), 2)

            # Draw a horizontal line with the same format than the vertical one
            pygame.draw.line(window, lines_color, (50, 50 + 50*i), (500, 50 + 50*i), 2)
        # Every 3 lines (i % 3 == 0), the drawn linea should be in bold (width x2)
        # To differenciate the 3x3 grids and make the grid easier for the user (sudoku player)
        else:
            # Lines in bold
            pygame.draw.line(window, lines_color, (50 + 50*i, 50), (50 + 50*i, 500), 4)
            pygame.draw.line(window, lines_color, (50, 50 + 50*i), (500, 50 + 50*i), 4)

    # Update what is being displayed
    pygame.display.update()

    # Populate the displayed grid
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            # Check if the value is valid (between 1 and 9)
            if (1 <= grid[row][column] <= 9):
                # If valid, write the value in the grid
                clue = font.render(str(grid[row][column]), True, clues_color)
                window.blit(clue, ((column+1)*50 + 17, (row+1)*50 + 6))

    # Update what is being displayed
    pygame.display.update()

    # Close the window whenever the user presses Sudoku game window QUIT button
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()
