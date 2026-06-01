#  CLI News Digest

> From the command line, Wikipedia summary, readability analysis, and QR code for any topic — all in one tool.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-00ffc8?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-00ffc8?style=flat-square)]()
[![Level](https://img.shields.io/badge/Level-Beginner-ffcc00?style=flat-square)]()

---

##  Project Overview

**CLI News Digest** A Python-based command-line tool that fetches information from Wikipedia on any topic provided by the user and presents it nicely in the terminal. It also generates the article's readability score and a QR code.

This is a **Level 1 Beginner Project** — ideal for learning to use real-world Python libraries and understanding the basics of creating a CLI tool.

---

##  Product Requirements (PRD)

### Problem Statement
If you want to quickly learn about a new topic, you have to open a browser and go to Wikipedia. There is no easy tool for developers to do this from the terminal.

### Target Users
- Beginners who are learning Python.
- Developers who prefer a terminal-centric workflow.
- Anyone uses Wikipedia for quick reference.

### Goals
- [x] The Wikipedia summary can be read from the terminal
- [x] You can understand how difficult an article is by its readability score
- [x] By scanning the QR code, the complete article can be read on mobile/any other device.
- [x] Configuration can be managed using `.env` .

### Non-Goals (Outside of Scope)
- GUI/web interface is not available
- No Multiple language support  (English Wikipedia only)
- Article save/export feature নেই (v1 scope-এ)

---

##  Features

| Feature | Description | Library |
|---------|-------------|---------|
| **Wikipedia Fetch** | Brings a 5-sentence summary with the topic, URL, and categories | `wikipedia` |
| **Table Formatting** | Beautiful terminal table in `fancy_grid` format | `tabulate` |
| **QR Code** | Create and save PNG QR code from Article URL | `qrcode[pil]` |
| **Readability Score** | Flesch score, grade level, word count | `textstat` |
| **Env Management** | Keep app config in the `.env` file | `python-dotenv` |
| **Auto Disambiguation** | If there are multiple results, it auto-suggests | built-in |

---

##  Project Structure

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

##  Tech Stack

```
Python 3.8+
├── wikipedia         → Wikipedia API wrapper
├── tabulate          → Terminal table formatting
├── qrcode[pil]       → QR code generation
├── textstat          → Readability analysis
└── python-dotenv     → .env file loading
```

---

##  Installation

### Prerequisites
- Python 3.8 or above
- pip (Python package manager)
- Git

### Step 1 — Cloning 

```bash
git clone https://github.com/your-username/cli-news-digest.git
cd cli-news-digest
```

### Step 2 — Virtual Environment

```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac / Linux:
source venv/bin/activate
```

### Step 3 — Dependencies Install

```bash
pip install -r requirements.txt
```

### Step 4 — .env 

```bash
cp .env.example .env
```

`.env` Inside .env:

```env
APP_NAME=CLI News Digest
VERSION=1.0.0
```

### Step 5 — Run!

```bash
python news_digest.py
```

---

##  Usage

```
$ python news_digest.py

==================================================
  CLI News Digest v1.0
==================================================

 Which topic do you want to know about? (Write in English): Black hole

 Information is being taken from Wikipedia about 'Black hole.'..

 ARTICLE INFORMATION
╒══════════════╤════════════════════════════════════════════════════════╕
│ Field        │ Details                                                │
╞══════════════╪════════════════════════════════════════════════════════╡
│ Title        │ Black hole                                             │
│ Summary      │ A black hole is a region of spacetime where gravity... │
│ URL          │ https://en.wikipedia.org/wiki/Black_hole               │
│ Categories   │ Black holes, General relativity, Gravity               │
╘══════════════╧════════════════════════════════════════════════════════╛

 READABILITY ANALYSIS
╒══════════════════╤══════════╕
│ Metric           │ Value    │
╞══════════════════╪══════════╡
│ Flesch Score     │ 38.4     │
│ Grade Level      │ 13.2     │
│ Word Count       │ 203      │
│ Sentences        │ 9        │
│ Difficulty       │ Hard     │
╘══════════════════╧══════════╛

 QR CODE GENERATION
 QR Code created successfully: Black_hole_qr.png
 Article URL: https://en.wikipedia.org/wiki/Black_hole

==================================================
 Done! If you scan the QR code, it will go directly to the article।
==================================================
```

---

##  requirements.txt

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
- [ ] Search history preserve

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

MIT License — Details [LICENSE](LICENSE) ।

---

##  Author

**Your Name**
- GitHub: [@mashruf99](https://github.com/mashruf99)

---

> _"The best tool is the one you actually use."_