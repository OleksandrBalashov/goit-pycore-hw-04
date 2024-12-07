import sys
from pathlib import Path
from colorama import init, Fore, Style

def get_directories(path, divider = ''):
    if not path.is_dir():
        print(Fore.RED + 'Invalid path')
        return

    try:
        for item in path.iterdir():
            if item.is_dir():
                print(Fore.GREEN + f"{divider}📂 {item.name}")
                get_directories(item, divider + '  ')
            else:
                print(Fore.BLUE + f"{divider}📜 {item.name}")
    except Exception as e:
        print(Fore.RED + f"{divider}Error: {e}")


def main():
    init(autoreset=True)

    if len(sys.argv) > 2:
        print(Fore.RED + 'Please enter a path' + Style.RESET_ALL)
        return

    path = Path(sys.argv[1])
    get_directories(path)



if __name__ == "__main__":
    main()