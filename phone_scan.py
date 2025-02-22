from config import API_KEYS
import os
import requests
import json
from tqdm import tqdm
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)

def get_colored_status(status):
    if status == "FOUND":
        return Fore.GREEN + status + Style.RESET_ALL
    elif status == "NOT FOUND":
        return Fore.RED + status + Style.RESET_ALL
    else:
        return Fore.YELLOW + status + Style.RESET_ALL

def scan_phone(phone_number):
    """ Mode 4: Scan Phone Number using API """
    results = []
    table_data = []

    api_services = {
        "NumVerify": f"http://apilayer.net/api/validate?access_key={API_KEYS.get('NUMVERIFY_API_KEY')}&number={phone_number}",
        "Truecaller": f"https://api4.truecaller.com/v1/search?number={phone_number}",
        "Whitepages": f"https://proapi.whitepages.com/3.0/phone?phone={phone_number}&api_key={API_KEYS.get('WHITEPAGES_API_KEY')}",
        "CallerID": f"https://api.callersmart.com/v1/phone_numbers/{phone_number}/lookup",
        "CallerSmart": f"https://api.callersmart.com/v1/phones/{phone_number}?api_key={API_KEYS.get('CALLERSMART_API_KEY')}",
        "PhoneVerify": f"https://api.phoneverify.com/lookup?number={phone_number}&apikey={API_KEYS.get('PHONEVERIFY_API_KEY')}"
    }

    print(f"\n{Fore.CYAN}[+] Scanning phone number: {phone_number}\n{Style.RESET_ALL}")

    for service, url in tqdm(api_services.items(), desc="Checking", unit="API"):
        try:
            response = requests.get(url, timeout=5)
            status = "FOUND" if response.status_code == 200 else "NOT FOUND"
        except requests.RequestException:
            status = "ERROR"

        status_terminal = get_colored_status(status)

        results.append({"Service": service, "URL": url, "Status": status})
        table_data.append([service, status_terminal])

        print(f"{service}: {status_terminal}")

    if results:
        print("\n" + tabulate(table_data, headers=["Service", "Status"], tablefmt="grid"))
    else:
        print(f"{Fore.RED}[ERROR] No results found!{Style.RESET_ALL}")

    json_output = {
        "phone_number": phone_number,
        "mode": "Phone Scan",
        "results": results
    }

    if not os.path.exists("results"):
        os.makedirs("results")

    json_filename = f"results/phone_scan_results_{phone_number}.json"
    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(json_output, json_file, indent=4)

    print(f"\n{Fore.GREEN}[INFO] The scan results have been saved in the file: {json_filename}{Style.RESET_ALL}")
