def add_device(Name,IP,Type,theVar):
    theVar[Name] = [IP,Type]

def find_device_ip(IP,theVar):
    for name, values in theVar.items():
        if IP in values:
            return name
    return None

def find_device_name(Name,theVar):
    if theVar.get(Name): 
        temp_0 = theVar.get(Name) # it will be a list with content of [IP,Type]
        temp_1 = temp_0[0] # IP
        temp_2 = temp_0[1] # Type
        return temp_1, temp_2
    return None
