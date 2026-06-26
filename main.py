"""
Photobooth application entry point.

Initializes pygame, displays the camera feed, and handles photo capture.

State machine:
    IDLE       — showing live camera feed, waiting for trigger
    COUNTDOWN  — showing live feed with countdown overlay
    CAPTURED   — photo taken, brief pause before returning to IDLE
"""

import pygame
from enum import Enum, auto
from camera import DevCamera
from config import (
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    DISPLAY_FPS,
    COUNTDOWN_FROM,
    COUNTDOWN_HOLD_SECS,
    FONT_SIZE,
    COUNTDOWN_CAPTURE_WAIT
)
from ui import draw_countdown


class State(Enum):
    """
    Possible states the photobooth can be in.

    Similar to a union type in TypeScript:
        type State = "IDLE" | "COUNTDOWN" | "CAPTURED"
    """
    IDLE      = auto()
    COUNTDOWN = auto()
    CAPTURED  = auto()


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Photobooth")

    camera: DevCamera = DevCamera()
    font = pygame.font.SysFont(None, FONT_SIZE, bold=True)
    clock = pygame.time.Clock()

    state = State.IDLE

    # Tracks when the current countdown number started showing (ms)
    countdown_number_start: int = 0
    # Which number we're currently showing (3, 2, 1)
    countdown_current: int = COUNTDOWN_FROM

    running = True
    while running:
        now: int = pygame.time.get_ticks()  # milliseconds since pygame.init()

        clock.tick(DISPLAY_FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Only accept trigger in IDLE state — ignore clicks during countdown
            if state == State.IDLE:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    state = State.COUNTDOWN
                    countdown_current = COUNTDOWN_FROM
                    countdown_number_start = now

                if event.type == pygame.MOUSEBUTTONDOWN:
                    state = State.COUNTDOWN
                    countdown_current = COUNTDOWN_FROM
                    countdown_number_start = now

        # State: IDLE
        if state == State.IDLE:
            frame = camera.get_frame(DISPLAY_WIDTH, DISPLAY_HEIGHT)
            screen.blit(frame, (0, 0))
            pygame.display.flip()

        # State: COUNTDOWN
        elif state == State.COUNTDOWN:
            elapsed_ms: int = now - countdown_number_start
            hold_ms: int = int(COUNTDOWN_HOLD_SECS * 1000)

            # Advance to next number if enough time has passed
            if elapsed_ms >= hold_ms:
                countdown_current -= 1
                countdown_number_start = now

                # Countdown finished — take the photo
                if countdown_current < 1:
                    frame = camera.get_frame(DISPLAY_WIDTH, DISPLAY_HEIGHT)
                    path = camera.save_frame(frame)  # type: ignore[attr-defined]
                    print(f"Photo saved: {path}")
                    state = State.CAPTURED

            # Still counting — draw the current number over the live feed
            if state == State.COUNTDOWN:
                frame = camera.get_frame(DISPLAY_WIDTH, DISPLAY_HEIGHT)
                draw_countdown(screen, frame, countdown_current, font)

        # State: CAPTURED
        elif state == State.CAPTURED:
            # Brief pause so the user knows the photo was taken,
            # then loop back to idle
            pygame.time.wait(COUNTDOWN_CAPTURE_WAIT)
            state = State.IDLE

    camera.release()
    pygame.quit()


if __name__ == "__main__":
    main()