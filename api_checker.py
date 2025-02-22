import os
import json
import requests
from tqdm import tqdm
from tabulate import tabulate
from colorama import Fore, Style, init
from config import API_KEYS

init(autoreset=True)

def get_colored_status(status):
    if status == "FOUND":
        return Fore.GREEN + status + Style.RESET_ALL
    elif status == "NOT FOUND":
        return Fore.RED + status + Style.RESET_ALL
    else:
        return Fore.YELLOW + status + Style.RESET_ALL

def scan_api_checker(identifier):
    """ Mode 5: API Checker for Username/Email """

    results = []
    table_data = []

    api_services = {
        "Twitter": f"https://api.twitter.com/2/users/by/username/{identifier}",
        "GitHub": f"https://api.github.com/users/{identifier}",
        "Instagram": f"https://graph.instagram.com/{identifier}?access_token={API_KEYS.get('INSTAGRAM_API_KEY')}",
        "TikTok": f"https://www.tiktok.com/@{identifier}",
        "Facebook": f"https://graph.facebook.com/{identifier}?access_token={API_KEYS.get('FACEBOOK_ACCESS_TOKEN')}",
        "Discord": f"https://discord.com/api/users/{identifier}",
        "Shodan": f"https://api.shodan.io/shodan/host/search?key={API_KEYS.get('SHODAN_API_KEY')}&query={identifier}",
        "Censys": f"https://search.censys.io/api/v1/search?query={identifier}&api_id={API_KEYS.get('CENSYS_API_ID')}&api_secret={API_KEYS.get('CENSYS_API_SECRET')}",
        "ZoomEye": f"https://api.zoomeye.org/user/search?query={identifier}&access_token={API_KEYS.get('ZOOMEYE_API_KEY')}",
        "Spyse": f"https://api.spyse.com/v4/data/domain/{identifier}?api_token={API_KEYS.get('SPYSE_API_KEY')}",
        "WHOISXML": f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={API_KEYS.get('WHOISXML_API_KEY')}&domainName={identifier}&outputFormat=json",
    }

    print(f"\n{Fore.CYAN}[+] Scanning API for: {identifier} {Style.RESET_ALL}\n")

    for service, url in tqdm(api_services.items(), desc="Checking APIs", unit="API", leave=False):
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
        "identifier": identifier,
        "mode": "API Checker",
        "results": results
    }

    if not os.path.exists("results"):
        os.makedirs("results")

    json_filename = f"results/api_scan_results_{identifier}.json"
    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(json_output, json_file, indent=4)

    print(f"\n{Fore.GREEN}[INFO] The API scan results have been saved in the file: {json_filename}{Style.RESET_ALL}")
