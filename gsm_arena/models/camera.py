# -*- coding: utf-8 -*-


class Camera:
    def __init__(self, manufacturer: str = None,
                 brand: str = None,
                 model: str = None,
                 resolution: int = None,
                 pixel_size: int = None,
                 sensor_size: str = None,
                 aperture_factor: float = None,
                 position: CameraPosition = None,
                 c_type: CameraType = None,
                 eis: bool = False,
                 ois: bool = False,
                 sensor_shift_ois: bool = False,
                 optical_zoom: int = 1,
                 digital_zoom: int = 1,
                 pdaf: bool = False,
                 dual_pixel_pdaf: bool = False,
                 multi_direction_pdaf: bool = False,
                 video_capabilities: list = []):
        self.manufacturer = manufacturer
        self.brand = brand
        self.model = model
        self.resolution = resolution
        self.pixel_size = pixel_size
        self.sensor_size = sensor_size
        self.aperture_factor = aperture_factor
        self.position = position
        self.c_type = c_type
        self.eis = eis if eis is not None else False
        self.ois = ois if ois is not None else False
        self.sensor_shift_ois = sensor_shift_ois if sensor_shift_ois is not None else False
        self.optical_zoom = optical_zoom
        self.digital_zoom = digital_zoom
        self.pdaf = pdaf if pdaf is not None else False
        self.dual_pixel_pdaf = dual_pixel_pdaf if dual_pixel_pdaf is not None else False
        self.multi_direction_pdaf = multi_direction_pdaf if multi_direction_pdaf is not None else False
        self.video_capabilities = video_capabilities or []
