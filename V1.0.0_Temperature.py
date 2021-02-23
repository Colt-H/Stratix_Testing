from Message import generic_int

class_code = 863
instance = 1
attribute = 1
name = 'Temperature'

data = generic_int(class_code, instance, attribute, name)
print(data.tag,data.value)