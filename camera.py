"""
Provides camera functionality

Uses OpenCV to capture frames from a USB or built-in webcam and
convert them to pygame surfaces.
"""

import os
from datetime import datetime
import cv2
from PIL import Image
import pygame
import numpy as np
from config import DEV_CAMERA_INDEX, CAPTURE_DIR, CAPTURE_PREFIX, CAPTURE_QUALITY


class DevCamera:
    """
    Webcam-based camera for development on a regular Linux or macOS machine.
    Uses OpenCV to capture frames and converts them to pygame Surfaces.
    """

    def __init__(self) -> None:
        self._cap = cv2.VideoCapture(DEV_CAMERA_INDEX)

        if not self._cap.isOpened():
            raise RuntimeError(
                f"Could not open webcam at index {DEV_CAMERA_INDEX}. "
                "Check that your webcam is connected and try a different index "
                "in config.py (DEV_CAMERA_INDEX)."
            )

    def get_frame(self, width: int, height: int) -> pygame.Surface:
        """Returns a scaled pygame Surface from the current webcam frame."""
        ret, frame = self._cap.read()

        if not ret:
            raise RuntimeError("Failed to read frame from webcam.")

        # OpenCV gives us BGR, so convert to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # numpy array -> pygame Surface, then scale to display size
        surface = pygame.surfarray.make_surface(np.transpose(frame, (1, 0, 2)))
        return pygame.transform.scale(surface, (width, height))
    
    def save_frame(self, surface: pygame.Surface) -> str:
        """
        Saves surface as a timestamped JPEG to the captures directory.
        Returns the saved filepath.
        captures/photo_20260101_XXXXXX.jpg
        """
        os.makedirs(CAPTURE_DIR, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{CAPTURE_PREFIX}_{timestamp}.jpg"
        filepath = os.path.join(CAPTURE_DIR, filename)

        # Convert pygame Surface → PIL Image → save as JPEG
        raw = pygame.image.tostring(surface, "RGB")
        image = Image.frombytes("RGB", surface.get_size(), raw)
        image.save(filepath, "JPEG", quality=CAPTURE_QUALITY)

        return filepath

    def capture(self, width: int, height: int) -> pygame.Surface:
        return self.get_frame(width, height)

    def release(self) -> None:
        """
        Release the webcam resource.
        Always call this on exit.
        """
        self._cap.release()