import pygame
import sys

def run_game():
    screen = pygame.display.set_mode((1200,800))


    while True:
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0,0,255))
        pygame.display.flip()

run_game()
