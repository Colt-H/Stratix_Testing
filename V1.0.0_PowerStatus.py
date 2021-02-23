from Message import generic_int

class_code = 863
instance = 1
attribute = 8
name = 'Power Status'

data = generic_int(class_code, instance, attribute, name)
pwr_a = 'on' if data.value & 0b_1 else 'off'
pwr_b = 'on' if data.value & 0b_10 else 'off'

print(f'PWR A: {pwr_a}, PWR B: {pwr_b}')