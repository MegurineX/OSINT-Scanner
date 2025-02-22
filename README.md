# 🔍 OSINT Scanner 🔍 - MegurineX

![OSINT Scanner](https://img.shields.io/badge/OSINT-Scanner-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![License](https://img.shields.io/github/license/MegurineX/OSINT-Scanner)

**An Advanced OSINT Scanner for Usernames, Emails, Phone Numbers & APIs** 🔍  
Designed for ethical researchers & cybersecurity professionals.  

---

## 📜 **Features**

✅ Scan **Usernames, Emails, and Phone Numbers**.  
✅ **API-based** verification for emails & phone numbers.  
✅ **Multi-category OSINT scanning** (Social Media, Gaming, Developer, etc.).  
✅ **Interactive terminal UI** with colorized output and table format.  
✅ **Fast scanning with threading & optimized requests.**  
✅ **Results saved in JSON format for structured reporting.**  

---

## ⚡ **Installation**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/MegurineX/OSINT-Scanner.git
cd OSINT-Scanner
```

### 2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Setup API Keys**
  Edit api_keys.env inside **configs** folder and add your API keys
*Example:*
```
HUNTER_API_KEY=your_hunter_api_key
EMAILREP_API_KEY=your_emailrep_api_key
FULLCONTACT_API_KEY=your_fullcontact_api_key
HIBP_API_KEY=your_hibp_api_key
INTELX_API_KEY=your_intelx_api_key
DEHASHED_API_KEY=your_dehashed_api_key
ABSTRACT_API_KEY=your_abstract_api_key
EMAIL_VALIDATOR_API_KEY=your_email_validator_api_key
VERIFALIA_API_KEY=your_verifalia_api_key
```

---

## 🚀 **Usage**

### **Run the script:**
```bash
python main.py
```

### Then, select a *scan mode*:
```
1. Username Scan
2. Email Scan
3. Phone Number Scan
99. Exit
```

---

## 📌 **Example: Scanning a username**

```bash
python main.py
```
```bash
Enter username: MegurineX
Select Scan Mode:
1. All Websites
2. API Checker
3. Category-based Scan
```

---

## 📂 **JSON Output Example**

All scan results are saved in the results/ directory.

  Example file: results/osint_results_MegurineX.json
```
{
    "identifier": "MegurineX",
    "mode": "OSINT",
    "category": "Developer",
    "results": [
        {
            "Category": "Developer",
            "Site": "GitHub",
            "Status": "FOUND",
            "URL": "https://github.com/MegurineX"
        },
        {
            "Category": "Developer",
            "Site": "GitLab",
            "Status": "NOT FOUND",
            "URL": "https://gitlab.com/MegurineX"
        },
```

---

## ⚒️ **Supported Websites**
OSINT Scanner can check 100+ websites (*Will add more sites on future update*)
including:

• **Social Media:** Facebook, Twitter, Instagram, Reddit, TikTok, etc.

• **Gaming Platform:** Steam, Twitch, Xbox, PlayStation, etc.

• **E-Commerce:** Amazon, eBay, Shopee, AliExpress, etc.

• **Developer Sites:** GitHub, GitLab, Stack Overflow, etc.

• **Crypto & Finance:** Binance, CoinGecko, Blockchain.com, etc.

---

## ❓ **FAQ**

### 1️⃣ *How do I add more APIs?*

  Edit api_keys.env inside **configs** folder and add your API keys.

### 2️⃣ *Can i scan without API keys?*

  Yes! **Basic scanning (Username & Emails) works without API keys.**
  However, **email & phone verification require APIs.**

### 3️⃣ *How to update the tool?*
```bash
git pull origin master
pip install -r requirements.txt
```

---

## 📝 **License**
  **This project is licensed under the MIT License.**

---

## 🤝 **Contributing**
Feel free to contribute! Fork the repo, make changes, nad create a pull request.

**•** **Author   :** MegurineX

**•** **GitHub   :** https://github.com/MegurineX

**•** **Telegram :** https://t.me/MegurineChan

**•** **Email    :** ariefrhmns123@gmail.com

---
