import psutil
import subprocess

def get_hardware_id():
    # Windows Serial Extractor
    try:
        # Motherboard
        mb = subprocess.check_output('wmic baseboard get serialnumber', shell=True).decode().split('\n')[1].strip()
        # CPU
        cpu = subprocess.check_output('wmic cpu get processorid', shell=True).decode().split('\n')[1].strip()
        # Storage
        disk = subprocess.check_output('wmic diskdrive get serialnumber', shell=True).decode().split('\n')[1].strip()
        
        return f"Motherboard: {mb}, CPU: {cpu}, Storage: {disk}"
    except Exception as e:
        return f"Error retrieving hardware ID: {e}"
