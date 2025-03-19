# -*- coding: utf-8 -*-

from .camera_video_resolution import CameraVideoResolution


class CameraVideoCapability:
    def __init__(self, resolution: CameraVideoResolution,
                 fps: list = []):
        self.resolution = resolution
        self.fps = fps
