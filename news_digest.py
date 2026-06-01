import os
import wikipedia
import qrcode
import textstat
from tabulate import tabulate
from dotenv import load_dotenv

load_dotenv()
APP_NAME = os.getenv("APP_NAME", "CLI News Digest")
VERSION  = os.getenv("VERSION", "1.0.0")


def print_banner():
    print("\n" + "=" * 52)
    print(f"  {APP_NAME} v{VERSION}")
    print("=" * 52 + "\n")


# ─────────────────────────────────────────
def pick_topic(raw_query):
    wikipedia.set_lang("en")
    wikipedia.set_user_agent("CLINewsDigest/1.0 (https://github.com/mashruf99/-CLI_News_Digest_Tool)")


    suggestion = wikipedia.suggest(raw_query)
    if suggestion and suggestion.lower() != raw_query.lower():
        print(f'  Suggestion found: "{suggestion}"')
        choice = input(f'  Use "{suggestion}" instead of "{raw_query}"? [Y/n]: ').strip().lower()
        if choice in ("", "y", "yes"):
            raw_query = suggestion

   
    print(f'\n  Searching for: "{raw_query}"...')
    results = wikipedia.search(raw_query, results=6)

    if not results:
        print("  No results found. Please try a different topic.")
        return None

    
    print("\n  Related articles found:\n")
    for i, title in enumerate(results, 1):
        print(f"  [{i}] {title}")
    print(f"  [0] None of these — re-enter topic")

    # Step 4: user choice
    while True:
        raw = input("\n  Pick a number: ").strip()
        if raw == "0":
            new_query = input("  Enter new topic: ").strip()
            return pick_topic(new_query) if new_query else None
        if raw.isdigit() and 1 <= int(raw) <= len(results):
            return results[int(raw) - 1]
        print(f"  Please enter a number between 0 and {len(results)}.")


# ─────────────────────────────────────────
def fetch_page(topic):
    """Wikipedia page fetching function. Returns dict or None."""
    try:
        page    = wikipedia.page(topic, auto_suggest=False)
        summary = wikipedia.summary(topic, sentences=5, auto_suggest=False)
        return {
            "title":      page.title,
            "summary":    summary,
            "url":        page.url,
            "categories": page.categories[:5],
        }
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"\n  Multiple meanings found for \"{topic}\".")
        options = e.options[:10]
        for i, opt in enumerate(options, 1):
            print(f"  [{i}] {opt}")
        while True:
            raw = input("\n  Pick a number: ").strip()
            if raw.isdigit() and 1 <= int(raw) <= len(options):
                return fetch_page(options[int(raw) - 1])
            print(f"  Please enter a number between 1 and {len(options)}.")
    except wikipedia.exceptions.PageError:
        print(f'\n  Page not found for "{topic}". Try picking another from the list.')
        return None


# ─────────────────────────────────────────
def readability(text):
    flesch = textstat.flesch_reading_ease(text)
    grade  = textstat.flesch_kincaid_grade(text)
    words  = textstat.lexicon_count(text)
    sents  = textstat.sentence_count(text)

    if flesch >= 70:   level = "Easy"
    elif flesch >= 50: level = "Medium"
    else:              level = "Hard"

    return {
        "Flesch Score": f"{flesch:.1f}",
        "Grade Level":  f"{grade:.1f}",
        "Word Count":   words,
        "Sentences":    sents,
        "Difficulty":   level,
    }


# ─────────────────────────────────────────
def display_table(data, headers=("Metric", "Value")):
    rows = [[k, v] for k, v in data.items()]
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))


def display_article_table(result):
    short = (result["summary"][:220] + "...") if len(result["summary"]) > 220 else result["summary"]
    data  = {
        "Title":      result["title"],
        "Summary":    short,
        "URL":        result["url"],
        "Categories": ", ".join(result["categories"][:3]),
    }
    rows = [[k, v] for k, v in data.items()]
    print(tabulate(rows, headers=["Field", "Details"], tablefmt="fancy_grid", maxcolwidths=[12, 58]))


# ─────────────────────────────────────────
def generate_qr(url, title):
    filename = title.replace(" ", "_").replace("/", "-")[:60] + "_qr.png"
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return filename


def main():
    print_banner()

    raw = input("Search topic: ").strip()
    if not raw:
        print("  No topic entered. Exiting.")
        return

    topic = pick_topic(raw)
    if not topic:
        return
    

    print(f'\n  Fetching "{topic}" from Wikipedia...\n')
    result = fetch_page(topic)
    if not result:
        return

    print("─" * 10)
    print("  ARTICLE INFORMATION")
    print("─" * 10)
    display_article_table(result)


    print("\n─" * 10)
    print("  FULL SUMMARY")
    print("─" * 10)
    print(result["summary"])


    print("\n─" * 10)
    print("  READABILITY ANALYSIS")
    print("─" * 10)
    display_table(readability(result["summary"]))


    print("\n─" * 10)
    print("  QR CODE")
    print("─" * 10)
    qr_file = generate_qr(result["url"], result["title"])
    print(f"  Saved: {qr_file}")
    print(f"  URL  : {result['url']}")

    print("\n" + "=" * 10)
    print("  Done.")
    print("=" * 10 + "\n")


if __name__ == "__main__":
    main()