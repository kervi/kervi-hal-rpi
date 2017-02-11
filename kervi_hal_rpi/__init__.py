from . import gpio_driver
from . import i2c_driver


def get_gpio_driver():
    return gpio_driver.GPIODriver()
