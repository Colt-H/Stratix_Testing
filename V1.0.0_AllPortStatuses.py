from Message import generic_dword

class_code = 246
instance = 0
attribute = 101
name = 'Link Status'

data = generic_dword(class_code, instance, attribute, name)

for i in range (1,21):
    print(data.tag, "Port", i, data.value[i])
    