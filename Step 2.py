import random
import pygame
import time
from pygame.locals import *

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Constants
CELL_SIZE = 20
GRID_WIDTH = 800
GRID_HEIGHT = 400
ROWS = GRID_HEIGHT // CELL_SIZE
COLS = GRID_WIDTH // CELL_SIZE

def create_grid():
    return [[random.randint(0, 1) for _ in range(COLS)] for _ in range(ROWS)]

def count_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < ROWS and 0 <= y + j < COLS and grid[x + i][y + j]:
                count += 1
    return count

def update_grid(grid):
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    for x in range(ROWS):
        for y in range(COLS):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y]:
                if neighbors == 2 or neighbors == 3:
                    new_grid[x][y] = 1
            else:
                if neighbors == 3:
                    new_grid[x][y] = 1
    return new_grid

def draw_grid(screen, grid):
    for x in range(0, GRID_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, GRID_HEIGHT))
    for y in range(0, GRID_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (GRID_WIDTH, y))

    for x in range(ROWS):
        for y in range(COLS):
            if grid[x][y]:
                pygame.draw.rect(screen, WHITE, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")

    grid = create_grid()
    paused = True
    generation = 0

    clock = pygame.time.Clock()

    # Define buttons
    start_button = pygame.Rect(50, GRID_HEIGHT + 20, 100, 40)
    stop_button = pygame.Rect(200, GRID_HEIGHT + 20, 100, 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if event.key == pygame.K_q:
                    pygame.quit()
                    return
            if event.type == MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    paused = False
                if stop_button.collidepoint(event.pos):
                    paused = True

        if not paused:
            grid = update_grid(grid)
            generation += 1

        screen.fill(BLACK)
        draw_grid(screen, grid)

        # Draw buttons
        pygame.draw.rect(screen, (0, 128, 0), start_button)
        pygame.draw.rect(screen, (255, 0, 0), stop_button)

        font = pygame.font.Font(None, 36)

        # Display generation
        generation_text = font.render(f"Generation: {generation}", True, WHITE)
        generation_bg = pygame.Surface((generation_text.get_width(), generation_text.get_height()))
        generation_bg.fill(BLACK)
        screen.blit(generation_bg, (10, 10))
        screen.blit(generation_text, (10, 10))

        # Count alive cells
        alive_cells = sum(sum(row) for row in grid)
        cells_text = font.render(f"Cells: {alive_cells}", True, WHITE)
        cells_bg = pygame.Surface((cells_text.get_width(), cells_text.get_height()))
        cells_bg.fill(BLACK)
        screen.blit(cells_bg, (GRID_WIDTH - cells_text.get_width() - 10, 10))
        screen.blit(cells_text, (GRID_WIDTH - cells_text.get_width() - 10, 10))

        pygame.display.flip()

        clock.tick(10)

if __name__ == "__main__":
    main()
