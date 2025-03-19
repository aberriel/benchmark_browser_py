# -*- coding: utf-8 -*-

from .camera_video_capability import CameraVideoCapability


class CameraVideoCapabilities:
    def __init__(self, capabilities: list = [],
                 stereo_sound_rec: bool = False,
                 gyro_eis: bool = False,
                 hdr_10_bit: bool = False,
                 pro_res: bool = False,
                 dolby_vision_hdr: bool = False,
                 super_steady_video: bool = False):
        self.capabilities = capabilities or []
        self.stereo_sound_rec = stereo_sound_rec if stereo_sound_rec is not None else False
        self.gyro_eis = gyro_eis if gyro_eis is not None else False
        self.hdr_10_bit = hdr_10_bit if hdr_10_bit is not None else False
        self.pro_res = pro_res if pro_res is not None else False
        self.dolby_vision_hdr = dolby_vision_hdr if dolby_vision_hdr is not None else False
        self.super_steady_video = super_steady_video if super_steady_video is not None else False
