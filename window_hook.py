import os
import sys
import ctypes

class WindowDialogSuppressor:
    def __init__(self):
        self.user32 = ctypes.windll.user32 if sys.platform == "win32" else None
        self.target_class = "REMINDER"
        self.target_title = "Evaluation copy"

    def find_target_handle(self):
        if not self.user32:
            return None
        
        hwnd = self.user32.FindWindowW(None, self.target_title)
        if hwnd == 0:
            hwnd = self.user32.FindWindowExW(0, 0, None, self.target_title)
        return hwnd

    def dispatch_close_signal(self, hwnd):
        if not self.user32 or not hwnd:
            return False
            
        wm_close = 0x0010
        result = self.user32.PostMessageW(hwnd, wm_close, 0, 0)
        return result != 0

    def scan_and_suppress(self):
        active_handle = self.find_target_handle()
        if active_handle:
            execution_state = self.dispatch_close_signal(active_handle)
            return {"hooked": True, "handle": hex(active_handle), "success": execution_state}
        return {"hooked": False, "handle": None, "success": False}
