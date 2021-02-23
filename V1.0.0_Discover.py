from pycomm3 import CIPDriver
from pycomm3.logger import configure_default_logger, LOG_VERBOSE

def discover():
    print(CIPDriver.discover())

configure_default_logger(level=LOG_VERBOSE, filename="logs/pycomm3_V1.0.0_Discover.log")
discover()