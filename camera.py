"""
camera.py
---------
In mock mode, uses a regular USB or built-in webcam via OpenCV
"""

import cv2
import pygame
import numpy as np
from config import MOCK_CAMERA_INDEX


class MockCamera:
    """
    Webcam-based camera for development on a regular Linux or macOS machine.
    Uses OpenCV to capture frames and converts them to pygame Surfaces.
    """

    def __init__(self) -> None:
        self._cap = cv2.VideoCapture(MOCK_CAMERA_INDEX)

        if not self._cap.isOpened():
            raise RuntimeError(
                f"Could not open webcam at index {MOCK_CAMERA_INDEX}. "
                "Check that your webcam is connected and try a different index "
                "in config.py (MOCK_CAMERA_INDEX)."
            )

    def get_frame(self, width: int, height: int) -> pygame.Surface:
        """
        Capture a single frame from the webcam and return it as a
        pygame Surface scaled to dimensions in config.py (DISPLAY_WIDTH and
        DISPLAY_WIDTH)
        """
        ret, frame = self._cap.read()

        if not ret:
            raise RuntimeError("Failed to read frame from webcam.")

        # OpenCV gives us BGR, so convert to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # numpy array -> pygame Surface, then scale to display size.
        surface = pygame.surfarray.make_surface(np.transpose(frame, (1, 0, 2)))
        return pygame.transform.scale(surface, (width, height))

    def capture(self, width: int, height: int) -> pygame.Surface:
        return self.get_frame(width, height)

    def release(self) -> None:
        """
        Release the webcam resource.
        Always call this on exit.
        """
        self._cap.release()