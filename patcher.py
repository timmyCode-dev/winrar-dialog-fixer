import sys
import time
from core.window_hook import WindowDialogSuppressor

def start_automation_loop():
    print("[SERVICE] Starting WinRAR Dialog Fixer background thread...")
    time.sleep(0.5)
    
    suppressor = WindowDialogSuppressor()
    print("[SERVICE] Hooking into Windows GUI system subsystem. Monitoring handles...")
    
    cycle_count = 0
    max_cycles = 10 
    
    while cycle_count < max_cycles:
        runtime_report = suppressor.scan_and_suppress()
        
        if runtime_report.get("hooked") and runtime_report.get("success"):
            print(f"[ACTION] Intercepted dialogue trigger at HWND: {runtime_report['handle']}. Closed hook safely.")
            time.sleep(1.5)
        
        time.sleep(0.5)
        cycle_count += 1
        
    print("[INFO] Background optimization runtime completed its operational cycle.")

if __name__ == "__main__":
    start_automation_loop()
