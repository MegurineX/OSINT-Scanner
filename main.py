import os
import time
from scanner import scan_osint
from phone_scan import scan_phone
from api_checker import scan_api_checker
from email_scanner import scan_email_api
from colorama import Fore, Style, init
import pyfiglet

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

init(autoreset=True)

CYAN = Fore.CYAN
PINK = Fore.MAGENTA
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL

def print_banner():
    clear_terminal()
    ascii_banner = pyfiglet.figlet_format("MegurineX", font="slant")
    
    banner_lines = ascii_banner.split("\n")
    for i, line in enumerate(banner_lines):
        print(CYAN + line if i % 2 == 0 else PINK + line)
        time.sleep(0.05)

    print(YELLOW + "=" * 50)
    print(YELLOW + " GitHub   : https://github.com/MegurineX")
    print(YELLOW + " Telegram : https://t.me/MegurineChan")
    print(YELLOW + " Email    : ariefrhmns02@gmail.com")
    print(YELLOW + "=" * 50 + RESET)

def main():
    print_banner()

    while True:
        print(f"{CYAN}          🔍 OSINT SCANNER MENU 🔍{RESET}")
        print(YELLOW + "=" * 50)
        print("1. Username Scan")
        print("2. Email Scan")
        print("3. Phone Number Scan")
        print("99. Exit")
        print(YELLOW + "=" * 50 + RESET)
        
        choice = input("\nInput options (1-3, 99 for exit): ").strip()

        if choice == "99":
            print("\n[INFO] Exit the program, thank you for using this tool - MegurineX")
            break
        elif choice not in ["1", "2", "3"]:
            print(f"{Fore.RED}[ERROR] Invalid choice!{Style.RESET_ALL}")
            time.sleep(1)
            continue

        identifier = input("\nEnter the data you want to search for: ").strip()

        clear_terminal()
        print_banner()
        print("\n" + YELLOW + "=" * 50)
        print(f"{CYAN}          🔍 SELECT SCAN MODE 🔍{RESET}")
        print(YELLOW + "=" * 50)
        print("1. All Websites (Username/Email)")
        print("2. Check Email (Using API)")
        print("3. Categories (Scan using category)")
        print("4. Phone Number (Using API)")
        print("5. API Checker (Username/Email)")
        print("0. Back")
        print(YELLOW + "=" * 50 + RESET)

        mode = input("\nEnter options (0-5): ").strip()

        if mode == "0":
            continue

        category = None
        if mode == "3":
            clear_terminal()
            print_banner()
            print("\n" + YELLOW + "=" * 50)
            print(f"{CYAN}          📂 SELECT CATEGORY 📂{RESET}")
            print(YELLOW + "=" * 50)
            print("1. Social Media")
            print("2. Gaming")
            print("3. E-Commerce")
            print("4. Developer")
            print("5. Crypto & Finance")
            print("0. Back")
            print(YELLOW + "=" * 50 + RESET)

            cat_choice = input("\nEnter options (0-5): ").strip()

            if cat_choice == "0":
                continue

            categories = {
                "1": "Social Media",
                "2": "Gaming",
                "3": "E-Commerce",
                "4": "Developer",
                "5": "Crypto & Finance"
            }
            category = categories.get(cat_choice)

        clear_terminal()
        print_banner()
        if mode == "1" or mode == "3":
            scan_osint(identifier, mode, category)
        elif mode == "2":
            scan_email_api(identifier)  # Email API Mode
        elif mode == "4":
            scan_phone(identifier)  # Phone Scan mode
        elif mode == "5":
            scan_api_checker(identifier)  # API Checker mode
        else:
            print(f"{Fore.RED}[ERROR] Invalid choice!{Style.RESET_ALL}")

        input("\nPress ENTER to return to the main menu...")
        clear_terminal()
        print_banner()

if __name__ == "__main__":
    main()
