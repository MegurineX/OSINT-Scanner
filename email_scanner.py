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
    if status == "VALID":
        return Fore.GREEN + status + Style.RESET_ALL
    elif status == "INVALID":
        return Fore.RED + status + Style.RESET_ALL
    else:
        return Fore.YELLOW + status + Style.RESET_ALL

def scan_email_api(email):
    """ Mode 2: Scan Email via API """
    
    results = []
    table_data = []  # Untuk tampilan tabel

    # 🔹 API yang digunakan untuk scan email
    api_services = {
        "Hunter.io": f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={API_KEYS.get('HUNTER_API_KEY')}",
        "EmailRep.io": f"https://emailrep.io/{email}",
        "FullContact": "https://api.fullcontact.com/v3/person.enrich",
        "HaveIBeenPwned": f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}",
        "IntelX": f"https://2.intelx.io/phonebook/search?k={API_KEYS.get('INTELX_API_KEY')}&term={email}",
        "Dehashed": f"https://api.dehashed.com/search?query={email}",
        "Abstract API": f"https://emailvalidation.abstractapi.com/v1/?api_key={API_KEYS.get('ABSTRACT_API_KEY')}&email={email}",
        "EmailValidator": f"https://api.email-validator.net/api/verify?EmailAddress={email}&APIKey={API_KEYS.get('EMAIL_VALIDATOR_API_KEY')}",
        "Verifalia": "https://api.verifalia.com/v2.4/email-validations",
        "Trumail": f"https://api.trumail.io/v2/lookups/json?email={email}"
    }

    print(f"\n{Fore.CYAN}[+] Checking Email via API: {email} {Style.RESET_ALL}\n")

    # 🔹 Gunakan tqdm untuk menunjukkan progres scanning API
    for service, url in tqdm(api_services.items(), desc="Checking Email APIs", unit="API", leave=False):
        try:
            headers = {}
            if service == "FullContact":
                headers = {
                    "Authorization": f"Bearer {API_KEYS.get('FULLCONTACT_API_KEY')}",
                    "Content-Type": "application/json"
                }
                response = requests.post(url, headers=headers, json={"email": email})
            elif service == "Verifalia":
                headers = {
                    "Authorization": f"Basic {API_KEYS.get('VERIFALIA_API_KEY')}",
                    "Content-Type": "application/json"
                }
                response = requests.post(url, headers=headers, json={"entries": [{"inputData": email}]})
            elif service == "Dehashed":
                headers = {
                    "Authorization": f"Basic {API_KEYS.get('DEHASHED_API_KEY')}",
                    "Content-Type": "application/json"
                }
                response = requests.get(url, headers=headers, timeout=5)
            else:
                response = requests.get(url, timeout=5)

            status = "VALID" if response.status_code == 200 else "INVALID"
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
        "identifier": email,
        "mode": "Email API Check",
        "results": results
    }

    if not os.path.exists("results"):
        os.makedirs("results")

    json_filename = f"results/email_check_{email}.json"
    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(json_output, json_file, indent=4)

    print(f"\n{Fore.GREEN}[INFO] Hasil email check telah disimpan dalam file: {json_filename}{Style.RESET_ALL}")