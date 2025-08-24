import sys
import termios
import tty

def get_keypress():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

print("Press keys (ESC to exit):")
while True:

    key = get_keypress()
    if ord(key) == 27:  # ESC key
        print("\nExiting...")
        break
    print(f"Key pressed: {key}")
