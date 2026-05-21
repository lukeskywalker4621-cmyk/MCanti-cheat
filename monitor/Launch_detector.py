#used to detect when the Minecraft launcher is launched and closed

#imports
import psutil
import time
from HWID import get_hardware_id

def is_minecraft_running():
    for proc in psutil.process_iter(['name', 'cmdline']):
        try:
            # Check for the Minecraft executable
            if proc.info['name'] == 'javaw.exe' or proc.info['name'] == 'java':
                # Check the command line args to confirm it's Minecraft
                cmdline = proc.info.get('cmdline')
                if cmdline and any('minecraft' in str(arg).lower() for arg in cmdline):
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def detect_launcher():
    print("Monitoring for Minecraft launches...")
    is_running = False
    
    while True:
        currently_running = is_minecraft_running()
        
        if currently_running and not is_running:
            print("Minecraft has been launched!")
            hwid = get_hardware_id()
            print(f"Hardware ID: {hwid}")
            is_running = True
            
        elif not currently_running and is_running:
            print("Minecraft has been closed.")
            is_running = False
        time.sleep(5)

if __name__ == "__main__":
    detect_launcher()