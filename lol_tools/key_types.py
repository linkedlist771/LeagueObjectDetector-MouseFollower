from enum import Enum


class KeyTypes(Enum):
    # 字母键
    A = 0x41  # A 键
    B = 0x42  # B 键
    C = 0x43  # C 键
    D = 0x44  # D 键
    E = 0x45  # E 键
    F = 0x46  # F 键
    G = 0x47  # G 键
    H = 0x48  # H 键
    I = 0x49  # I 键
    J = 0x4A  # J 键
    K = 0x4B  # K 键
    L = 0x4C  # L 键
    M = 0x4D  # M 键
    N = 0x4E  # N 键
    O = 0x4F  # O 键
    P = 0x50  # P 键
    Q = 0x51  # Q 键
    R = 0x52  # R 键
    S = 0x53  # S 键
    T = 0x54  # T 键
    U = 0x55  # U 键
    V = 0x56  # V 键
    W = 0x57  # W 键
    X = 0x58  # X 键
    Y = 0x59  # Y 键
    Z = 0x5A  # Z 键

    # 数字键
    ZERO = 0x30  # 0 键
    ONE = 0x31  # 1 键
    TWO = 0x32  # 2 键
    THREE = 0x33  # 3 键
    FOUR = 0x34  # 4 键
    FIVE = 0x35  # 5 键
    SIX = 0x36  # 6 键
    SEVEN = 0x37  # 7 键
    EIGHT = 0x38  # 8 键
    NINE = 0x39  # 9 键

    # 数字小键盘
    NUMPAD0 = 0x60  # 小键盘 0 键
    NUMPAD1 = 0x61  # 小键盘 1 键
    NUMPAD2 = 0x62  # 小键盘 2 键
    NUMPAD3 = 0x63  # 小键盘 3 键
    NUMPAD4 = 0x64  # 小键盘 4 键
    NUMPAD5 = 0x65  # 小键盘 5 键
    NUMPAD6 = 0x66  # 小键盘 6 键
    NUMPAD7 = 0x67  # 小键盘 7 键
    NUMPAD8 = 0x68  # 小键盘 8 键
    NUMPAD9 = 0x69  # 小键盘 9 键
    MULTIPLY = 0x6A  # 小键盘 * 键
    ADD = 0x6B  # 小键盘 + 键
    SEPARATOR = 0x6C  # 小键盘分隔符(通常是 Enter 键)
    SUBTRACT = 0x6D  # 小键盘 - 键
    DECIMAL = 0x6E  # 小键盘 . 键
    DIVIDE = 0x6F  # 小键盘 / 键

    # 方向键
    LEFT = 0x25  # 左箭头键
    UP = 0x26  # 上箭头键
    RIGHT = 0x27  # 右箭头键
    DOWN = 0x28  # 下箭头键

    # 功能键
    F1 = 0x70  # F1 键
    F2 = 0x71  # F2 键
    F3 = 0x72  # F3 键
    F4 = 0x73  # F4 键
    F5 = 0x74  # F5 键
