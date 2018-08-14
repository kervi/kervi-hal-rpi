import io
import time
from PIL import Image, ImageDraw
from kervi.vision.camera import FrameCameraDeviceDriver
import picamera
from threading import Condition

class _StreamingMPEGBuffer(object):
    def __init__(self, driver):
        self.frame = None
        self.driver = driver
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                frame = self.buffer.getvalue()
                self.driver.frame_ready(frame)
                #self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class CameraDriver(FrameCameraDeviceDriver):
    def __init__(self):
        FrameCameraDeviceDriver.__init__(self)
        self._buffer_type = "jpeg"

    def capture_frames(self):
        with picamera.PiCamera() as camera:
            print("start Raspberry Pi camera")
            camera.resolution = (self.camera.width, self.camera.height)
            camera.framerate =  self.camera.fps
            camera.hflip = self.camera.flip_horizontal
            camera.vflip = self.camera.flip_vertical
            camera.shutter_speed = 0
            time.sleep(2)
            output = _StreamingMPEGBuffer(self)
            
            camera.start_recording(output, format='mjpeg')
            while not self.terminate:
                time.sleep(1)
            camera.stop_recording()
            

