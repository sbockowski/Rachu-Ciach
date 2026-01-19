import sys
from cli.handlers import DISPATCHER

def main():
    if len(sys.argv) < 2:
        print("Please enter a command.")
        print("Available commands:", ", ".join(DISPATCHER.keys()))
        return

    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd not in DISPATCHER:
        print(f"Unknown command: {cmd}")
        return

    # wywołujemy handler z przekazanymi argumentami
    DISPATCHER[cmd](*map(convert_arg, args))  # mapujemy np. int/float/str

def convert_arg(arg):
    # prosta heurystyka do konwersji liczb
    try:
        if '.' in arg:
            return float(arg)
        else:
            return int(arg)
    except ValueError:
        return arg  # pozostawiamy stringi

if __name__ == "__main__":
    main()