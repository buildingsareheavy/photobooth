"""
Photobooth entry point. 

Initializes pygame and runs the main loop.
"""

import pygame
from enum import Enum
from camera import DevCamera
from config import (
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    DISPLAY_FPS,
    COUNTDOWN_FROM,
    COUNTDOWN_HOLD_SECS,
    FONT_SIZE,
    CAPTURE_FLASH_SECS,
    FLASH_COLOR
)
from ui import draw_countdown


class State(Enum):
    """
    Possible states the photobooth can be in.

    Similar to a union type in TypeScript:
        type State = "IDLE" | "COUNTDOWN" | "CAPTURED"
    """
    IDLE      = "idle"
    COUNTDOWN = "countdown"
    CAPTURED  = "captured"


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Photobooth")

    camera = DevCamera()
    font = pygame.font.SysFont(None, FONT_SIZE, bold=True)
    clock = pygame.time.Clock()

    state = State.IDLE

    # Tracks when the current countdown number started showing (ms)
    countdown_number_start: int = 0
    # Which number we're currently showing (3, 2, 1)
    countdown_current: int = COUNTDOWN_FROM
    # Tracks when we entered the CAPTURED state (ms)
    captured_at: int = 0
    # Run these outside their loops so they don't get recalculated every frame 
    flash_ms: int = int(CAPTURE_FLASH_SECS * 1000)
    hold_ms: int = int(COUNTDOWN_HOLD_SECS * 1000)
    flash_surface = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    flash_surface.fill(FLASH_COLOR)

    running = True
    while running:
        now: int = pygame.time.get_ticks()  # milliseconds since pygame.init()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Only accept trigger in IDLE state - ignore clicks during countdown
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

            # Advance to next number if enough time has passed
            if elapsed_ms >= hold_ms:
                countdown_current -= 1
                countdown_number_start = now

                # Countdown finished - take the photo
                if countdown_current < 1:
                    frame = camera.get_frame(DISPLAY_WIDTH, DISPLAY_HEIGHT)
                    path = camera.save_frame(frame)
                    print(f"Photo saved: {path}")
                    captured_at = now
                    state = State.CAPTURED

            # Still counting - draw the current number over the live feed
            if state == State.COUNTDOWN:
                frame = camera.get_frame(DISPLAY_WIDTH, DISPLAY_HEIGHT)
                draw_countdown(screen, frame, countdown_current, font)

        # State: CAPTURED
        elif state == State.CAPTURED:
            # Instant flash that fades out so the user knows the photo was taken,
            # then loop back to idle
            elapsed: int = now - captured_at

            # calculate opacity - start at 255, fade to 0 over flash_ms
            progress: float = min(elapsed / flash_ms, 1.0)
            alpha: int = int(255 * (1.0 - progress))

            # Draw camera feed underneath
            frame = camera.get_frame(DISPLAY_WIDTH, DISPLAY_HEIGHT)
            screen.blit(frame, (0, 0))

            # Draw white overlay on top with fading alpha
            flash_surface.set_alpha(alpha)
            screen.blit(flash_surface, (0, 0))

            pygame.display.flip()

            if elapsed >= flash_ms:
                state = State.IDLE

        clock.tick(DISPLAY_FPS)

    camera.release()
    pygame.quit()

# Run only if executed directly, not imported
if __name__ == "__main__":
    main()