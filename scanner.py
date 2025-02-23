import os
import json
import requests
from tqdm import tqdm
from tabulate import tabulate
from colorama import Fore, Style, init

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

# 🔹 Website List (Scan Per Kategori)
WEBSITES = {
    "Social Media": {
        "Facebook": "https://www.facebook.com/{}",
        "Twitter": "https://twitter.com/{}",
        "Instagram": "https://www.instagram.com/{}/",
        "Reddit": "https://www.reddit.com/user/{}",
        "TikTok": "https://www.tiktok.com/@{}",
        "Threads": "https://www.threads.net/@{}",
        "Pinterest": "https://www.pinterest.com/{}",
        "Snapchat": "https://www.snapchat.com/add/{}",
        "Tumblr": "https://{}.tumblr.com/",
        "VK (Russia)": "https://vk.com/{}",
        "Weibo (China)": "https://weibo.com/{}",
        "Mastodon": "https://mastodon.social/@{}",
        "Xing (Germany)": "https://www.xing.com/profile/{}",
        "Badoo": "https://badoo.com/profile/{}",
        "Taringa (Argentina)": "https://www.taringa.net/{}/",
    },
    "Gaming": {
        "Steam": "https://steamcommunity.com/id/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "Roblox": "https://www.roblox.com/users/{}/profile",
        "Xbox": "https://account.xbox.com/en-US/Profile?gamertag={}",
        "PlayStation": "https://my.playstation.com/profile/{}",
        "Epic Games": "https://www.epicgames.com/id/{}/",
        "Battle.net": "https://us.battle.net/account/management/profile-detail.xml?battleTag={}",
        "Nintendo Switch": "https://www.nintendo.com/switch/{}/",
        "RuneScape": "https://secure.runescape.com/m=hiscore/index_lite.ws?player={}",
        "Garena": "https://account.garena.com/profile/{}/",
        "Origin (EA)": "https://myaccount.ea.com/cp-ui/aboutme/index?personaId={}",
        "GOG": "https://www.gog.com/u/{}",
        "Itch.io": "https://{}.itch.io/",
    },
    "E-Commerce": {
        "Amazon": "https://www.amazon.com/s?k={}",
        "eBay": "https://www.ebay.com/usr/{}",
        "AliExpress": "https://www.aliexpress.com/wholesale?SearchText={}",
        "Shopee": "https://shopee.com/{}",
        "Lazada": "https://www.lazada.com.ph/shop/{}",
        "Walmart": "https://www.walmart.com/search?q={}",
        "Etsy": "https://www.etsy.com/shop/{}",
        "Rakuten (Japan)": "https://www.rakuten.co.jp/shop/{}",
        "Mercari (Japan)": "https://www.mercari.com/jp/u/{}/",
    },
    "Developer": {
        "GitHub": "https://github.com/{}",
        "GitLab": "https://gitlab.com/{}",
        "Stack Overflow": "https://stackoverflow.com/users/{}",
        "SourceForge": "https://sourceforge.net/u/{}/profile/",
        "Kaggle": "https://www.kaggle.com/{}",
        "Dev.to": "https://dev.to/{}",
        "Bitbucket": "https://bitbucket.org/{}/",
        "HackerRank": "https://www.hackerrank.com/{}",
        "LeetCode": "https://leetcode.com/{}/",
        "Replit": "https://replit.com/@{}",
    },
    "Crypto & Finance": {
        "Binance": "https://www.binance.com/en/userCenter/userInfo.html?username={}",
        "CoinGecko": "https://www.coingecko.com/en/coins/{}",
        "Crypto.com": "https://crypto.com/nft/profile/{}",
        "CoinMarketCap": "https://coinmarketcap.com/currencies/{}/",
        "Blockchain.com": "https://www.blockchain.com/btc/address/{}",
        "KuCoin": "https://www.kucoin.com/ucenter/usercenter?username={}",
        "OKX": "https://www.okx.com/account/userinfo/{}/",
        "Bybit": "https://www.bybit.com/user/info/{}/",
    }
}

def scan_osint(identifier, mode, category=None):
    """ Mode 1 & 3: OSINT Username & Email """
    results = []

    print(f"\n{Fore.CYAN}[+] Scanning {identifier} on websites...\n{Style.RESET_ALL}")

    # 🔹 Pilih daftar website berdasarkan kategori atau semua
    sites_to_check = WEBSITES.get(category, {}) if category else {site: url for cat in WEBSITES.values() for site, url in cat.items()}

    if not sites_to_check:
        print(f"{Fore.RED}[ERROR] Kategori tidak ditemukan atau kosong!{Style.RESET_ALL}")
        return

    for site_name, url_template in tqdm(sites_to_check.items(), desc="Checking", unit="site"):
        try:
            url = url_template.format(identifier)  # 🔹 Format URL dengan identifier
            response = requests.get(url, timeout=5)
            status = "FOUND" if response.status_code == 200 else "NOT FOUND"
        except requests.RequestException:
            status = "TIMEOUT/ERROR"

        # ✅ Warna hanya untuk terminal
        status_terminal = get_colored_status(status)

        # ✅ Simpan status tanpa warna di JSON
        results.append({
            "Category": category if category else "All",
            "Site": site_name,
            "Status": status,
            "URL": url_template.format(identifier)
        })

        # 🔹 Menampilkan hasil di terminal
        print(f"{site_name}: {status_terminal}")

    # 🔹 Tampilkan hasil dalam tabel
    if results:
        print("\n" + tabulate(results, headers="keys", tablefmt="grid"))
    else:
        print(f"{Fore.RED}[ERROR] Tidak ada hasil ditemukan!{Style.RESET_ALL}")

    # 🔹 Simpan hasil dalam format JSON yang lebih rapi
    json_output = {
        "identifier": identifier,
        "mode": "OSINT",
        "category": category if category else "All",
        "results": results
    }

    if not os.path.exists("results"):
        os.makedirs("results")

    json_filename = f"results/osint_results_{identifier}.json"
    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(json_output, json_file, indent=4)

    print(f"\n{Fore.GREEN}[INFO] Hasil scan telah disimpan dalam file: {json_filename}{Style.RESET_ALL}")