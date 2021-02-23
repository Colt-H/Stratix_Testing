from pycomm3 import CIPDriver, INT
#from pycomm3.logger import configure_default_logger, LOG_VERBOSE

def stratix_temperature():
    message_path = '192.168.1.101'
    
    with CIPDriver(message_path) as device:
        data = device.generic_message(
            service=b'\x0e',
            class_code=246,
            instance=20,
            attribute=1,
            connected=True,
            unconnected_send=False,
            route_path=True,
            data_type=INT,
            name='Temperature'
        )
        
        print(data)

#configure_default_logger(level=LOG_VERBOSE, filename="logs/pycomm3_V1.0.0_Power_Status.log")        
stratix_temperature()