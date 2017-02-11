import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class GPIODriver(object):
    def __init__(self):
        print("init gpio driver")
        self._pwm_pins = {}

    def define_pin(self, pin, io_type, **kwargs):
        if io_type == "in":
            GPIO.setup(pin, GPIO.IN)
        elif io_type == "out":
            GPIO.setup(pin, GPIO.OUT)
        elif io_type == "pwm":
            GPIO.setup(pin, GPIO.OUT)
            pwm = GPIO.PWM(pin, kwargs.get("frequency", 60))
            self._pwm_pins[pin] = pwm

    def set_pin(self, pin, state):
        if state:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)

    def get_pin(self, pin):
        return GPIO.input(pin)

    def listen_pin(self, pin):
        print("listen pin")

    def set_duty_cycle(self, pin, duty_cycle):
        self._pwm_pins[pin].ChangeDutyCycle(duty_cycle)
