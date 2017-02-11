import RPi.GPIO as GPIO


class GPIODriver(object):
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self._pwm_pins = {}

    def define_pin_in(self, pin):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def define_pin_out(self, pin):
        GPIO.setup(pin, GPIO.OUT)

    def define_pin_pwm(self, pin, frequency):
        GPIO.setup(pin, GPIO.OUT)
        pwm_pin = GPIO.PWM(pin, frequency)
        self._pwm_pins[pin] = pwm_pin

    def set_pin_low(self, pin):
        GPIO.output(pin, GPIO.LOW)

    def set_pin_high(self, pin):
        GPIO.output(pin, GPIO.HIGH)

    def get_pin(self, pin):
        return GPIO.input(pin)

    def start_pwm(self, pin, duty_cycle):
        self._pwm_pins[pin].start(duty_cycle)

    def stop_pwm(self, pin):
        self._pwm_pins[pin].stop

    def listen_pin(self, pin, callback, bounce_time=200):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.BOTH, callback=callback, bouncetime=bounce_time)

    def listen_rising_pin(self, pin, callback, bounce_time=200):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.RISING, callback=callback, bouncetime=bounce_time)

    def listen_falling_pin(self, pin, callback, bounce_time=200):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=callback, bouncetime=bounce_time)
