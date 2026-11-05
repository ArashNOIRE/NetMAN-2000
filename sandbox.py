from Globals import devices
from handelers import hDevices


hDevices.add_device("hi","1.1.1.1","PC",devices)
#debug1, debug2=hDevices.find_device_name("John",devices)
#print(f"the john of hi is {debug1} and it's a {debug2}")
#debug1, debug2=hDevices.find_device_name(hDevices.find_device_ip("1.1.1.1",devices),devices)
#debug3 = hDevices.find_device_ip("1.1.1.1",devices)
#print(f"{debug3}, {debug1}, {debug2}")
print(hDevices.add_device("bye","1.1.1.1","PC",devices))

oh_my_pc = hDevices.find_devices_by_type("PC",devices)
print(oh_my_pc)