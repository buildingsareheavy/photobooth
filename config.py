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
# Webcam location index: /dev/video0 = 0, /dev/video1 = 1 etc.
DEV_CAMERA_INDEX: int = 0

# Countdown
COUNTDOWN_FROM: int         = 5
COUNTDOWN_HOLD_SECS: float  = 1.0
CAPTURE_FLASH_SECS: float = 1.5

# UI
FONT_SIZE: int                      = 280               # pixels
NUMBER_COLOR: tuple[int, int, int]  = (255, 255, 255)   # white
NUMBER_ALPHA: int                   = 210               # 0-255
SHADOW_COLOR: tuple[int, int, int]  = (0, 0, 0)         # black
SHADOW_ALPHA: int                   = 130               # 0-255
SHADOW_OFFSET: int                  = 8                 # pixels
CIRCLE_COLOR: tuple[int, int, int]  = (0, 0, 0)         # black
CIRCLE_ALPHA: int                   = 110               # 0-255
CIRCLE_RADIUS: int                  = 160               # pixels
FLASH_COLOR: tuple[int, int, int]   = (255, 255, 255)   # white

# Overlay position (center of screen by default)
OVERLAY_X: float = 0.5  # percentage of screen width  (0.0 - 1.0)
OVERLAY_Y: float = 0.5  # percentage of screen height (0.0 - 1.0)

# Capture Directory
# this is the name of the folder that images will get saved to in your project
CAPTURE_DIR: str = "captures"


