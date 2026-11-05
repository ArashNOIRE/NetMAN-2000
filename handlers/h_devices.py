lazy import ipaddress
def add_device(Name, IP, Type, theVar):
    try:  # Check IP validity
        ipaddress.IPv4Address(IP)
    except ipaddress.AddressValueError:
        return False, "Invalid IP address."
    # Check duplicate Name
    if Name in theVar:
        return False, "Device name already exists."
    # Check duplicate IP
    for name, values in theVar.items():
        if values[0] == IP:
            return False, "Sorry, this IP already taken."
    # Add device
    theVar[Name] = [IP, Type]
    return True, "Device added successfully."

def find_device_ip(IP,theVar):
    for name, values in theVar.items(): # note: values is The list
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

def find_devices_by_type(Type, theVar):
    result = []
    for name, values in theVar.items():
        if values[1] == Type:
            result.append(name)
    return result

def remove_device(Name, theVar):

    if Name not in theVar:
        return False, "Device not found."

    del theVar[Name]

    return True, "Device removed successfully."