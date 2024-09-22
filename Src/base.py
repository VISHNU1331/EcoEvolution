import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ecosystem Evolution Simulator')

# Define colors
GREEN = (0, 255, 0)  # Plant
BLUE = (0, 0, 255)   # Prey
RED = (255, 0, 0)    # Predator
WHITE = (255, 255, 255)  # Background

# Grid settings
rows, cols = 20, 20
cell_size = width // cols

# Entity Classes
class Plant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 5  # Plants have energy that prey can consume

class Prey:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 10  # Prey starts with some energy

class Predator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 15  # Predators start with more energy

# Create random entities in the grid
def create_entities(num_plants, num_prey, num_predators):
    plants = []
    prey = []
    predators = []

    for _ in range(num_plants):
        x = random.randint(0, cols - 1)
        y = random.randint(0, rows - 1)
        plants.append(Plant(x, y))

    for _ in range(num_prey):
        x = random.randint(0, cols - 1)
        y = random.randint(0, rows - 1)
        prey.append(Prey(x, y))

    for _ in range(num_predators):
        x = random.randint(0, cols - 1)
        y = random.randint(0, rows - 1)
        predators.append(Predator(x, y))

    return plants, prey, predators

# Drawing the grid and entities
def draw_grid():
    for x in range(0, width, cell_size):
        for y in range(0, height, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(window, WHITE, rect, 1)

def draw_entities(plants, prey, predators):
    for plant in plants:
        pygame.draw.rect(window, GREEN, (plant.x * cell_size, plant.y * cell_size, cell_size, cell_size))
    
    for p in prey:
        pygame.draw.rect(window, BLUE, (p.x * cell_size, p.y * cell_size, cell_size, cell_size))
    
    for predator in predators:
        pygame.draw.rect(window, RED, (predator.x * cell_size, predator.y * cell_size, cell_size, cell_size))

# Main loop
def main():
    clock = pygame.time.Clock()
    plants, prey, predators = create_entities(20, 10, 5)  # Start with 20 plants, 10 prey, and 5 predators

    running = True
    while running:
        clock.tick(10)  # Frame rate
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background
        window.fill(WHITE)

        # Draw grid and entities
        draw_grid()
        draw_entities(plants, prey, predators)

        # Update display
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
