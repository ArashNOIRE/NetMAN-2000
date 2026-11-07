lazy import ipaddress

# - - - Delete and Adding Devices
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
    # Validate new status
    if Type not in ("PC","Server","Router","Switch","Printer"):
        return False, "Invalid device type."
    # Add device
    theVar[Name] = {
        "IP": IP,
        "Type": Type,
        "Status": Status
    }
    return True, "Device added successfully."

def remove_device(Name, theVar):
    # Check whether the device exists
    if Name not in theVar:
        return False, "Device not found."
    # Remove the device from the dictionary
    del theVar[Name]
    return True, "Device removed successfully."

# - - - Finding and Showing Devices

def find_device_ip(IP, theVar):
    # Search for a device using its IP address
    for name, values in theVar.items():
        if values["IP"] == IP:
            return True, name, values["Type"], values["Status"]
    return False, None, None, None


def find_device_name(Name, theVar):
    # Find a device using its name
    if Name in theVar:
        return True, theVar[Name]["IP"], theVar[Name]["Type"], theVar[Name]["Status"]
    return False, None, None, None


def find_devices_by_type(Type, theVar):
    # Find all devices that match the specified device type
    result = []
    for name, values in theVar.items():
        if values["Type"] == Type:
            result.append(name)
    if result:
        return True, result
    return False, None, None, None

def find_devices_by_status(Status, theVar):
    # Find devices by their status
    result = []
    for name, values in theVar.items():
        if values["Status"] == Status:
            result.append(name)
    if result:
        return True, result
    return False, None, None, None

# - - - Changing in Devices

def change_device_status(Name, Status, theVar):
    # Check device existence
    if Name not in theVar:
        return False, "Device not found."
    # Validate new status
    if Status not in ("Online", "Offline"):
        return False, "Invalid device status."
    # Update device status
    theVar[Name]["Status"] = Status
    return True, "Device status updated successfully."

def rename_device(OldName, NewName, theVar):
    # Check whether the old device name exists
    if OldName not in theVar:
        return False, "Device not found."
    # Check whether the new device name is already taken
    if NewName in theVar:
        return False, "New device name already exists."
    # Rename device while preserving its information
    theVar[NewName] = theVar.pop(OldName)
    return True, "Device renamed successfully."

def change_device_ip(Name, IP, theVar):
    # Check device existence
    if Name not in theVar:
        return False, "Device not found."
    # Validate new IP address
    try:
        ipaddress.IPv4Address(IP)
    except ipaddress.AddressValueError:
        return False, "Invalid IP address."
    # Check whether the IP is already assigned to another device
    for name, values in theVar.items():
        if name != Name and values["IP"] == IP:
            return False, "Sorry, this IP is already taken."
    # Update device IP address
    theVar[Name]["IP"] = IP
    return True, "Device IP updated successfully."

def change_device_type(Name, Type, theVar):
    # Check device existence
    if Name not in theVar:
        return False, "Device not found."
    # Validate new status
    if Type not in ("PC","Server","Router","Switch","Printer"):
        return False, "Invalid device type."
    # Update device type
    theVar[Name]["Type"] = Type
    return True, "Device type updated successfully."