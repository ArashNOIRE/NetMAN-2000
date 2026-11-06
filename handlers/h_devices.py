import ipaddress


def add_device(Name, IP, Type, theVar, Status="Offline"):
    # Check IP validity
    try:
        ipaddress.IPv4Address(IP)
    except ipaddress.AddressValueError:
        return False, "Invalid IP address."
    # Validate device status
    if Status not in ("Online", "Offline"):
        return False, "Invalid device status."
    # Check duplicate Name
    if Name in theVar:
        return False, "Device name already exists."
    # Check duplicate IP
    for name, values in theVar.items():
        if values["IP"] == IP:
            return False, "Sorry, this IP already taken."
    # Add device
    theVar[Name] = {
        "IP": IP,
        "Type": Type,
        "Status": Status
    }
    return True, "Device added successfully."


def find_device_ip(IP, theVar):
    # Search for a device using its IP address
    for name, values in theVar.items():
        if values["IP"] == IP:
            return name
    return None


def find_device_name(Name, theVar):
    # Find a device using its name
    if Name in theVar:
        return theVar[Name]["IP"], theVar[Name]["Type"], theVar[Name]["Status"]
    return None


def find_devices_by_type(Type, theVar):
    # Find all devices that match the specified device type
    result = []
    for name, values in theVar.items():
        if values["Type"] == Type:
            result.append(name)
    return result


def remove_device(Name, theVar):
    # Check whether the device exists
    if Name not in theVar:
        return False, "Device not found."
    # Remove the device from the dictionary
    del theVar[Name]
    return True, "Device removed successfully."
