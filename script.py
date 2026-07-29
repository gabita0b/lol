from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
from typing import List

from bs4 import BeautifulSoup
from datasets import load_dataset
from tqdm import tqdm
import json

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "article.md"
EDA_OUTPUT = ROOT / "eda_output.json"

THEMES = [
    "bike theft",
    "burglary",
    "battery",
    "stalking",
    "arson",
    "assault",
    "rape",
    "petty theft",
    "grand theft",
    "hate violence",
    "vehicle theft",
]

LOCATION_PATTERNS = [
    r"\b[A-Z][a-zA-Z'\-]+(?:\s+[A-Z][a-zA-Z'\-]+)*\s(?:Hall|Building|Lot|Road|Way|Drive|Center|Residences|Residence|Mall|Commons|House|Highrise|Club|Field|Course|Parking|Court|Lab|Institute|Theater)\b",
    r"\b(?:\d{1,4}\s)?[A-Z][a-zA-Z'\-]+\s(?:Avenue|Ave|Street|St|Road|Rd|Lane|Ln|Circle|Cir)\b",
]

LOCATION_RE = re.compile("|".join(f"({p})" for p in LOCATION_PATTERNS))


def collect(example: dict) -> dict:
    """Extract list items from the HTML record and plain text."""
    soup = BeautifulSoup(example.get("html", "") or "", "html.parser")
    example["items"] = [li.get_text(" ", strip=True) for li in soup.find_all("li")]
    example["text"] = soup.get_text(" ", strip=True)
    return example


def count_themes(titles: List[str], records: List[dict]) -> Counter:
    """Count occurrences of themes in titles and in items/text as a fallback."""
    counts: Counter[str] = Counter()
    lowered_titles = [t.lower() for t in titles]
    for title in lowered_titles:
        for theme in THEMES:
            if theme in title:
                counts[theme] += 1
    # also search inside items/text to capture incidents not in titles
    for r in records:
        text = (r.get("title", "") + " " + r.get("text", "")).lower()
        for theme in THEMES:
            counts[theme] += text.count(theme)
    return counts


def find_first_matching_item(records: List[dict], needle: str) -> str | None:
    n = needle.lower()
    for record in records:
        for item in record.get("items", []):
            if n in item.lower():
                return item
    return None


def clean_example(text: str | None, fallback: str) -> str:
    if not text:
        return fallback
    text = re.sub(r"\s+", " ", text).strip()
    return text.rstrip(".")


def collect_examples(records: List[dict], needles: List[str]) -> List[str]:
    examples: List[str] = []
    for needle in needles:
        examples.append(
            clean_example(
                find_first_matching_item(records, needle), f"No example found for {needle}",
            )
        )
    return examples


def extract_locations(records: List[dict]) -> Counter:
    counter: Counter[str] = Counter()
    for r in records:
        text = r.get("text", "")
        for m in LOCATION_RE.finditer(text):
            match = m.group(0)
            counter[match] += 1
        # also scan individual items
        for item in r.get("items", []):
            for m in LOCATION_RE.finditer(item):
                counter[m.group(0)] += 1
    return counter


def build_article(records: List[dict], theme_counts: Counter, locations: Counter) -> str:
    total_posts = len(records)
    avg_items = sum(len(r.get("items", [])) for r in records) / total_posts if total_posts else 0

    top_themes = theme_counts.most_common(10)
    top_locations = locations.most_common(10)

    examples = collect_examples(records, [t for t, _ in top_themes[:4]])
    example_lines = "\n".join(f"- {e}." for e in examples)

    md = [
        "# Crime at Stanford — Analytical report",
        "",
        "This report summarizes patterns seen in the Stanford Daily weekly police-blotter posts (dataset: stanforddams/daily, html config). It is a data-driven overview meant to show the most common incident themes, the campus locations that appear most often, and example incident text for context.",
        "",
        "## High-level numbers",
        f"- Posts analyzed: **{total_posts}**",
        f"- Average listed incidents per post (approx): **{avg_items:.2f}**",
        "",
        "## Top themes (by occurrences in titles and text)",
    ]

    for theme, cnt in top_themes:
        md.append(f"- **{theme}** — {cnt} occurrences")

    md += ["", "## Top locations (by simple pattern match)"]
    for loc, cnt in top_locations:
        md.append(f"- {loc} — {cnt} mentions")

    md += ["", "## Example incidents", example_lines, "", "## Notes and limitations", "- Counts use simple substring and pattern matching (not a full NLP classifier).", "- Location extraction uses heuristics and will miss or mislabel some place names.", "- Duplicates and reprints across posts are not deduplicated.", "", "## Next steps", "- Parse dates/times and build time-series of incidents.", "- Use named-entity recognition to extract and normalize locations and incident types.", "- Map incidents to campus coordinates for spatial analysis.", ""]

    return "\n".join(md)


def main() -> None:
    print("Loading dataset indexes...")
    index_ds = load_dataset("stanforddams/daily", split="train")
    print("Loading HTML records and extracting items...")
    html_ds = load_dataset("stanforddams/daily", "html", split="train")
    html_ds = html_ds.map(collect)

    records = []
    titles = []
    for meta, html in zip(index_ds, html_ds):
        records.append(
            {
                "id": meta.get("id"),
                "title": meta.get("title", "") or "",
                "items": html.get("items", []),
                "text": html.get("text", ""),
            }
        )
        titles.append(meta.get("title", "") or "")

    print("Counting themes and extracting locations...")
    theme_counts = count_themes(titles, records)
    locations = extract_locations(records)

    article = build_article(records, theme_counts, locations)
    OUTPUT.write_text(article, encoding="utf-8")

    # Save a small JSON summary for programmatic inspection
    summary = {
        "n_posts": len(records),
        "avg_items_per_post": sum(len(r.get("items", [])) for r in records) / len(records) if records else 0,
        "theme_counts": theme_counts.most_common(50),
        "top_locations": locations.most_common(50),
    }
    EDA_OUTPUT.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Wrote {OUTPUT} and {EDA_OUTPUT}")


if __name__ == "__main__":
    main()
