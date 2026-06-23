"""
main.py
-------
Entry point for the application.
Run this file to start the photobooth.
"""

import pygame
from camera import MockCamera
from config import DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY_FPS


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Photobooth")

    camera = MockCamera()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        frame = camera.get_frame(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        screen.blit(frame, (0, 0))
        pygame.display.flip()
        clock.tick(DISPLAY_FPS)

    camera.release()
    pygame.quit()


if __name__ == "__main__":
    main()