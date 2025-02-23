import os
import json
import requests
from tqdm import tqdm  # 🔹 Import tqdm untuk progress bar
from tabulate import tabulate
from colorama import Fore, Style, init
from config import API_KEYS

# 🔹 Inisialisasi Colorama
init(autoreset=True)

def get_colored_status(status):
    """Mengembalikan status berwarna untuk terminal"""
    if status == "FOUND":
        return Fore.GREEN + status + Style.RESET_ALL
    elif status == "NOT FOUND":
        return Fore.RED + status + Style.RESET_ALL
    else:
        return Fore.YELLOW + status + Style.RESET_ALL

def scan_api_checker(identifier):
    """ Mode 5: API Checker for Username/Email """

    results = []
    table_data = []  # Untuk tampilan tabel

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

    # 🔹 Gunakan tqdm untuk menunjukkan progres scanning API
    for service, url in tqdm(api_services.items(), desc="Checking APIs", unit="API", leave=False):
        try:
            response = requests.get(url, timeout=5)
            status = "FOUND" if response.status_code == 200 else "NOT FOUND"
        except requests.RequestException:
            status = "ERROR"

        # ✅ Warna hanya untuk terminal
        status_terminal = get_colored_status(status)

        # ✅ Simpan status tanpa warna di JSON
        results.append({"Service": service, "URL": url, "Status": status})
        table_data.append([service, status_terminal])  # Tambahkan ke tabel

        # 🔹 Menampilkan hasil scanning di terminal
        print(f"{service}: {status_terminal}")

    # 🔹 Tampilkan hasil dalam tabel
    if results:
        print("\n" + tabulate(table_data, headers=["Service", "Status"], tablefmt="grid"))
    else:
        print(f"{Fore.RED}[ERROR] Tidak ada hasil ditemukan!{Style.RESET_ALL}")

    # 🔹 Simpan hasil dalam format JSON yang lebih rapi
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

    print(f"\n{Fore.GREEN}[INFO] Hasil scan API telah disimpan dalam file: {json_filename}{Style.RESET_ALL}")