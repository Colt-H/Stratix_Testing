from pycomm3 import CIPDriver

def stratix_temperature():
    message_path = '192.168.1.101'
    
    with CIPDriver(message_path) as device:
        data = device.generic_message(
            service=b'\x0e',
            class_code=246,
            instance=1,
            attribute=1,
            connected=True,
            unconnected_send=False,
            route_path=False,
            data_format=[('Temperature', 'INT'), ],
            name='Temperature'
        )
        
        print(data)
        
stratix_temperature()