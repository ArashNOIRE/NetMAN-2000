from ui.terminal import run_terminal
from handlers import h_storage
from globals import devices

if __name__ == "__main__":
    # Load devices from JSON
    devices.update(h_storage.load_devices())
    # Run application
    run_terminal()
    # Save devices before exiting
    h_storage.save_devices(devices)
