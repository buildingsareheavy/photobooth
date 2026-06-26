"""
Handles UI (view layer) for camera feed.

It only draws things, it doesn't handle any logic or state.
"""

import pygame
from config import (
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    NUMBER_COLOR,
    NUMBER_ALPHA,
    SHADOW_COLOR,
    SHADOW_ALPHA,
    SHADOW_OFFSET,
    CIRCLE_COLOR,
    CIRCLE_ALPHA,
    CIRCLE_RADIUS,
    OVERLAY_X,
    OVERLAY_Y,
)

def draw_countdown(
    screen: pygame.Surface,
    camera_frame: pygame.Surface,
    number: int,
    font: pygame.font.Font,
) -> None:
    """
    Draw a single countdown number over the live camera frame.

    Layers from bottom to top:
      1. Camera frame (live feed)
      2. Semi-transparent dark circle (backing shape)
      3. Drop shadow
      4. Number

    Args:
        screen:       The main pygame display surface to draw onto.
        camera_frame: The current webcam frame as a pygame Surface.
        number:       The countdown number to display (3, 2, 1).
        font:         The pygame Font object to render the number with.
    """
    # Calculate overlay center from config percentages
    cx: int = int(DISPLAY_WIDTH * OVERLAY_X)
    cy: int = int(DISPLAY_HEIGHT * OVERLAY_Y)

    # Layer 1 - camera frame
    screen.blit(camera_frame, (0, 0))

    # Layer 2 - semi-transparent dark circle behind the number
    circle_surface = pygame.Surface((CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2), pygame.SRCALPHA)
    pygame.draw.circle(
        circle_surface,
        (*CIRCLE_COLOR, CIRCLE_ALPHA),
        (CIRCLE_RADIUS, CIRCLE_RADIUS),
        CIRCLE_RADIUS,
    )
    screen.blit(circle_surface, (cx - CIRCLE_RADIUS, cy - CIRCLE_RADIUS))

    # Layer 3 - drop shadow
    shadow_surface = font.render(str(number), True, SHADOW_COLOR)
    shadow_surface.set_alpha(SHADOW_ALPHA)
    screen.blit(shadow_surface, shadow_surface.get_rect(center=(cx + SHADOW_OFFSET, cy + SHADOW_OFFSET)))

    # Layer 4 - the number itself
    num_surf = font.render(str(number), True, NUMBER_COLOR)
    num_surf.set_alpha(NUMBER_ALPHA)
    screen.blit(num_surf, num_surf.get_rect(center=(cx, cy)))

    pygame.display.flip()