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

# /dev/video0 = 0, /dev/video1 = 1 etc.
DEV_CAMERA_INDEX: int = 0

# Capture Directory
CAPTURE_DIR: str = "captures"


