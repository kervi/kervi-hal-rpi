from kervi.camera import FrameCameraDeviceDriver
from PIL import Image, ImageDraw
import picamera
import time

class CameraDriver(FrameCameraDeviceDriver):
    def __init__(self):
        FrameCameraDeviceDriver.__init__(self)

    def capture_frames(self):
        with picamera.PiCamera() as camera:
            camera.resolution = (self.camera.width, self.camera.height)
            camera.framerate = self.camera.fps
            time.sleep(2)
            stream = io.BytesIO()
            for foo in camera.capture_continous(stream, format="jpeg", use_video_port=True):
                stream.seek(0)
                image = Image.open(stream)
                self.frame_ready(image)
                stream.seek(0)
                self.wait_next_frame()
                if self.terminate:
                    break
