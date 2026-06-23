"""
Photobooth application entry point.

Initializes pygame, displays the camera feed, and handles photo capture.
"""

import pygame
from camera import DevCamera
from config import DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY_FPS


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Photobooth")

    camera = DevCamera()
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