from Message import generic_int

class_code = 246
attribute = 1

for i in range (1, 21):
    instance = i
    name = 'Port '+str(instance)+":"
    data = generic_int(class_code, instance, attribute, name)
    print(data.tag,data.value,"Mbps")
    