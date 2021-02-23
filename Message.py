from pycomm3 import CIPDriver, BOOL, SINT, INT, DINT, LINT, REAL, STIME, DATE, TIME_OF_DAY, DATE_AND_TIME, StringDataType, STRING, STRING2, DWORD

def generic_int(msgclass, msginstance, msgattribute, msgname):
    message_path = '192.168.1.101'
    
    with CIPDriver(message_path) as device:
        data = device.generic_message(
            service=b'\x0e',
            class_code=msgclass,
            instance=msginstance,
            attribute=msgattribute,
            connected=True,
            unconnected_send=False,
            route_path=True,
            data_type=INT,
            name=msgname
        )
        
        return data

def generic_dword(msgclass, msginstance, msgattribute, msgname):
    message_path = '192.168.1.101'
    
    with CIPDriver(message_path) as device:
        data = device.generic_message(
            service=b'\x0e',
            class_code=msgclass,
            instance=msginstance,
            attribute=msgattribute,
            connected=True,
            unconnected_send=False,
            route_path=True,
            data_type=DWORD,
            name=msgname
        )
        
        return data