"""
Application configuration.

Contains display, camera, and image capture settings.
All user-adjustable settings should be maintained here.
"""

# Display

DISPLAY_WIDTH: int  = 640
DISPLAY_HEIGHT: int = 480
DISPLAY_FPS: int    = 30

# Camera 
CAPTURE_PREFIX: str  = "photo"
CAPTURE_QUALITY: int = 95 # JPEG quality 0-100

# UI
COUNTDOWN_FROM: int         = 3
COUNTDOWN_HOLD_SECS: float  = 1.0
COUNTDOWN_CAPTURE_WAIT: int = 250 #milliseconds

# Countdown
FONT_SIZE: int                      = 280
NUMBER_COLOR: tuple[int, int, int]  = (255, 255, 255)   # white
NUMBER_ALPHA: int                   = 210               # 0-255
SHADOW_COLOR: tuple[int, int, int]  = (0, 0, 0)
SHADOW_ALPHA: int                   = 130
SHADOW_OFFSET: int                  = 8                 # pixels
CIRCLE_COLOR: tuple[int, int, int]  = (0, 0, 0)
CIRCLE_ALPHA: int                   = 110
CIRCLE_RADIUS: int                  = 160
# Overlay position (center of screen by default)
OVERLAY_X: float = 0.5  # percentage of screen width  (0.0 - 1.0)
OVERLAY_Y: float = 0.5  # percentage of screen height (0.0 - 1.0)

# /dev/video0 = 0, /dev/video1 = 1 etc.
DEV_CAMERA_INDEX: int = 0

# Capture Directory
CAPTURE_DIR: str = "captures"


