from handlers import h_devices
from globals import devices
from handlers import h_storage
lazy import os


# - - - Display Functions

def soap():
    os.system("cls")

def show_header():
    print("\n" + "=" * 40)
    print("               NetMAN 2K")
    print("=" * 40)


def show_main_menu():
    print("""
    1. Add Device
    2. Remove Device
    3. Rename Device

    4. List All Devices
    5. Find Device

    6. Change Device IP
    7. Change Device Type
    8. Change Device Status

    9. Statistics

    0. Exit
    """)


def show_devices():
    # Check whether any devices exist
    if not devices:
        print("\nNo devices found.")
        return

    # Display all registered devices
    print("\n" + "-" * 75)
    print(f"{'Name':<20} {'IP':<18} {'Type':<15} {'Status':<10}")
    print("-" * 75)

    for name, values in devices.items():
        print(
            f"{name:<20} "
            f"{values['IP']:<18} "
            f"{values['Type']:<15} "
            f"{values['Status']:<10}"
        )

    print("-" * 75)


# - - - Device Operations

def add_device_ui():
    Name = input("Device Name: ")
    IP = input("IP Address: ")
    Type = input("Device Type: ")

    success, message = h_devices.add_device(
        Name, IP, Type, devices
    )

    if success:
        if not h_storage.save_devices(devices):
            print("Warning: Could not save devices to JSON.")
    print(message)


def remove_device_ui():
    Name = input("Device Name: ")

    # Ask for confirmation before removing
    confirm = input(f"Remove {Name}? (Y/N): ")

    if confirm.upper() != "Y":
        print("Operation cancelled.")
        return

    success, message = h_devices.remove_device(Name, devices)
    if success:
        if not h_storage.save_devices(devices):
            print("Warning: Could not save devices to JSON.")
    print(message)


def rename_device_ui():
    OldName = input("Current Name: ")
    NewName = input("New Name: ")

    success, message = h_devices.rename_device(
        OldName, NewName, devices
    )
    if success:
        if not h_storage.save_devices(devices):
            print("Warning: Could not save devices to JSON.")
    print(message)


def change_ip_ui():
    Name = input("Device Name: ")
    IP = input("New IP Address: ")

    success, message = h_devices.change_device_ip(
        Name, IP, devices
    )
    if success:
        if not h_storage.save_devices(devices):
            print("Warning: Could not save devices to JSON.")
    print(message)


def change_type_ui():
    Name = input("Device Name: ")
    Type = input("New Device Type(PC,Server,Router,Switch,Printer): ")

    success, message = h_devices.change_device_type(
        Name, Type, devices
    )
    if success:
        if not h_storage.save_devices(devices):
            print("Warning: Could not save devices to JSON.")
    print(message)


def change_status_ui():
    Name = input("Device Name: ")
    Status = input("New Status (Online/Offline): ")

    success, message = h_devices.change_device_status(
        Name, Status, devices
    )
    if success:
        if not h_storage.save_devices(devices):
            print("Warning: Could not save devices to JSON.")
    print(message)


# - - - Search Menu

def search_menu():
    while True:
        print("""
        ===== SEARCH DEVICES =====

        1. Find by Name
        2. Find by IP
        3. Find by Type
        4. Find by Status

        0. Back
        """)

        choice = input("Select: ")

        if choice == "1":
            Name = input("Device Name: ")
            code, ip, device_type, status = h_devices.find_device_name(Name, devices)
            print(f"{Name}'s IP is {ip}, it's a {device_type} and {status}." if code else "Device not found.")

        elif choice == "2":
            IP = input("IP Address: ")
            code, name, device_type, status = h_devices.find_device_ip(IP, devices)
            print(f"There is a device called {name} with IP address of {IP}. it's a {device_type} and {status}." if code else "Device not found.")

        elif choice == "3":
            Type = input("Device Type: ")
            code, result = h_devices.find_devices_by_type(Type, devices)
            if code:
                print("Found Devices:")
                for i, device in enumerate(result, start=1):
                    print(f"  {i}. {device}")

        elif choice == "4":
            Status = input("Device Status: ")
            code, result = h_devices.find_devices_by_status(Status, devices)
            if code:
                print("Found Devices:")
                for i, device in enumerate(result, start=1):
                    print(f"  {i}. {device}")

        elif choice == "0":
            break

        else:
            print("Invalid option.")


# - - - Statistics

def show_statistics():
    total = len(devices)

    online_result = h_devices.find_devices_by_status(
        "Online", devices
    )

    offline_result = h_devices.find_devices_by_status(
        "Offline", devices
    )

    online = len(online_result[1]) if online_result else 0
    offline = len(offline_result[1]) if offline_result else 0

    print("\n===== DEVICE STATISTICS =====")
    print(f"Total Devices   : {total}")
    print(f"Online Devices  : {online}")
    print(f"Offline Devices : {offline}")
    

# - - - Main Terminal Loop

def run_terminal():
    while True:
        soap()
        show_header()
        show_main_menu()

        choice = input("Select an option: ")

        if choice == "1":
            soap()
            add_device_ui()

        elif choice == "2":
            soap()
            remove_device_ui()

        elif choice == "3":
            soap()
            rename_device_ui()

        elif choice == "4":
            soap()
            show_devices()

        elif choice == "5":
            soap()
            search_menu()

        elif choice == "6":
            soap()
            change_ip_ui()

        elif choice == "7":
            soap()
            change_type_ui()

        elif choice == "8":
            soap()
            change_status_ui()

        elif choice == "9":
            soap()
            show_statistics()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            soap()
            print("Invalid option. Please try again.")

        input("\nPress Enter to continue...")
