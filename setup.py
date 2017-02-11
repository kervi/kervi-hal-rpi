import distutils
from setuptools import setup
from kervi_hal_rpi.version import VERSION

try:
    distutils.dir_util.remove_tree("dist")
except:
    pass

setup(
    name='kervi-hal-rpi',
    version=VERSION,
    packages=[
        "kervi_hal_rpi",
    ],
    install_requires=[
        'psutil'
    ],

)