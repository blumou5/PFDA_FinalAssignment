import pygame

# Screen Display

def main():
    pygame.init()
    pygame.display.set_caption("Pomodoro Tomodachi")
    resolution = (600, 600)
    screen = pygame.display.set_mode(resolution)