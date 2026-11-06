# NetMAN 2000

A simple Python-based terminal application for managing network devices.

## Features
- Add, remove, and rename devices
- View all registered devices
- Search devices by name, IP, type, or status
- Change device IP address, type, and status
- Display device statistics
- Validate IP addresses and prevent duplicate names and IPs

## Device Types
PC, Server, Router, Switch, Printer

## Device Status
Online, Offline

## How to Run

1. Make sure Python 3 is installed.
2. Clone or download the project.
3. Run the following command:

```bash
python main.py
```

## Project Structure

- `main.py` – Application entry point
- `globals.py` – Stores device data
- `handlers/` – Device management logic
- `ui/` – Terminal user interface