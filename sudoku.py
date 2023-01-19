# SUDOKU GAME

# Set up pygame
import pygame

# Fix the size of the window that will be displayed to play the Sudoku game
WINDOW_SIZE = (550, 550)

# Set up a background color for the window
background_color = (250,250,250) # white-grey
lines_color = (0,0,0) # black

def main():

    # Initialize pygame
    pygame.init()

    # Display the window and fill it with the chosen background color
    window = pygame.display.set_mode(WINDOW_SIZE)
    window.fill(background_color)

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

    # Close the window whenever the user presses Sudoku game window QUIT button
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()
