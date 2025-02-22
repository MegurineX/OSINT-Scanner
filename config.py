import os
from dotenv import load_dotenv

load_dotenv("configs/api_keys.env")

API_KEYS = {
    "HUNTER_API_KEY": os.getenv("HUNTER_API_KEY"),
    "EMAILREP_API_KEY": os.getenv("EMAILREP_API_KEY"),
    "FULLCONTACT_API_KEY": os.getenv("FULLCONTACT_API_KEY"),
    "HIBP_API_KEY": os.getenv("HIBP_API_KEY"),
    "INTELX_API_KEY": os.getenv("INTELX_API_KEY"),
    "DEHASHED_API_KEY": os.getenv("DEHASHED_API_KEY"),
    "ABSTRACT_API_KEY": os.getenv("ABSTRACT_API_KEY"),
    "EMAIL_VALIDATOR_API_KEY": os.getenv("EMAIL_VALIDATOR_API_KEY"),
    "VERIFALIA_API_KEY": os.getenv("VERIFALIA_API_KEY"),

    # 🔹 Phone Number Intelligence
    "NUMVERIFY_API_KEY": os.getenv("NUMVERIFY_API_KEY"),
    "TRUECALLER_API_KEY": os.getenv("TRUECALLER_API_KEY"),
    "WHITEPAGES_API_KEY": os.getenv("WHITEPAGES_API_KEY"),
    "CALLERSMART_API_KEY": os.getenv("CALLERSMART_API_KEY"),
    "PHONEVERIFY_API_KEY": os.getenv("PHONEVERIFY_API_KEY"),
    "CALLERID_API_KEY": os.getenv("CALLERID_API_KEY"),

    # 🔹 Social Media APIs
    "WHATSAPP_API_KEY": os.getenv("WHATSAPP_API_KEY"),
    "TELEGRAM_BOT_TOKEN": os.getenv("TELEGRAM_BOT_TOKEN"),
    "VIBER_API_KEY": os.getenv("VIBER_API_KEY"),
    "SIGNAL_API_KEY": os.getenv("SIGNAL_API_KEY"),
    "LINE_API_KEY": os.getenv("LINE_API_KEY"),
    "TWITTER_BEARER_TOKEN": os.getenv("TWITTER_BEARER_TOKEN"),
    "INSTAGRAM_API_KEY": os.getenv("INSTAGRAM_API_KEY"),
    "TIKTOK_API_KEY": os.getenv("TIKTOK_API_KEY"),
    "FACEBOOK_ACCESS_TOKEN": os.getenv("FACEBOOK_ACCESS_TOKEN"),
    "DISCORD_API_KEY": os.getenv("DISCORD_API_KEY"),

    # 🔹 OSINT / Cybersecurity APIs
    "SHODAN_API_KEY": os.getenv("SHODAN_API_KEY"),
    "ZOOMEYE_API_KEY": os.getenv("ZOOMEYE_API_KEY"),
    "CENSYS_API_ID": os.getenv("CENSYS_API_ID"),
    "CENSYS_API_SECRET": os.getenv("CENSYS_API_SECRET"),
    "GITHUB_API_KEY": os.getenv("GITHUB_API_KEY"),
    "WHOISXML_API_KEY": os.getenv("WHOISXML_API_KEY"),
    "SPYSE_API_KEY": os.getenv("SPYSE_API_KEY"),
    "EMAILVERIFY_API_KEY": os.getenv("EMAILVERIFY_API_KEY"),
}
