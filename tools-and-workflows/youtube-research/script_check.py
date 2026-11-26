"""Check a voiceover script. Measures, does not judge taste. (License: see LICENSE-varg next to this file.)

Parts are marked by "## Part ..." headings or "=== PART ... ===" lines. Text before the first part heading is ignored.
Optional: put your locked last line in youtube-studio/brand/outro.txt and the checker makes sure the script ends with it.

Usage: python tools-and-workflows/youtube-research/script_check.py <script.md|.txt> [--wpm 150] [--short]
  --short   reel/short: hook must be clear in the first ~8 words, no YouTube rehook check.
Exit code 1 when any check FAILs. Warnings are things to look at, not orders: your own words win.
"""
import re
import sys

AI_TELLS = [
    "delve", "tapestry", "testament to", "in today's fast-paced", "in today's world", "ever-evolving",
    "game-changer", "game changer", "revolutionize", "unlock the power", "unleash", "elevate your",
    "seamless", "seamlessly", "cutting-edge", "next level", "take it to the next level", "look no further",
    "whether you're", "imagine a world", "buckle up", "let's dive in", "dive into", "without further ado",
    "it's not just", "isn't just", "more than just", "the best part?", "here's the thing", "picture this",
    "say goodbye to", "say hello to", "transform the way", "embark", "journey", "realm", "landscape",
    "great question", "you're absolutely right", "supercharge", "harness", "leverage", "robust",
    "crucial", "pivotal", "let that sink in", "this changes everything",
]
NOT_X_ITS_Y = re.compile(
    r"\b(it's|it is|this is|that's|this isn't|it isn't|that isn't)\s+(not\s+)?(just\s+|only\s+)?"
    r"(a |an |the )?[\w' -]{1,30}[.,;:—–-]+\s*(it's|it is|this is|that's)\b")
WEAK_OPENERS = ["hey guys", "hi guys", "welcome back", "in this video", "today we're going to",
                "today i'm going to", "have you ever wondered", "did you know", "hello everyone", "what's up"]
import os
_OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "youtube-studio", "brand", "outro.txt")
OUTRO_LINE = open(_OUT, encoding="utf-8").read().strip().lower().replace(",", "") if os.path.exists(_OUT) else ""


def load(path):
    text = open(path, encoding="utf-8").read()
    parts, cur, started = [], None, False
    for line in text.splitlines():
        s = line.strip()
        head = re.match(r"^(##\s+(.+)|===\s*(.+?)\s*===)$", s)
        if head:
            started = True
            cur = {"name": (head.group(2) or head.group(3)).strip(), "lines": []}
            parts.append(cur)
            continue
        if not started or not s or s == "---" or s.startswith("#") or s.startswith(">"):
            continue
        cur["lines"].append(s)
    if not parts:  # plain text, no headings: one part
        parts = [{"name": "script", "lines": [l.strip() for l in text.splitlines() if l.strip()]}]
    return parts


def clean(s):
    s = re.sub(r"<break[^>]*/>", " ", s)
    s = re.sub(r"\[[^\]]*\]", " ", s)           # [proof: ...] editor notes
    return s.replace("…", ", ").replace("’", "'").replace("“", '"').replace("”", '"')


def words(s):
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9'%$.:-]*", clean(s))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    args = sys.argv[1:]
    wpm = float(args[args.index("--wpm") + 1]) if "--wpm" in args else 150.0
    short = "--short" in args
    parts = load(args[0])
    res = []

    def add(level, check, msg):
        res.append((level, check, msg))

    # pace: where each part starts, so we can see the 2-3 min rehook point
    t, timeline = 0.0, []
    for p in parts:
        n = sum(len(words(l)) for l in p["lines"])
        timeline.append((t, p["name"], n))
        t += n / wpm * 60
    total = t

    all_lines = [(p["name"], l) for p in parts for l in p["lines"]]
    if not all_lines:
        add("FAIL", "script", "no spoken lines found")
    else:
        first = clean(all_lines[0][1]).lower().strip(' "')
        for o in WEAK_OPENERS:
            if first.startswith(o):
                add("FAIL", "hook", f"opens with '{o}': start on the result, the surprise or the problem")
        if short and len(words(all_lines[0][1])) > 12:
            add("WARN", "hook", f"first line is {len(words(all_lines[0][1]))} words; a reel hook should land in ~8")

    for name, line in all_lines:
        low = clean(line).lower()
        for p in AI_TELLS:
            if re.search(r"\b" + re.escape(p) + r"\b", low):
                add("WARN", "ai-tell", f"[{name}] '{p}': say the concrete thing instead")
        if NOT_X_ITS_Y.search(low):
            add("WARN", "ai-tell", f"[{name}] \"it's not X, it's Y\" shape: just say Y")
        for s in re.split(r"[.!?]+", clean(line)):
            n = len(s.split())
            if n > 25:
                add("WARN", "ear", f"[{name}] {n}-word sentence, split it for the ear: '{s.strip()[:60]}...'")
        if re.search(r"\b\d[\d,.]*\s?(%|x\b|percent|million|billion|k\b)|\$\d", low):
            add("INFO", "claim", f"[{name}] number claim, check it is true and shown on screen: '{line[:60]}'")

    spoken = " ".join(clean(l) for _, l in all_lines)
    n_then = len(re.findall(r"\band then\b", spoken, re.I))
    if n_then >= 2:
        add("WARN", "flow", f"'and then' x{n_then}: link beats with 'but' or 'so', not 'and then'")

    if not short and total > 180:
        tease = re.search(r"\b(later|at the end|in a second|coming up|wait till|but first|the best part)\b", spoken, re.I)
        if not tease:
            add("WARN", "rehook", "long video with no tease of what's coming (e.g. 'at the end…'); add one near the hook or at 2-3 min")

    tail = clean(" ".join(l for _, l in all_lines[-3:])).lower()
    if OUTRO_LINE and OUTRO_LINE not in re.sub(r"\s+", " ", tail.replace(",", "")):
        add("FAIL", "outro", f"last lines don't end with your outro line from youtube-studio/brand/outro.txt: '{OUTRO_LINE}'")

    print(f"Spoken: {sum(len(words(l)) for _, l in all_lines)} words, ~{int(total // 60)}:{int(total % 60):02d} at {wpm:.0f} wpm")
    for start, name, n in timeline:
        print(f"  {int(start // 60)}:{int(start % 60):02d}  {name}  ({n} words)")
    print()
    for level, check, msg in res:
        print(f"{level:4} {check:8} {msg}")
    fails = sum(1 for r in res if r[0] == "FAIL")
    print(f"\n{fails} fail, {sum(1 for r in res if r[0] == 'WARN')} warn")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
