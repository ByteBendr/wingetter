import os
import colorama
from colorama import Fore, Style

# Color Constants
WHITE= Fore.LIGHTWHITE_EX + Style.BRIGHT
CYAN = Fore.LIGHTCYAN_EX + Style.BRIGHT
GREEN = Fore.LIGHTGREEN_EX + Style.BRIGHT
RED = Fore.LIGHTRED_EX + Style.BRIGHT
MAGENTA = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
YELLOW = Fore.LIGHTYELLOW_EX + Style.BRIGHT
BLUE = Fore.LIGHTBLUE_EX + Style.BRIGHT
RESET = Style.RESET_ALL

def is_winget_installed():
    result = os.system("where winget > nul 2>&1")
    return result == 0

def install_winget():
    print(f"\n{RESET}{WHITE}[{CYAN}info{WHITE}] Installing WinGet...{RESET}")
    os.system("powershell -Command 'Get-WindowsCapability -Online | Where-Object {$_.Name -like \"Microsoft.Windows.AppExplorer*\"} | Add-WindowsCapability -Online'")
    print(f"\n{RESET}{WHITE}[{CYAN}info{WHITE}][info] WinGet installed successfully{RESET}")

def search_and_install():
    query = input(f"\n{RESET}{WHITE}[{CYAN}>{WHITE}] Enter the software to search and install:{GREEN} ")
    print()
    os.system(f"winget search {query}")
    
    app_name = input(f"\n{RESET}{WHITE}[{CYAN}>{WHITE}] Enter the exact name of the software to install:{GREEN} ")
    print()
    os.system(f"winget install {app_name}")

def uninstall_software():
    app_name = input(f"\n{RESET}{WHITE}[{CYAN}>{WHITE}] Enter the name of the software to uninstall:{GREEN} ")
    print()
    os.system(f"winget uninstall {app_name}")
    


def main():
    os.system('cls')
    print(f'''{WHITE}\n
██╗    ██╗██╗███╗   ██╗ ██████╗ ███████╗████████╗████████╗███████╗██████╗ 
██║    ██║██║████╗  ██║██╔════╝ ██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
██║ █╗ ██║██║██╔██╗ ██║██║  ███╗█████╗     ██║      ██║   █████╗  ██████╔╝
██║███╗██║██║██║╚██╗██║██║   ██║██╔══╝     ██║      ██║   ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║ ╚████║╚██████╔╝███████╗   ██║      ██║   ███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝
==========================================================================={RESET}\n''')
    installation_status = f"{WHITE}<< [{CYAN}info{WHITE}]{GREEN} WinGet is already installed {WHITE}>>{RESET}\n" if is_winget_installed() else f"{WHITE}<< [{CYAN}info{WHITE}]{GREEN} WinGet is not installed {WHITE}>>{RESET}\n"
    print(installation_status)


    print(f"{WHITE}[{BLUE}1{WHITE}] Install WinGet{RESET}")
    print(f"{WHITE}[{BLUE}2{WHITE}] Search and install software{RESET}")
    print(f"{WHITE}[{BLUE}3{WHITE}] Uninstall software{RESET}\n")

    choice = input(f"{WHITE}[{CYAN}>{WHITE}] Enter your choice (1/2/3):{RESET}{GREEN} ")

    if choice == "1":
        install_winget()
    elif choice == "2":
        search_and_install()
    elif choice == "3":
        uninstall_software()
    else:
        print(f"\n{RESET}{WHITE}[{RED}err{WHITE}] Invalid choice. Please enter 1, 2, or 3{RESET}")

if __name__ == "__main__":
    main()
