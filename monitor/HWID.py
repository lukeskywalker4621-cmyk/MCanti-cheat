import subprocess
import json

def get_hardware_id():
    # Windows Serial Extractor
    try:
        # Motherboard
        mb = subprocess.check_output('wmic baseboard get serialnumber', shell=True).decode().split('\n')[1].strip()
        # CPU
        cpu = subprocess.check_output('wmic cpu get processorid', shell=True).decode().split('\n')[1].strip()
        # Storage
        disk = subprocess.check_output('wmic diskdrive get serialnumber', shell=True).decode().split('\n')[1].strip()

        memory = subprocess.check_output('wmic memorychip get serialnumber', shell=True).decode().split('\n')[1].strip()
        
        return f"Motherboard: {mb}, CPU: {cpu}, Storage: {disk}, Memory: {memory}"
    except Exception as e:
        return f"Error retrieving hardware ID: {e}"
    
def save_hardware_id(hwid):
    with open('HWIDs.json', 'w') as f:
        json.dump({'hardware_id': hwid}, f)

def no_duplicate_hwid(hwid):
    try:
        with open('HWIDs.json', 'r') as f:
            data = json.load(f)
            return data.get('hardware_id') != hwid
    except FileNotFoundError:
        return True  # No existing HWID, so it's not a duplicate

    
