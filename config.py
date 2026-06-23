"""
config.py
---------
Central configuration for the photobooth
"""

# Display

DISPLAY_WIDTH: int  = 800
DISPLAY_HEIGHT: int = 480
DISPLAY_FPS: int    = 30

# Camera 

# /dev/video0 = 0, /dev/video1 = 1 etc.
MOCK_CAMERA_INDEX: int = 0

# Capture Directory

CAPTURE_DIR: str = "captures"