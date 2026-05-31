# 📟 CLI News Digest

> Command line থেকে যেকোনো topic-এ Wikipedia summary, readability analysis, এবং QR code — একটাই tool-এ।

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-00ffc8?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-00ffc8?style=flat-square)]()
[![Level](https://img.shields.io/badge/Level-Beginner-ffcc00?style=flat-square)]()

---

## 📌 Project Overview

**CLI News Digest** একটি Python-based command-line tool যা user-এর দেওয়া যেকোনো topic-এর উপর Wikipedia থেকে তথ্য এনে terminal-এ সুন্দরভাবে present করে। সাথে article-এর readability score এবং একটি QR code তৈরি করে।

এটি একটি **Level 1 Beginner Project** — Python-এর real-world library ব্যবহার শিখতে এবং CLI tool তৈরির basics বুঝতে আদর্শ।

---

## 🎯 Product Requirements (PRD)

### Problem Statement
নতুন কোনো topic সম্পর্কে দ্রুত জানতে চাইলে browser খুলে Wikipedia-তে যেতে হয়। Developer-দের জন্য terminal থেকেই এই কাজটা করার কোনো সহজ tool নেই।

### Target Users
- Python শিখছেন এমন beginners
- Terminal-centric workflow পছন্দ করেন এমন developers
- Quick reference এর জন্য Wikipedia ব্যবহার করেন এমন যেকেউ

### Goals
- [x] Terminal থেকে Wikipedia summary পড়া যাবে
- [x] Article কতটা কঠিন তা readability score দিয়ে বোঝা যাবে
- [x] QR code স্ক্যান করে মোবাইলে সম্পূর্ণ article পড়া যাবে
- [x] `.env` দিয়ে configuration manage করা যাবে

### Non-Goals (Scope বাইরে)
- GUI বা web interface নেই
- Multiple language support নেই (English Wikipedia only)
- Article save/export feature নেই (v1 scope-এ)

---

## ✨ Features

| Feature | Description | Library |
|---------|-------------|---------|
| **Wikipedia Fetch** | Topic দিয়ে 5-sentence summary, URL, categories আনে | `wikipedia` |
| **Table Formatting** | `fancy_grid` format-এ সুন্দর terminal table | `tabulate` |
| **QR Code** | Article URL থেকে PNG QR code তৈরি ও save | `qrcode[pil]` |
| **Readability Score** | Flesch score, grade level, word count | `textstat` |
| **Env Management** | App config `.env` ফাইলে রাখা | `python-dotenv` |
| **Auto Disambiguation** | Multiple results হলে auto-suggest করে | built-in |

---

## 🗂️ Project Structure

```
cli-news-digest/
│
├── news_digest.py        # Main application file
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (git-ignored)
├── .env.example          # Example env file (committed)
├── .gitignore            # Files to ignore in git
└── README.md             # This file
```

---

## 🛠️ Tech Stack

```
Python 3.8+
├── wikipedia         → Wikipedia API wrapper
├── tabulate          → Terminal table formatting
├── qrcode[pil]       → QR code generation
├── textstat          → Readability analysis
└── python-dotenv     → .env file loading
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.8 বা তার উপরে
- pip (Python package manager)
- Git

### Step 1 — Clone করো

```bash
git clone https://github.com/your-username/cli-news-digest.git
cd cli-news-digest
```

### Step 2 — Virtual Environment

```bash
# তৈরি করো
python -m venv venv

# Activate করো
# Windows:
venv\Scripts\activate

# Mac / Linux:
source venv/bin/activate
```

### Step 3 — Dependencies Install

```bash
pip install -r requirements.txt
```

### Step 4 — .env ফাইল তৈরি করো

```bash
cp .env.example .env
```

`.env` ফাইলের ভেতরে:

```env
APP_NAME=CLI News Digest
VERSION=1.0.0
```

### Step 5 — Run!

```bash
python news_digest.py
```

---

## 🚀 Usage

```
$ python news_digest.py

==================================================
  CLI News Digest v1.0
==================================================

🔍 কোন topic সম্পর্কে জানতে চাও? (English-এ লেখো): Black hole

⏳ 'Black hole' সম্পর্কে Wikipedia থেকে তথ্য আনা হচ্ছে...

📰 ARTICLE INFORMATION
╒══════════════╤════════════════════════════════════════════════════════╕
│ Field        │ Details                                                │
╞══════════════╪════════════════════════════════════════════════════════╡
│ Title        │ Black hole                                             │
│ Summary      │ A black hole is a region of spacetime where gravity... │
│ URL          │ https://en.wikipedia.org/wiki/Black_hole               │
│ Categories   │ Black holes, General relativity, Gravity               │
╘══════════════╧════════════════════════════════════════════════════════╛

📊 READABILITY ANALYSIS
╒══════════════════╤══════════╕
│ Metric           │ Value    │
╞══════════════════╪══════════╡
│ Flesch Score     │ 38.4     │
│ Grade Level      │ 13.2     │
│ Word Count       │ 203      │
│ Sentences        │ 9        │
│ Difficulty       │ Hard 🔴  │
╘══════════════════╧══════════╛

📱 QR CODE GENERATION
✅ QR Code সফলভাবে তৈরি হয়েছে: Black_hole_qr.png
🔗 Article URL: https://en.wikipedia.org/wiki/Black_hole

==================================================
✨ Done! QR code স্ক্যান করলে সরাসরি article-এ যাবে।
==================================================
```

---

## 📁 requirements.txt

```txt
python-dotenv
requests
wikipedia
qrcode[pil]
tabulate
textstat
```

---

##  .env.example

```env
APP_NAME=CLI News Digest
VERSION=1.0.0
# Future API keys :
# NEWS_API_KEY=your_key_here
```

---

##  Troubleshooting

| Error | Reason | Solution |
|-------|--------|----------|
| `ModuleNotFoundError` | Package install required | `pip install -r requirements.txt` |
| `PageError` | Didn't Find The Topic | Provide the right name in English |
| `PIL not found` | Pillow missing | `pip install pillow` |
| `DisambiguationError` | Multiple results | Code auto-handle |
| `SSLError` | Internet connection issue | Check Internet  Connection |

---

## 🗺️ Roadmap

### v1.0 (Current)
- [x] Wikipedia summary fetch
- [x] Tabulate table output
- [x] QR code generation
- [x] Readability score

### v1.1 (Planned)
- [ ] Multiple language support (Bengali, Hindi)
- [ ] Summary export to `.txt` file
- [ ] Search history সংরক্ষণ

### v2.0 (Future)
- [ ] News API integration
- [ ] CLI flags support (`--lang`, `--sentences`, `--no-qr`)
- [ ] Colorized terminal output with `rich` library

---

## If you want to contribute

1. Fork the repo
2. Create a feature branch  (`git checkout -b feature/amazing-feature`)
3. Commit those changes (`git commit -m 'Add amazing feature'`)
4. Push the changes (`git push origin feature/amazing-feature`)
5. Open pull request.

---

## License

MIT License — বিস্তারিত [LICENSE](LICENSE) ফাইলে।

---

## 👤 Author

**Your Name**
- GitHub: [@mashruf99](https://github.com/mashruf99)

---

> _"The best tool is the one you actually use."_