# directkeys.py
# http://stackoverflow.com/questions/13564851/generate-keyboard-events
# msdn.microsoft.com/en-us/library/dd375731

import ctypes
from ctypes import wintypes
import time
from lol_tools.key_types import KeyTypes


def get_screen_resolution():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()  # 使进程对 DPI 感知，获取实际分辨率
    screenWidth = user32.GetSystemMetrics(0)
    screenHeight = user32.GetSystemMetrics(1)
    return screenWidth, screenHeight


screenWidth, screenHeight = get_screen_resolution()

user32 = ctypes.WinDLL("user32", use_last_error=True)

INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004
KEYEVENTF_SCANCODE = 0x0008

MAPVK_VK_TO_VSC = 0

# List of all codes for keys:
# # msdn.microsoft.com/en-us/library/dd375731
UP = 0x26
DOWN = 0x28
A = 0x41
SPACE = 0x20

# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM


class MOUSEINPUT(ctypes.Structure):
    _fields_ = (
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", wintypes.ULONG_PTR),
    )


class KEYBDINPUT(ctypes.Structure):
    _fields_ = (
        ("wVk", wintypes.WORD),
        ("wScan", wintypes.WORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", wintypes.ULONG_PTR),
    )

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk, MAPVK_VK_TO_VSC, 0)


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (
        ("uMsg", wintypes.DWORD),
        ("wParamL", wintypes.WORD),
        ("wParamH", wintypes.WORD),
    )


class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT), ("mi", MOUSEINPUT), ("hi", HARDWAREINPUT))

    _anonymous_ = ("_input",)
    _fields_ = (("type", wintypes.DWORD), ("_input", _INPUT))


LPINPUT = ctypes.POINTER(INPUT)


def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args


user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (
    wintypes.UINT,  # nInputs
    LPINPUT,  # pInputs
    ctypes.c_int,
)  # cbSize

# Functions


def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD, ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    x = INPUT(
        type=INPUT_KEYBOARD, ki=KEYBDINPUT(wVk=hexKeyCode, dwFlags=KEYEVENTF_KEYUP)
    )
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def MoveMouse(x, y):
    x = int(x * 65535 / screenWidth)
    y = int(y * 65535 / screenHeight)

    mi = MOUSEINPUT(
        dx=x, dy=y, mouseData=0, dwFlags=0x0001 | 0x8000, time=0, dwExtraInfo=0
    )
    inp = INPUT(type=INPUT_MOUSE, mi=mi)
    user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(inp))


class InputManager(object):
    def __init__(self):
        pass

    def press(self, key: KeyTypes):
        hexKeyCode = key.value
        PressKey(hexKeyCode)

    def release(self, key: KeyTypes):
        hexKeyCode = key.value
        ReleaseKey(hexKeyCode)

    def move_mouse(self, x, y):
        MoveMouse(x, y)


if __name__ == "__main__":
    input_manager = InputManager()
    input_manager.press(KeyTypes.A)
    time.sleep(0.5)
    input_manager.release(KeyTypes.A)
    # Move mouse to position (100, 200)
    input_manager.move_mouse(100, 200)
