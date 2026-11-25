import pygame

# Screen Display

def main():
    pygame.init()
    pygame.display.set_caption("Pomodoro Tomodachi")
    resolution = (400, 500)
    screen = pygame.display.set_mode(resolution)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

if __name__ == "__main__":
    main()
