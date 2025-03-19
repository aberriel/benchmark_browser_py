# -*- coding: utf-8 -*-

from commons.models import CameraVideoCapabilities


class CameraSystem:
    def __init__(self, cameras: list = [],
                 flash: bool = False,
                 led_flash: bool = False,
                 dual_led_flash: bool = False,
                 hdr: bool = False,
                 auto_hdr: bool = False,
                 laser_af: bool = False,
                 best_face: bool = False,
                 panorama: bool = False,
                 video_capabilities: list = []):
        self.cameras = cameras or []
        self.flash = flash if flash is not None else False
        self.led_flash = led_flash if led_flash is not None else False
        self.dual_led_flash = dual_led_flash if dual_led_flash is not None else False
        self.hdr = hdr if hdr is not None else False
        self.auto_hdr if auto_hdr is not None else False
        self.laser_af = laser_af if laser_af is not None else False
        self.best_face = best_face if best_face is not None else False
        self.panorama = panorama if panorama is not None else False
        self.video_capabilities = video_capabilities or []
    