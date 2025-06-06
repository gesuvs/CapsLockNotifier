import ctypes
from ctypes import wintypes
import sys
from app.toast import ToastNotifier

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
VK_CAPITAL = 0x14


# Compatibilidade para 64 bits
LRESULT = ctypes.c_longlong if sys.maxsize > 2**32 else ctypes.c_long
HOOKPROC = ctypes.WINFUNCTYPE(LRESULT, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)

user32.CallNextHookEx.restype = LRESULT
user32.CallNextHookEx.argtypes = [ctypes.c_void_p, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM]


class CapsLockNotifier:
  
  def __init__(self):
    self.hooked = None
    self.last_state = self._get_capslock_state()
    
  
  def _get_capslock_state(self):
    return bool(user32.GetKeyState(VK_CAPITAL) & 0x0001)  
    

  def _hook_proc(self, nCode, wParam, lParam):
    if nCode == 0 and wParam == WM_KEYDOWN:
      kbd_struct = ctypes.cast(lParam, ctypes.POINTER(KBDLLHOOKSTRUCT)).contents
      if kbd_struct.vkCode == VK_CAPITAL:
        new_state = self._get_capslock_state()
        if new_state != self.last_state:
          self.last_state = new_state
          status = "DESATIVADO" if new_state  else "ATIVADO"
          ToastNotifier(f"Caps Lock {status}").show()
    
    return user32.CallNextHookEx(self.hooked, nCode, wParam, lParam)

        
  def run(self):
    print("Iniciando o monitor de Caps Lock...")

    self.pointer = HOOKPROC(self._hook_proc)
    h_module = None
    
    print(f"[DEBUG] Module Handle: {h_module}")

    self.hooked = user32.SetWindowsHookExW(
        WH_KEYBOARD_LL,
        self.pointer,
        h_module,
        0
    )

    if not self.hooked:
        raise Exception("Hook do teclado falhou.")

    msg = wintypes.MSG()
    while user32.GetMessageW(ctypes.byref(msg), 0, 0, 0) != 0:
        user32.TranslateMessage(ctypes.byref(msg))
        user32.DispatchMessageW(ctypes.byref(msg))

class KBDLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ("vkCode", wintypes.DWORD),
        ("scanCode", wintypes.DWORD),
        ("flags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]