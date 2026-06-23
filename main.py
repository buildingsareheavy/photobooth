"""
main.py
-------
Entry point for the photobooth application.
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

            # Shutter trigger - spacebar or mouse click.
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                frame = camera.capture(DISPLAY_WIDTH, DISPLAY_HEIGHT)
                path = camera.save_frame(frame)
                print(f"Photo saved: {path}")

            if event.type == pygame.MOUSEBUTTONDOWN:
                frame = camera.capture(DISPLAY_WIDTH, DISPLAY_HEIGHT)
                path = camera.save_frame(frame)
                print(f"Photo saved: {path}")

        frame = camera.get_frame(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        screen.blit(frame, (0, 0))
        pygame.display.flip()
        clock.tick(DISPLAY_FPS)

    camera.release()
    pygame.quit()


if __name__ == "__main__":
    main()