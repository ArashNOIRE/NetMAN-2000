# NetMAN 2000

A simple Python-based terminal application for managing network devices, built with Python.

## Features

- Add, remove, and rename devices
- View all registered devices
- Search devices by name, IP, type, or status
- Change device IP address, type, and status
- Display device statistics
- Validate IP addresses and prevent duplicate names and IPs
- Automatically save device information to a JSON file
- Load previously saved devices when the application starts
- Persistent data storage between application sessions

## Device Types

PC, Server, Router, Switch, Printer

## Device Status

Online, Offline

## Data Storage

NetMAN uses JSON for persistent device storage.

- Device information is stored in `data/devices.json`.
- Existing devices are automatically loaded when the application starts.
- Changes are saved to the JSON file after successful operations.
- The `data/` directory and JSON file are created automatically if they do not exist.

## How to Run

1. Make sure Python 3 is installed.
2. Clone or download the project.
3. Run the following command:

```bash
python main.py
```

No external libraries are required.

## Project Structure

```text
NetMAN/
│
├── main.py
├── globals.py
│
├── handlers/
│   ├── h_devices.py
│   └── h_storage.py
│
├── ui/
│   └── terminal.py
│
└── data/
    └── devices.json
```

## Modules

- `main.py` – Application entry point and initialization
- `globals.py` – Stores the shared device dictionary
- `handlers/h_devices.py` – Device management operations and validation
- `handlers/h_storage.py` – JSON loading and saving operations
- `ui/terminal.py` – Terminal user interface
- `data/devices.json` – Persistent device database