from pycomm3 import CIPDriver

def stratix_power_status():
    message_path = '192.168.1.101'
    
    with CIPDriver(message_path) as device:
        data = device.generic_message(
            service=b'\x0e',
            class_code=246,
            instance=1,
            attribute=8,
            connected=True,
            unconnected_send=False,
            route_path=True,
            data_format=[('Power Status', 'INT'), ],
            name='Power Status'
        )
        
        print(data.value)
        
"""         pwr_a = 'on' if data.value['Power Status'] & 0b_1 else 'off'
        pwr_b = 'on' if data.value['Power Status'] & 0b_10 else 'off'
        
        print(f'PWR A: {pwr_a}, PWR B: {pwr_b}') """
        
stratix_power_status()