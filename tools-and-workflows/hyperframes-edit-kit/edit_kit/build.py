# Edit kit: build engine. Resolves <video>/shots.py against the voice's word timings and writes one HyperFrames
# composition per section + project/index.html, in the creator's look (youtube-studio/brand/design.json, see theme.py).
# usage: python tools-and-workflows/hyperframes-edit-kit/edit_kit/build.py <video folder>
#   then: cd <video>/project && npx hyperframes check && npx hyperframes render . -o ../renders/<name>_v01.mp4
# Kinds and options: tools-and-workflows/hyperframes-edit-kit/edit_kit/KINDS.md
import html as H, json, pathlib, re, subprocess, sys, importlib, math
KIT = pathlib.Path(__file__).parent; sys.path.insert(0, str(KIT))
V = pathlib.Path(sys.argv[1]).resolve(); P = V / "project"
ROOT = KIT.parent.parent.parent
STUDIO = ROOT / "youtube-studio"
sys.path.insert(0, str(V))
S = importlib.import_module("shots"); sys.modules["shots"] = S
SHOTS = S.SHOTS
from theme import Theme
TH = Theme(STUDIO)
if not TH.found:
    print("No youtube-studio/brand/design.json yet: editing in the kit's neutral default look.\n"
          "For your own colours, fonts and rules, say: build my design system (about 10 minutes).", file=sys.stderr)
REPOS = getattr(S, "REPOS", [])            # map items: [(no, name, sub), ...] for the blurred map ("hub") and topic cards ("card")
SKILLS = getattr(S, "SKILLS", []); KEEP = getattr(S, "KEEP", []); LOADS = getattr(S, "LOADS", [])
HUBLABEL = getattr(S, "HUBLABEL", "")
# map positions: given in the shots file, else spread evenly on a ring around the center
HUBXY = getattr(S, "HUBXY", None) or [(round(960 + 560 * math.sin(2 * math.pi * q / max(len(REPOS), 1))), round(540 - 360 * math.cos(2 * math.pi * q / max(len(REPOS), 1)))) for q in range(len(REPOS))]
from kinds import KIT_CSS, NEW
NUM = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "ten": "10", "twenty": "20", "thirty": "30"}
norm = lambda x: NUM.get(re.sub(r"[^a-z0-9]", "", x.lower()), re.sub(r"[^a-z0-9]", "", x.lower()))
WF = V / "audio" / ("words_tight.json" if (V / "audio" / "words_tight.json").exists() else "words.json")
VOICE = getattr(S, "VOICE", "voice_tight.wav" if (V / "audio" / "voice_tight.wav").exists() else "voice.mp3")
words = [w for s in json.loads(WF.read_text(encoding="utf8")) for w in s["words"]]
toks = [norm(w["w"]) for w in words]

def find(ph, start=0):
    want = "".join(norm(p) for p in ph.split())
    for i in range(start, len(toks)):
        got = ""
        for j in range(i, min(i + 16, len(toks))):
            got += toks[j]
            if got == want: return i
            if not want.startswith(got): break
    raise SystemExit(f"phrase not found after the previous shot: {ph!r} (copy it exactly as in {WF.name})")

pos = 0
for s in SHOTS:
    s["i"] = find(s["at"], pos); pos = s["i"] + 1; s["t"] = words[s["i"]]["s"]
VOICE_END = words[-1]["e"]
for a, b in zip(SHOTS, SHOTS[1:] + [None]):
    a["e"] = b["t"] if b else VOICE_END + 1.2
    a["w"] = words[a["i"]:(b["i"] if b else len(words))]
# big words never wait on an empty screen: a words shot starts on its first displayed word, the previous shot holds until then
for a, b in zip(SHOTS, SHOTS[1:]):
    if b["kind"] == "words":
        first = norm(b["lines"][0][0]); ft = next((w["s"] for w in b["w"] if norm(w["w"]) == first), b["t"])
        if ft - b["t"] > .35: b["t"] = a["e"] = round(ft - .05, 3)
# sections (one HyperFrames composition each): from shots.py, else a new one about every 60 s
if hasattr(S, "SECTIONS"): SECTIONS = S.SECTIONS
else:
    SECTIONS, _last = [], -99
    for x in SHOTS:
        if x["t"] - _last >= 60: SECTIONS.append((x["at"], f"part{len(SECTIONS) + 1}")); _last = x["t"]
# sections are found in order (the phrase "the first repo" also appears earlier, in "before we touch the first repo")
SEC_T, sp = [], 0
for p, _ in SECTIONS:
    i = next(x["i"] for x in SHOTS if x["i"] >= sp and "".join(norm(w) for w in x["at"].split()).startswith("".join(norm(w) for w in p.split()))); SEC_T.append(SHOTS[[x["i"] for x in SHOTS].index(i)]["t"]); sp = i + 1
SEC_T.append(SHOTS[-1]["e"])

GOLD = "#F2C200"
CSS = r'''
#root { background: #16171B; overflow: hidden; }
.glow { position: absolute; inset: 0; background: radial-gradient(ellipse 60% 55% at 92% 8%, rgba(242,194,0,.16), transparent 70%), #16171B; }
.shot { position: absolute; inset: 0; }
.goldg { background: linear-gradient(180deg, #EDE62A 0%, #E8B000 100%); -webkit-background-clip: text; background-clip: text; color: transparent; }
.card { position: absolute; left: 96px; top: 70px; width: 1728px; height: 940px; border-radius: 22px; overflow: hidden; background: #0d0e11; box-shadow: 0 50px 120px rgba(0,0,0,.7), 0 0 0 2px #2a2c33; }
.bar { position: absolute; left: 0; top: 0; right: 0; height: 56px; background: #232429; display: flex; align-items: center; padding: 0 22px; gap: 10px; }
.bar i { width: 15px; height: 15px; border-radius: 50%; display: block; }
.bar i:nth-child(1) { background: #FF5F57; } .bar i:nth-child(2) { background: #FEBC2E; } .bar i:nth-child(3) { background: #28C840; }
.bar .lb { position: absolute; left: 50%; transform: translateX(-50%); font: 500 24px "JetBrains Mono", monospace; color: #c9cacf; white-space: nowrap; }
.bar .lb b { color: #F2C200; font-weight: 700; margin-left: 26px; }
.content { position: absolute; left: 0; top: 56px; width: 1728px; height: 884px; overflow: hidden; background: #0d0e11; }
.content video, .content img { width: 100%; height: 100%; object-fit: cover; display: block; }
.mark { position: absolute; border: 5px solid #F2C200; border-radius: 12px; box-shadow: 0 0 30px rgba(242,194,0,.45); }
.words { position: absolute; left: 0; right: 0; top: 50%; transform: translateY(-50%); text-align: center; font-family: "Montserrat"; font-weight: 900; text-transform: uppercase; letter-spacing: -.03em; line-height: 1.0; color: #F4F4F2; }
.words .ln { display: block; overflow: hidden; padding: 6px 0 14px; }
.words .u { display: inline-block; margin: 0 .1em; }
.term { position: absolute; left: 190px; top: 130px; width: 1540px; height: 820px; border-radius: 22px; overflow: hidden; background: #111216; box-shadow: 0 50px 120px rgba(0,0,0,.7), 0 0 0 2px #2a2c33; }
.term .body { position: absolute; left: 0; top: 56px; right: 0; bottom: 0; padding: 50px 60px; font: 500 36px/1.6 "JetBrains Mono", monospace; color: #e6e6e3; }
.tl { position: relative; white-space: pre-wrap; margin-bottom: 26px; }
.tl .ch { opacity: 0; }
.tl.cmd::before { content: "> "; color: #F2C200; font-weight: 700; }
.tl.out { color: #9a9ba0; } .tl.err { color: #FF6B6B; } .tl.ok { color: #6EE7A0; } .tl.dim { color: #6b6c72; }
.tl.claude::before { content: "\25CF  "; color: #F4F4F2; }
.tl .ck { color: #F2C200; font-weight: 700; margin-left: 18px; }
.wall { display: flex; flex-direction: column; gap: 18px; margin-top: 10px; }
.wall i { display: block; height: 22px; border-radius: 11px; background: #3a3c43; transform-origin: 0 50%; }
.tcard { position: absolute; left: 160px; right: 160px; top: 0; bottom: 0; display: flex; flex-direction: column; justify-content: center; }
.tcard .no { font: 700 52px "JetBrains Mono", monospace; color: #F2C200; }
.tcard .nm { font: 900 150px/1.0 "Montserrat"; text-transform: uppercase; letter-spacing: -.035em; color: #F4F4F2; margin: 18px 0 30px; }
.tcard .sb { font: 500 44px "JetBrains Mono", monospace; color: #9a9ba0; }
.hubcam { position: absolute; inset: 0; }
.hubc { position: absolute; left: 790px; top: 370px; width: 340px; height: 340px; border-radius: 50%; border: 6px solid #F2C200; display: flex; flex-direction: column; align-items: center; justify-content: center; background: radial-gradient(circle, rgba(242,194,0,.14), #16171B 70%); box-shadow: 0 0 80px rgba(242,194,0,.25); }
.hubc b { font: 900 120px/0.9 "Montserrat"; color: #F2C200; } .hubc span { font: 900 34px/1.1 "Montserrat"; color: #F4F4F2; text-transform: uppercase; text-align: center; }
.hline { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; }
.pill { position: absolute; height: 100px; border-radius: 50px; padding: 0 40px; display: flex; align-items: center; gap: 22px; background: #1F2026; border: 3px solid #3a3c43; white-space: nowrap; transform: translate(-50%, -50%); }
.pill em { font: 700 34px "JetBrains Mono", monospace; font-style: normal; color: #6b6c72; } .pill b { font: 900 36px "Montserrat"; color: #F4F4F2; }
.pill.on { border-color: #F2C200; box-shadow: 0 0 50px rgba(242,194,0,.3); } .pill.on em { color: #F2C200; }
.chip { position: absolute; width: 150px; height: 56px; border-radius: 14px; background: #24262d; border: 2px solid #3a3c43; display: flex; align-items: center; gap: 10px; padding: 0 16px; font: 700 22px "JetBrains Mono", monospace; color: #8a8b91; }
.chip i { width: 22px; height: 22px; border-radius: 6px; background: #4a4c55; display: block; }
.count { position: absolute; left: 0; right: 0; top: 400px; text-align: center; font: 900 220px/1 "Montserrat"; color: #F4F4F2; text-shadow: 0 20px 60px rgba(0,0,0,.8); }
.count small { display: block; font-size: 70px; letter-spacing: -.01em; margin-top: 10px; }
.pane { position: absolute; top: 150px; width: 860px; height: 740px; border-radius: 20px; overflow: hidden; background: #0d0e11; box-shadow: 0 40px 100px rgba(0,0,0,.7), 0 0 0 2px #2a2c33; }
.pane video { width: 100%; height: 100%; object-fit: cover; display: block; }
.tag { position: absolute; top: 60px; font: 900 40px "Montserrat"; text-transform: uppercase; padding: 12px 30px; border-radius: 14px; }
.tag.g { background: linear-gradient(180deg, #EDE62A, #E8B000); color: #16171B; } .tag.r { background: #3a3c43; color: #F4F4F2; } .tag.red { background: #E5484D; color: #fff; }
.imgbox { position: absolute; border-radius: 20px; overflow: hidden; box-shadow: 0 40px 100px rgba(0,0,0,.7), 0 0 0 2px #2a2c33; background: #0d0e11; }
.imgbox img, .imgbox video { width: 100%; height: 100%; object-fit: cover; display: block; }
.cap { position: absolute; font: 500 34px "JetBrains Mono", monospace; color: #9a9ba0; text-align: center; }
.arrow { position: absolute; font: 900 120px "Montserrat"; color: #F2C200; }
.diff { position: absolute; left: 190px; top: 250px; width: 1540px; border-radius: 22px; overflow: hidden; background: #111216; box-shadow: 0 50px 120px rgba(0,0,0,.7), 0 0 0 2px #2a2c33; }
.diff .fn { height: 70px; background: #232429; font: 500 28px "JetBrains Mono", monospace; color: #c9cacf; display: flex; align-items: center; padding: 0 30px; }
.diff .dl { font: 500 38px/1 "JetBrains Mono", monospace; padding: 34px 40px; white-space: pre; }
.diff .dl.m { background: rgba(229,72,77,.16); color: #ff9a9d; } .diff .dl.p { background: rgba(110,231,160,.12); color: #8ff0b6; }
.copyc { position: absolute; left: 260px; top: 170px; width: 1400px; height: 740px; border-radius: 22px; background: #F4F4F2; color: #16171B; padding: 80px 90px; box-shadow: 0 50px 120px rgba(0,0,0,.7); font-family: "Montserrat"; }
.copyc h2 { font: 900 84px/1.05 "Montserrat"; letter-spacing: -.03em; margin: 0 0 40px; } .copyc p { font: 600 44px/1.5 "Montserrat"; color: #3a3c43; margin: 0; }
.hl { position: relative; display: inline-block; } .hl::after { content: ""; position: absolute; left: -6px; right: -6px; top: 6px; bottom: 2px; background: rgba(229,72,77,.32); border-radius: 8px; transform: scaleX(var(--s, 0)); transform-origin: 0 50%; }
.hlbox { position: absolute; background: rgba(229,72,77,.3); border-radius: 8px; transform-origin: 0 50%; }
.stk { position: absolute; left: 0; right: 0; text-align: center; font: 900 92px/1.1 "Montserrat"; letter-spacing: -.03em; }
.sline { position: absolute; height: 12px; background: #E5484D; border-radius: 6px; transform-origin: 0 50%; }
.grid2 { position: absolute; inset: 0; }
.flist { font: 500 26px/1.45 "JetBrains Mono", monospace; color: #c9cacf; padding: 110px 40px 0; }
.flist div { opacity: 0; } .flist b { color: #FF6B6B; font-weight: 700; }
.tok { position: absolute; left: 0; right: 0; bottom: 0; padding: 26px 40px; background: #1a1114; border-top: 2px solid #3a1d22; font: 700 40px "JetBrains Mono", monospace; color: #FF6B6B; }
.qlist { font: 600 40px/1.5 "Montserrat"; color: #F4F4F2; padding: 140px 50px 0; }
.qlist div { opacity: 0; margin-bottom: 34px; } .qlist em { font-style: normal; color: #F2C200; font-weight: 900; margin-right: 20px; }
.qhead { font: 500 30px "JetBrains Mono", monospace; color: #9a9ba0; padding: 0 50px; position: absolute; top: 100px; }
.obars { position: absolute; left: 160px; top: 330px; display: flex; flex-direction: column; gap: 110px; }
.orow { display: flex; flex-direction: column; gap: 22px; opacity: 0; font: 700 48px "JetBrains Mono", monospace; color: #9a9ba0; }
.otr { width: 1100px; height: 70px; border-radius: 35px; background: #24262c; overflow: hidden; }
.ofl { height: 100%; width: 100%; border-radius: 35px; transform-origin: 0 50%; background: linear-gradient(180deg, #EDE62A 0%, #E8B000 100%); }
.ofl.gr { background: #9a9ba0; }
.ogf { position: absolute; } .ogf.fr { border: 8px solid #f4f4f2; border-radius: 16px; overflow: hidden; box-shadow: 0 30px 70px rgba(0,0,0,.6); }
.ogf video { width: 100%; height: 100%; object-fit: cover; display: block; }
.odl { position: absolute; left: 130px; white-space: nowrap; font: 900 92px/1.04 "Montserrat"; text-transform: uppercase; letter-spacing: -.02em; color: #F4F4F2; }
.om { display: inline-block; overflow: hidden; vertical-align: top; padding: 0 .1em .08em; margin: 0 -.1em -.08em; } .ow { display: inline-block; }
.oend { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; }
.oln { font: 900 120px/1.02 "Montserrat"; text-transform: uppercase; letter-spacing: -.02em; color: #F4F4F2; }
.otrow { display: flex; align-items: center; gap: 60px; margin-top: 70px; }
.osw { position: relative; width: 240px; height: 120px; border-radius: 60px; background: #3a3c43; }
.oswg { position: absolute; inset: 0; border-radius: 60px; background: linear-gradient(180deg, #EDE62A, #E8B000); opacity: 0; }
.oknob { position: absolute; left: 12px; top: 12px; width: 96px; height: 96px; border-radius: 50%; background: #f4f4f2; }
.osubw { position: relative; width: 480px; height: 112px; }
.osub { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font: 900 52px "Montserrat"; border-radius: 16px; }
.cur { position: absolute; width: 60px; height: 60px; }
.esv { position: absolute; left: 160px; top: 300px; width: 960px; height: 540px; border: 3px solid #3a3c43; border-radius: 20px; }
.ess { position: absolute; left: 1330px; top: 560px; width: 300px; height: 300px; border: 3px solid #3a3c43; border-radius: 50%; }
.esv span, .ess span { position: absolute; left: 0; right: 0; bottom: -60px; text-align: center; font: 500 30px "JetBrains Mono", monospace; color: #9a9ba0; }
.esg { position: absolute; left: 1300px; top: 90px; width: 420px; height: 384px; border: 8px solid #F4F4F2; border-radius: 16px; overflow: hidden; box-shadow: 0 30px 70px rgba(0,0,0,.6); }
.esg img { width: 100%; height: 100%; object-fit: cover; display: block; }
.pk { position: absolute; top: 300px; width: 780px; height: 440px; border-radius: 30px; background: #1F2026; border: 3px solid #3a3c43; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 30px; box-shadow: 0 40px 100px rgba(0,0,0,.6); }
.pk b { font: 900 84px/1 "Montserrat"; color: #F4F4F2; letter-spacing: -.02em; } .pk span { font: 600 46px "Montserrat"; color: #9a9ba0; }
.pk.on { border-color: #F2C200; box-shadow: 0 0 70px rgba(242,194,0,.25), 0 40px 100px rgba(0,0,0,.6); } .pk.on span { color: #F2C200; }
.pkor { position: absolute; left: 930px; top: 488px; width: 60px; text-align: center; font: 700 40px "JetBrains Mono", monospace; color: #6b6c72; }
.tdd { position: absolute; left: 310px; top: 190px; width: 1300px; border-radius: 22px; background: #111216; box-shadow: 0 50px 120px rgba(0,0,0,.7), 0 0 0 2px #2a2c33; padding: 50px 60px 30px; }
.tdd .th { font: 500 34px "JetBrains Mono", monospace; color: #9a9ba0; margin-bottom: 34px; }
.tdd .tr { position: relative; font: 600 50px "JetBrains Mono", monospace; color: #ff9a9d; padding: 26px 30px 26px 110px; margin-bottom: 22px; border-radius: 16px; border: 2px solid rgba(229,72,77,.5); }
.tdd .tr em { position: absolute; left: 34px; font-style: normal; font-weight: 800; } .tdd .x { color: #E5484D; } .tdd .ok { color: #4ADE80; }
.pf { position: absolute; top: 330px; width: 680px; border-radius: 24px; background: #1F2026; border: 3px solid #3a3c43; padding: 34px 40px; box-shadow: 0 40px 100px rgba(0,0,0,.6); }
.pf.on { border-color: #F2C200; } .pn { display: flex; align-items: center; gap: 20px; font: 700 36px "JetBrains Mono", monospace; color: #F4F4F2; margin-bottom: 26px; }
.ps { display: flex; align-items: center; gap: 18px; font: 500 34px "JetBrains Mono", monospace; color: #c9cacf; margin: 14px 0 0 20px; }
.pfx { position: absolute; left: 0; right: 0; top: 90px; text-align: center; font: 900 60px "Montserrat"; color: #E5484D; text-transform: uppercase; }
.plate { position: absolute; inset: 0; background: linear-gradient(160deg, #EDE62A 0%, #E8B000 100%); }
.recslot { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 22px; background: repeating-linear-gradient(135deg, #111216 0 40px, #14151a 40px 80px); }
.recslot .rt { font: 900 120px/1 "Montserrat"; color: #F2C200; letter-spacing: -.02em; } .recslot .rr { font: 700 40px "JetBrains Mono", monospace; color: #F4F4F2; }
.recslot .rw { font: 500 30px/1.5 "JetBrains Mono", monospace; color: #9a9ba0; max-width: 1300px; text-align: center; } .recslot .rl { font: 500 24px "JetBrains Mono", monospace; color: #6b6c72; margin-top: 20px; }
.rdot { width: 34px; height: 34px; border-radius: 50%; background: #E5484D; box-shadow: 0 0 30px rgba(229,72,77,.6); }
.chipcol { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 34px; }
.chip2 { display: inline-flex; align-items: center; gap: 18px; padding: 20px 36px; border-radius: 22px; background: #1F2026; border: 2px solid #3a3c43; font: 800 44px "Montserrat"; color: #F4F4F2; white-space: nowrap; box-shadow: 0 24px 60px rgba(0,0,0,.55); }
.chip2 i { width: 20px; height: 20px; border-radius: 50%; display: block; flex: none; }
.chip2.red i { background: #E5484D; } .chip2.red { border-color: rgba(229,72,77,.55); }
.chip2.green i { background: #4ADE80; } .chip2.green { border-color: rgba(74,222,128,.5); }
.chip2.gold i { background: #F2C200; } .chip2.gold { border-color: #F2C200; }
.chip2.big { font-size: 110px; padding: 30px 70px; border-radius: 40px; } .chip2.big i { width: 44px; height: 44px; }
.fnode { position: absolute; top: 380px; width: 180px; display: flex; flex-direction: column; align-items: center; gap: 26px; }
.fbox { width: 180px; height: 180px; border-radius: 40px; background: #1F2026; border: 3px solid #3a3c43; display: flex; align-items: center; justify-content: center; box-shadow: 0 30px 70px rgba(0,0,0,.55); }
.fbox.on { border-color: #F2C200; box-shadow: 0 0 60px rgba(242,194,0,.3), 0 30px 70px rgba(0,0,0,.55); }
.flab { font: 700 32px "JetBrains Mono", monospace; color: #c9cacf; white-space: nowrap; text-align: center; }
.rcard { position: absolute; width: 230px; height: 160px; border-radius: 20px; background: #1F2026; border: 2px solid #33353d; padding: 22px; display: flex; flex-direction: column; gap: 14px; }
.rcard b { display: block; width: 70%; height: 16px; border-radius: 8px; background: #4a4c55; } .rcard i { display: block; width: 85%; height: 12px; border-radius: 6px; background: #33353d; }
.ficon { position: absolute; width: 70px; height: 70px; }
.fmap { position: absolute; left: 885px; top: 395px; width: 150px; height: 150px; }
.skwin { position: absolute; left: 260px; top: 110px; width: 1400px; height: 700px; border-radius: 22px; overflow: hidden; background: #1a1b20; box-shadow: 0 50px 120px rgba(0,0,0,.7), 0 0 0 2px #2a2c33; }
.skbody { position: absolute; left: 0; top: 56px; right: 0; bottom: 0; padding: 50px 70px; }
.skbody i { display: block; height: 18px; border-radius: 9px; background: #3a3c43; }
.sknav { display: flex; gap: 26px; margin-bottom: 70px; } .sknav i { width: 110px; height: 16px; } .sknav i:first-child { width: 160px; height: 26px; background: #55575f; margin-right: auto; }
.skhero { display: flex; flex-direction: column; gap: 18px; } .skhero i { background: #55575f; } .skhero u { display: block; width: 220px; height: 64px; border-radius: 14px; background: #6b5bd6; margin-top: 26px; }
.skhero i.rd { background: rgba(229,72,77,.55); }
.skrow { display: flex; gap: 30px; margin-top: 60px; } .skc { flex: 1; height: 150px; border-radius: 18px; background: #24262d; padding: 24px; display: flex; flex-direction: column; gap: 14px; } .skc i.sq { width: 46px; height: 46px; border-radius: 12px; background: #6b5bd6; }
.skform { width: 620px; margin: 30px auto; padding: 50px; border-radius: 24px; background: #24262d; display: flex; flex-direction: column; gap: 16px; }
.skin { height: 64px; border-radius: 14px; background: #16171B; border: 2px solid #3a3c43; } .skbtn { height: 72px; border-radius: 14px; background: #F2C200; margin-top: 18px; display: flex; align-items: center; justify-content: center; font: 900 30px "Montserrat"; color: #16171B; }
.skwall { display: flex; flex-direction: column; gap: 20px; margin-top: 150px; } .skwall i { background: #3a3c43; transform-origin: 0 50%; }
.skprompt { margin-top: 180px; } .skph { font: 700 30px "JetBrains Mono", monospace; color: #9a9ba0; margin-bottom: 20px; }
.skbox { border: 2px solid #4a4c55; border-radius: 18px; padding: 34px 36px; font: 500 40px "JetBrains Mono", monospace; color: #F4F4F2; } .skbox b { color: #F2C200; } .skbox .ch { opacity: 0; }
.skdoc { width: 760px; margin: 10px auto; padding: 50px; border-radius: 20px; background: #24262d; display: flex; flex-direction: column; gap: 22px; position: relative; } .sklock { position: absolute; right: 40px; top: 40px; }
.skcode > div { display: flex; align-items: center; gap: 24px; height: 50px; } .skcode em { font: 500 24px "JetBrains Mono", monospace; color: #55575f; width: 30px; font-style: normal; } .skcode i.g { background: #F2C200; opacity: .8; }
.skeye { position: absolute; right: 110px; top: 120px; }
.skchips { position: absolute; left: 0; right: 0; top: 760px; display: flex; justify-content: center; gap: 30px; }
.msite { background: #0f1013; } .mnav { display: flex; align-items: center; gap: 30px; padding: 40px 70px; } .mnav b { font: 900 34px "Montserrat"; color: #F4F4F2; letter-spacing: .1em; margin-right: auto; }
.mnav i { width: 100px; height: 14px; border-radius: 7px; background: #3a3c43; display: block; } .mnav u { width: 150px; height: 46px; border-radius: 12px; background: #F2C200; display: block; }
.mhero { position: absolute; left: 90px; top: 300px; display: flex; flex-direction: column; gap: 18px; } .mhero i { display: block; border-radius: 12px; background: #F4F4F2; } .mhero u { display: block; width: 220px; height: 70px; border-radius: 14px; background: #F2C200; margin-top: 30px; }
.mmodel { position: absolute; right: 70px; top: 120px; width: 820px; height: 640px; border-radius: 30px; overflow: hidden; background: #eceeed; } .mmodel img { width: 100%; height: 100%; object-fit: contain; }
.mtag { position: absolute; right: 90px; bottom: 30px; font: 500 24px "JetBrains Mono", monospace; color: #9a9ba0; }
'''

# ---- reference look: light page, dark ink, accent; dark windows stay dark
CSS += r'''
#root { background: #F5F4EE; }
.glow { background: radial-gradient(ellipse 60% 55% at 92% 8%, rgba(242,194,0,.20), transparent 70%), radial-gradient(ellipse 50% 45% at 6% 96%, rgba(217,119,87,.08), transparent 70%), #F5F4EE; }
.goldg { background: linear-gradient(180deg, #E8B000 0%, #B98500 100%); -webkit-background-clip: text; background-clip: text; color: transparent; }
.words { color: #1F1E1D; }
.tcard .nm { color: #1F1E1D; } .tcard .sb { color: #73726C; } .tcard .no { color: #B98500; }
.hubc { background: radial-gradient(circle, rgba(242,194,0,.22), #F5F4EE 72%); box-shadow: 0 0 80px rgba(242,194,0,.28); }
.hubc b { color: #C99A00; } .hubc span { color: #1F1E1D; }
.hline line { stroke: #DAD6CB; }
.pill { background: #FFFFFF; border-color: #E3DFD4; box-shadow: 0 10px 30px rgba(31,30,29,.06); }
.pill em { color: #A3A199; } .pill b { color: #1F1E1D; }
.pill.on { border-color: #F2C200; box-shadow: 0 0 50px rgba(242,194,0,.35); } .pill.on em { color: #B98500; }
.pill.bl b { filter: blur(11px); }
.chip2 { background: #FFFFFF; border-color: #E3DFD4; color: #1F1E1D; box-shadow: 0 18px 44px rgba(31,30,29,.08); }
.chip2.gold { border-color: #F2C200; }
.fbox { background: #FFFFFF; border-color: #E3DFD4; box-shadow: 0 24px 60px rgba(31,30,29,.08); }
.fbox.on { border-color: #F2C200; box-shadow: 0 0 60px rgba(242,194,0,.35), 0 24px 60px rgba(31,30,29,.08); }
.flab { color: #1F1E1D; }
.pk { background: #FFFFFF; border-color: #E3DFD4; box-shadow: 0 30px 80px rgba(31,30,29,.08); } .pk b { color: #1F1E1D; } .pk span { color: #73726C; } .pk.on span { color: #B98500; }
.pf { background: #FFFFFF; border-color: #E3DFD4; box-shadow: 0 30px 80px rgba(31,30,29,.08); } .pn { color: #1F1E1D; } .ps { color: #4A4945; }
.cap { color: #73726C; } .count { color: #1F1E1D; text-shadow: none; }
.orow { color: #73726C; } .otr { background: #E7E3D8; } .odl, .oln { color: #1F1E1D; }
.osw { background: #DAD6CB; } .oknob { box-shadow: 0 4px 14px rgba(0,0,0,.18); }
.esv, .ess { border-color: #CFCBC0; } .esv span, .ess span { color: #73726C; }
.esg { border-color: #FFFFFF; box-shadow: 0 30px 70px rgba(31,30,29,.18); }
.ogf.fr { border-color: #FFFFFF; box-shadow: 0 30px 70px rgba(31,30,29,.18); }
.card, .term, .pane, .imgbox, .diff, .skwin, .tdd { box-shadow: 0 40px 100px rgba(31,30,29,.22), 0 0 0 1px rgba(31,30,29,.08); }
.pfx { color: #E5484D; } .pkor { color: #A3A199; }
.term.light { background: #FFFFFF; } .term.light .bar { background: #EFECE4; } .term.light .bar .lb { color: #1F1E1D; }
.term.light .body { color: #1F1E1D; } .term.light .tl.out { color: #73726C; }
.gifw { position: absolute; border: 10px solid #FFFFFF; border-radius: 18px; overflow: hidden; box-shadow: 0 34px 80px rgba(31,30,29,.22); background: #000; }
.gifw video { width: 100%; height: 100%; object-fit: cover; display: block; }
.gifw.bare { border: 0; background: transparent; box-shadow: none; border-radius: 0; }
.gcap { position: absolute; left: 0; right: 0; text-align: center; font: 900 70px/1.05 "Montserrat"; text-transform: uppercase; letter-spacing: -.02em; color: #1F1E1D; }
.cc { position: absolute; left: 210px; top: 90px; width: 1500px; height: 900px; border-radius: 20px; overflow: hidden; background: #1E1E1D; box-shadow: 0 50px 120px rgba(31,30,29,.35), 0 0 0 1px rgba(0,0,0,.4); font-family: "Montserrat"; }
.cc .ctop { position: absolute; left: 0; right: 0; top: 0; height: 64px; border-bottom: 1px solid #2E2E2C; display: flex; align-items: center; gap: 22px; padding: 0 26px; color: #C9C8C2; font: 500 24px "Montserrat"; }
.cc .ctop .ic { display: flex; gap: 18px; color: #8E8D87; font: 500 22px "JetBrains Mono", monospace; }
.cc .ctop .ttl { color: #E8E7E3; }
.cc .ctop .wn { margin-left: auto; display: flex; gap: 34px; color: #8E8D87; font: 400 24px "Montserrat"; }
.cc .cmsgs { position: absolute; left: 230px; right: 230px; top: 110px; bottom: 190px; display: flex; flex-direction: column; gap: 26px; }
.cc .ub { align-self: flex-end; max-width: 820px; background: #2F2F2D; border-radius: 22px; padding: 22px 30px; color: #ECECEA; font: 500 31px/1.45 "Montserrat"; }
.cc .att { display: inline-flex; align-items: center; gap: 12px; margin-bottom: 14px; padding: 10px 16px; border-radius: 14px; background: #3A3A37; color: #C9C8C2; font: 500 24px "JetBrains Mono", monospace; }
.cc .att i { width: 34px; height: 34px; border-radius: 8px; background: linear-gradient(135deg, #D97757, #F2C200); display: block; }
.cc .cl { color: #E8E7E3; font: 500 31px/1.5 "Montserrat"; position: relative; padding-left: 50px; }
.cc .cl .st { position: absolute; left: 0; top: 2px; color: #D97757; font: 700 34px "Montserrat"; display: inline-block; }
.cc .tool { color: #A3A29C; font: 500 26px/1.4 "JetBrains Mono", monospace; padding-left: 50px; position: relative; }
.cc .tool::before { content: "\25CF"; position: absolute; left: 6px; color: #6B6A65; }
.cc .tool b { color: #E8E7E3; font-weight: 700; margin-right: 14px; }
.cc .tout { margin-left: 50px; padding: 18px 24px; border-radius: 14px; background: #171716; border: 1px solid #2E2E2C; font: 500 26px/1.5 "JetBrains Mono", monospace; color: #A3A29C; white-space: pre-wrap; }
.cc .tout.er { color: #FF7B72; } .cc .tout.okk { color: #6EE7A0; }
.cc .hlm { box-shadow: 0 0 0 4px #F2C200; border-radius: 14px; }
.cc .cin { position: absolute; left: 200px; right: 200px; bottom: 74px; height: 92px; border-radius: 20px; background: #262624; border: 1px solid #3A3A38; display: flex; align-items: center; padding: 0 30px; color: #8E8D87; font: 500 30px "Montserrat"; }
.cc .cin .tx { color: #ECECEA; white-space: nowrap; overflow: hidden; max-width: 960px; } .cc .cin .tx .ch { opacity: 0; } .cc .cin .ph { position: absolute; left: 30px; }
.cc .cin .snd { margin-left: auto; width: 46px; height: 46px; border-radius: 12px; background: #3A3A38; flex: none; }
.cc .cft { position: absolute; right: 200px; bottom: 26px; color: #8E8D87; font: 500 22px "Montserrat"; }
.cc .cft b { color: #C9C8C2; font-weight: 600; }
.slopw { position: absolute; left: 260px; top: 110px; width: 1400px; height: 820px; border-radius: 20px; overflow: hidden; background: #FFFFFF; box-shadow: 0 40px 100px rgba(31,30,29,.22), 0 0 0 1px rgba(31,30,29,.08); }
.slopw .bar { background: #EFECE4; } .slopw .bar .lb { color: #1F1E1D; }
.mnode { position: absolute; padding: 18px 26px; background: #ECECFF; border: 2px solid #9370DB; border-radius: 6px; font: 500 26px "Montserrat"; color: #333; box-shadow: 8px 10px 14px rgba(0,0,0,.35); white-space: nowrap; }
.msite { background: #FFFFFF !important; } .mnav b { color: #1F1E1D !important; } .mnav i { background: #E4E1D8 !important; } .mhero i { background: #1F1E1D !important; } .mhero i.sub { background: #CFCBC0 !important; }
.mmodel { background: #E9ECEB !important; border-radius: 28px !important; overflow: hidden !important; top: 130px !important; width: 860px !important; height: 608px !important; }
.mglow { position: absolute; right: 150px; top: 170px; width: 660px; height: 660px; border-radius: 50%; background: radial-gradient(circle, #FBE7A1 0%, rgba(251,231,161,.45) 45%, rgba(255,255,255,0) 70%); }
.mtag { color: #8a877f !important; }
.imgbox.lite { box-shadow: 0 30px 80px rgba(31,30,29,.14), 0 0 0 1px rgba(31,30,29,.06); }
.sty { position: absolute; top: 230px; width: 720px; height: 470px; border-radius: 26px; overflow: hidden; box-shadow: 0 40px 100px rgba(31,30,29,.2); }
.sty.glass { background: #1d1b2e; } .blob { position: absolute; border-radius: 50%; }
.b1 { width: 380px; height: 380px; left: 40px; top: 20px; background: #7c5cff; } .b2 { width: 320px; height: 320px; right: 30px; top: 150px; background: #F2C200; } .b3 { width: 260px; height: 260px; left: 260px; top: 260px; background: #29c4e0; }
.gpanel, .mpanel { position: absolute; left: 110px; top: 95px; right: 110px; bottom: 95px; border-radius: 22px; padding: 46px; box-sizing: border-box; display: flex; flex-direction: column; gap: 18px; }
.gpanel { background: rgba(255,255,255,.16); backdrop-filter: blur(26px); -webkit-backdrop-filter: blur(26px); border: 1.5px solid rgba(255,255,255,.45); }
.gpanel i, .mpanel i { display: block; height: 30px; border-radius: 8px; background: rgba(255,255,255,.92); } .gpanel u { display: block; margin-top: auto; width: 170px; height: 52px; border-radius: 26px; background: rgba(255,255,255,.3); border: 1.5px solid rgba(255,255,255,.6); }
.sty.mini { background: #FFFFFF; border: 1px solid #E4E1D8; } .mpanel { border: 1px solid #ECE9E1; } .mpanel i { background: #1F1E1D; } .mpanel u { display: block; margin-top: auto; width: 170px; height: 52px; border-radius: 8px; background: #1F1E1D; }
.stycap { position: absolute; top: 730px; width: 720px; text-align: center; font: 700 44px "Montserrat"; color: #1F1E1D; }
.plate { background: radial-gradient(ellipse 75% 70% at 50% 48%, #FBF0CC 0%, #F5F4EE 78%); }
.cc .ub, .cc .cl { font-size: 40px; } .cc .tool, .cc .tout { font-size: 31px; } .cc .cin { font-size: 34px; } .cc .cmsgs { left: 150px; right: 150px; } .cc .ub { max-width: 1000px; } .cc .att { font-size: 28px; }
.mstamp { position: absolute; padding: 14px 34px; border: 6px solid #E5484D; border-radius: 14px; color: #E5484D; font: 900 64px "Montserrat"; text-transform: uppercase; transform: rotate(-8deg); background: rgba(255,255,255,.92); }
'''
CSS += KIT_CSS

# framed GIFs/memes: name -> (file under assets/, width, height, seconds), set in shots.py
GIFS = getattr(S, "GIFS", {})   # name -> (file under assets/, w, h, seconds)

CUR = '<svg viewBox="0 0 24 24" width="60" height="60"><path d="M4 2 L4 20 L9 15.5 L12.5 22 L15.5 20.4 L12 14 L19 14 Z" fill="#F4F4F2" stroke="#16171B" stroke-width="1.2"/></svg>'
SFX = []  # (abs t, key)
TOT = f"{len(REPOS):02d}"

ICONS = {"github": "M5 4h11a2 2 0 0 1 2 2v14H7a2 2 0 0 1-2-2z M5 18a2 2 0 0 1 2-2h11", "terminal": "M3 5h18v14H3z M7 9l3 3-3 3 M12 15h5",
         "folder": "M3 6h6l2 2h10v11H3z", "check": "M5 12l4 4 10-10", "image": "M3 5h18v14H3z M3 16l5-5 4 4 3-3 6 6 M15 9.5a1.5 1.5 0 1 0 0.01 0",
         "claude": "M12 3v18 M3 12h18 M5.6 5.6l12.8 12.8 M18.4 5.6L5.6 18.4", "cube": "M12 2l9 5v10l-9 5-9-5V7z M12 12l9-5 M12 12v10 M12 12L3 7",
         "browser": "M3 4h18v16H3z M3 9h18 M6 6.5h.01 M9 6.5h.01", "file": "M6 2h9l5 5v15H6z M15 2v5h5",
         "map": "M3 3h7v6H3z M14 15h7v6h-7z M14 3h7v6h-7z M6.5 9v9h7.5 M10 6h4", "lock": "M6 11h12v10H6z M8 11V7a4 4 0 0 1 8 0v4", "eye": "M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z M12 9a3 3 0 1 0 0.01 0"}
def icon(n, size, col="#1F1E1D"):
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="{col}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="{ICONS[n]}"/></svg>'

def sketch_ui(ui, s, I):
    """grey wireframe UI  inside a dark window: bars stand in for text, gold marks the one thing that matters."""
    if ui == "landing":
        cards = "".join('<div class="skc"><i class="sq"></i><i style="width:60%"></i><i style="width:85%"></i></div>' for _ in range(3))
        return f'<div class="sknav"><i></i><i></i><i></i><i></i></div><div class="skhero"><i style="width:620px;height:46px"></i><i style="width:500px;height:46px"></i><i style="width:380px;height:16px;margin-top:16px"></i><u></u></div><div class="skrow">{cards}</div>'
    if ui == "form":
        return '<div class="skform"><i style="width:55%;height:30px"></i><i style="width:75%;height:14px;margin-bottom:26px"></i><div class="skin"></div><div class="skin"></div><div class="skbtn">Submit</div></div>'
    if ui == "wall":
        return '<div class="skwall">' + "".join(f'<i class="wb" style="width:{w}%"></i>' for w in (96, 88, 93, 79, 91, 85, 97, 72, 90, 83, 94, 66, 89, 77)) + '</div>'
    if ui == "prompt":
        chars = "".join(f'<span class="ch">{H.escape(c)}</span>' for c in s["text"])
        return f'<div class="skprompt"><div class="skph">Claude Code</div><div class="skbox"><b>&gt;</b> <span id="{I("pt")}">{chars}</span></div></div>'
    if ui == "spec":
        return f'<div class="skdoc"><i style="width:45%;height:30px"></i>' + "".join(f'<i style="width:{w}%"></i>' for w in (90, 80, 86, 60, 92, 74)) + f'<div class="sklock">{icon("lock", 120, "#F2C200")}</div></div>'
    if ui == "code":
        rows = [(8, 30, "g"), (12, 50, ""), (12, 38, ""), (16, 44, "g"), (16, 30, ""), (12, 22, ""), (8, 12, ""), (8, 34, "g"), (12, 46, ""), (8, 10, "")]
        return '<div class="skcode">' + "".join(f'<div><em>{q + 1}</em><i style="margin-left:{a}px;width:{b}%" class="{c}"></i></div>' for q, (a, b, c) in enumerate(rows)) + '</div>'
    if ui == "reader":
        return f'<div class="sknav"><i></i><i></i><i></i><i></i></div><div class="skhero"><i class="rd" style="width:640px;height:46px"></i><i class="rd" style="width:520px;height:46px"></i><i style="width:400px;height:16px;margin-top:16px"></i></div><div class="skeye">{icon("eye", 130)}</div>'
    raise SystemExit("unknown sketch " + ui)

def vid(i, src, t0, start, dur, mstart=0.0, extra=""):
    return f'<video id="{i}" class="clip" src="assets/{src}" muted playsinline data-start="{start - t0:.3f}" data-duration="{dur:.3f}" data-media-start="{mstart:.2f}" data-track-index="2"{extra}></video>'

LIVE = getattr(S, "LIVE", None)   # optional live clip used by "screen live=True", "mocksite", "ref3d"

def build(s, k, t0):
    """returns (html, js) for one shot; times inside js are relative to the section start t0."""
    t, e = s["t"], s["e"]; d = e - t; R = lambda x: round(x - t0, 3); I = lambda n: f"s{k}{n}"; js = []; kind = s["kind"]
    clean = lambda w: norm(w)
    def W(word, fallback, nth=0):
        hits = [w["s"] for w in s["w"] if clean(w["w"]) == clean(word)] if word else []
        return hits[nth] if len(hits) > nth else fallback
    def P(x): return f"{R(max(x, t)):.3f}"
    def fx(at, name):  # a sound only where something visibly changes, so never outside this shot
        if t - .05 <= at <= e - .2: SFX.append((round(at, 3), name))
    if s.get("sfx"): fx(t, s["sfx"])
    h = ""
    if kind == "screen":
        n = s.get("n", ""); lab = H.escape(s["label"]) + (f"<b>{n}/{TOT}</b>" if n else "")
        if s.get("still"):
            inner = f'<img id="{I("im")}" src="assets/{s["src"]}" alt="" style="object-position:50% 0%" />'
            js.append(f'tl.fromTo("#{I("im")}",{{scale:1}},{{scale:1.06,duration:{d:.2f},ease:"none"}},{P(t)});')
        else:
            inner = vid(I("v"), s["src"], t0, t, d, s.get("mstart", 0), f' style="{s["vstyle"]}"' if s.get("vstyle") else "")
            if s.get("live"): inner = f'<div style="position:absolute;inset:0;background:#E9ECEB"></div>' + vid(I("v"), LIVE, t0, t, d, s.get("mstart", 0), ' style="position:absolute;inset:0;object-fit:cover;object-position:50% 22%"')
        mk = ""
        if s.get("mark"):
            x, y, w_, h_ = s["mark"]; mk = f'<div class="mark" id="{I("mk")}" style="left:{x}px;top:{y}px;width:{w_}px;height:{h_}px"></div>'
            ma = W(s.get("mark_at", ""), t + 1.0); js.append(f'gsap.set("#{I("mk")}",{{opacity:0}});tl.fromTo("#{I("mk")}",{{opacity:0,scale:1.12}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},{P(ma)});'); fx(ma, "ding_sparkle")
        h = f'<div class="plate"></div><div class="card" id="{I("c")}"><div class="bar"><i></i><i></i><i></i><span class="lb">{lab}</span></div><div class="content">{inner}{mk}</div></div>'
        js.append(f'tl.fromTo("#{I("c")}",{{y:50,opacity:0}},{{y:0,opacity:1,duration:.35,ease:"expo.out"}},{P(t)});')
        js.append(f'tl.fromTo("#{I("c")}",{{scale:.88}},{{scale:.92,duration:{d:.2f},ease:"none"}},{P(t)});')
    elif kind == "full":
        # no text on b-roll (2026-11-18): captions and stamps on full clips are dropped
        if s.get("cap") or s.get("stamp"): print(f"  ! text on b-roll dropped: {s['at']!r} (give the words their own shot)"); s.pop("cap", None); s.pop("stamp", None)
        # full-bleed clip for mood shots , no plate
        h = f'<div class="fullv" id="{I("c")}" style="position:absolute;inset:0;overflow:hidden">{vid(I("v"), s["src"], t0, t, d, s.get("mstart", 0), " style=\"position:absolute;inset:0;width:100%;height:100%;object-fit:cover\"")}</div>'
        js.append(f'tl.fromTo("#{I("c")}",{{opacity:0}},{{opacity:1,duration:.25,ease:"power1.out"}},{P(t)});')
        js.append(f'tl.fromTo("#{I("c")} video",{{scale:1}},{{scale:1.08,duration:{d:.2f},ease:"none"}},{P(t)});')
        if s.get("cap"):   # caption under a full clip , e.g. "build me a house"
            ca = W(s.get("cap_at", ""), t + .3)
            h += f'<div class="gcap" id="{I("cp")}" style="top:760px;color:#F4F4F2;text-shadow:0 6px 30px rgba(0,0,0,.7)">{H.escape(s["cap"])}</div>'
            js.append(f'gsap.set("#{I("cp")}",{{opacity:0}});tl.fromTo("#{I("cp")}",{{opacity:0,y:24}},{{opacity:1,y:0,duration:.3,ease:"expo.out"}},{P(ca)});')
        if s.get("stamp"):
            h += f'<div class="mstamp" id="{I("st")}" style="left:640px;top:420px;font-size:150px;padding:20px 60px">{H.escape(s["stamp"])}</div>'
            sa = W(s.get("stamp_at", ""), t + .35); js.append(f'gsap.set("#{I("st")}",{{opacity:0}});tl.fromTo("#{I("st")}",{{opacity:0,scale:1.8}},{{opacity:1,scale:1,duration:.25,ease:"back.out(2)"}},{P(sa)});')
    elif kind == "gif":
        # framed GIF/meme, straight ; optional caption = the creator's exact words
        f, gw, gh, gd = GIFS[s["g"]]
        if d > gd + .15: print(f"  ! GIF {s['g']} is {gd:.2f}s but its slot is {d:.2f}s ({s['at']!r})")
        cap = s.get("cap")
        if s.get("bare"): bw, bh, bx, by = 1920, 1080, 0, 0
        else:
            bh = s.get("h", 600 if cap else 720); bw = round(gw / gh * bh)
            if bw > 1300: bw = 1300; bh = round(gh / gw * bw)
            bx = (1920 - bw) // 2; by = 110 if cap else (1080 - bh) // 2
        clip = vid(I("v"), f, t0, t, d if d - gd + s.get("mstart", 0) < .35 else gd - s.get("mstart", 0), s.get("mstart", 0))
        h = f'<div class="gifw{" bare" if s.get("bare") else ""}" id="{I("g")}" style="left:{bx}px;top:{by}px;width:{bw}px;height:{bh}px">{clip}</div>'
        if cap:
            gold = s.get("gold", set())
            sp = " ".join(f'<span class="{"goldg" if w_ in gold else ""}">{H.escape(w_)}</span>' for w_ in cap.split())
            h += f'<div class="gcap" id="{I("cp")}" style="top:{by + bh + 44}px">{sp}</div>'
            js.append(f'tl.fromTo("#{I("cp")}",{{opacity:0,y:24}},{{opacity:1,y:0,duration:.3,ease:"expo.out"}},{P(t + .12)});')
        js.append(f'tl.fromTo("#{I("g")}",{{opacity:0,scale:.86}},{{opacity:1,scale:1,duration:.3,ease:"back.out(1.7)"}},{P(t)});')
    elif kind == "chat":
        # Claude Code desktop chat, dark like the real app. Lines: ("you"|"claude"|"tool"|"out"|"err"|"ok", text, cue)
        msgs = ""; last = t + .15; ty = ""
        for q, (typ, text, cue) in enumerate(s["lines"]):
            at = max(W(cue, last) if cue else last, last); lid = I(f"m{q}")
            if typ == "you":
                chars = "".join(f'<span class="ch">{H.escape(c)}</span>' for c in text); step = min(.035, 1.1 / max(len(text), 1))
                ty = f'<span class="tx" id="{I("tx")}">{chars}</span>'
                js.append(f'tl.set("#{I("ph")}",{{opacity:0}},{P(at)});document.querySelectorAll("#{I("tx")} .ch").forEach((n,q)=>tl.set(n,{{opacity:1}},{R(at):.3f}+q*{step:.3f}));')
                fx(at, "typing_short"); send = at + len(text) * step + .2
                att = f'<div class="att"><i></i>{H.escape(s["attach"])}</div><br>' if s.get("attach") else ""
                msgs += f'<div class="ub" id="{lid}">{att}{H.escape(text)}</div>'
                js.append(f'gsap.set("#{lid}",{{opacity:0}});tl.set("#{I("tx")}",{{opacity:0}},{P(send)});tl.set("#{I("ph")}",{{opacity:1}},{P(send)});tl.fromTo("#{lid}",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.3,ease:"expo.out"}},{P(send)});')
                at = send; last = send + .45
            else:
                if typ == "claude": msgs += f'<div class="cl" id="{lid}"><span class="st">&#10043;</span>{H.escape(text)}</div>'
                elif typ == "tool":
                    nm, _, rest = text.partition(": "); msgs += f'<div class="tool" id="{lid}"><b>{H.escape(nm)}</b>{H.escape(rest)}</div>'
                else: msgs += f'<div class="tout{" er" if typ == "err" else " okk" if typ == "ok" else ""}" id="{lid}">{H.escape(text)}</div>'
                js.append(f'gsap.set("#{lid}",{{opacity:0}});tl.fromTo("#{lid}",{{opacity:0,y:18}},{{opacity:1,y:0,duration:.28,ease:"power2.out"}},{P(at)});')
                if q and typ in ("claude", "err", "ok"): fx(at, "pop")
                last = at + .45
            if s.get("mark_line") == q:
                js.append(f'tl.fromTo("#{lid}",{{boxShadow:"0 0 0 0px rgba(242,194,0,0)"}},{{boxShadow:"0 0 0 5px #F2C200",duration:.3}},{P(at + .35)});')
        h = (f'<div class="cc" id="{I("c")}"><div class="ctop"><span class="ic">&#9776; &#9634; &#8249; &#8250;</span><span class="ttl">{H.escape(s.get("title", "New session"))}</span><span class="wn">&#8212; &#9634; &#10005;</span></div>'
             f'<div class="cmsgs">{msgs}</div><div class="cin"><span class="ph" id="{I("ph")}">Type / for commands</span>{ty}<span class="snd"></span></div>'
             f'<div class="cft"><b>Opus 5.5</b>&nbsp; Medium &nbsp; Auto</div></div>')
        js.append(f'tl.fromTo("#{I("c")}",{{y:50,opacity:0}},{{y:0,opacity:1,duration:.35,ease:"expo.out"}},{P(t)});tl.fromTo("#{I("c")}",{{scale:.97}},{{scale:1,duration:{d:.2f},ease:"none"}},{P(t)});')
        js.append(f'tl.to("#{I("c")} .st",{{rotation:{int(d * 120)},duration:{d:.2f},ease:"none"}},{P(t)});')
    elif kind == "rec":
        # placeholder for a recording that isn't made yet
        h = (f'<div class="plate"></div><div class="card" id="{I("c")}"><div class="bar"><i></i><i></i><i></i><span class="lb">{H.escape(s["label"])}</span></div>'
             f'<div class="content recslot"><div class="rdot" id="{I("dot")}"></div><div class="rt">RECORDING {s["no"]}</div><div class="rw">{H.escape(s["what"])}</div>'
             f'<div class="rl">your clip goes here · {d:.1f} s</div></div></div>')
        js.append(f'tl.fromTo("#{I("c")}",{{y:50,opacity:0}},{{y:0,opacity:1,duration:.35,ease:"expo.out"}},{P(t)});tl.fromTo("#{I("c")}",{{scale:.88}},{{scale:.92,duration:{d:.2f},ease:"none"}},{P(t)});')
        js.append(f'tl.fromTo("#{I("dot")}",{{opacity:1}},{{opacity:.25,duration:.6,yoyo:true,repeat:{max(int(d / .6) - 1, 1)},ease:"sine.inOut"}},{P(t)});')
    elif kind == "chips":
        big = s.get("big"); body = ""
        for q, (txt, col, cue) in enumerate(s["items"]):
            body += f'<div class="chip2 {col}{" big" if big else ""}" id="{I(f"c{q}")}"><i></i>{H.escape(txt)}</div>'
            at = t + .1 if q == 0 else W(cue, t + .2 + q * .6); js.append(f'tl.fromTo("#{I(f"c{q}")}",{{opacity:0,y:30,scale:.9}},{{opacity:1,y:0,scale:1,duration:.32,ease:"back.out(1.7)"}},{P(at - .05)});')
            if q: fx(at, "pop")
        h = f'<div class="chipcol">{body}</div>'
        for q in range(len(s["items"])): js.insert(0, f'gsap.set("#{I(f"c{q}")}",{{opacity:0}});')
    elif kind == "flow":
        items = s["items"]; n = len(items); gap = min(1240 / max(n - 1, 1), 560); x0 = 960 - gap * (n - 1) / 2; body = ""; lines = ""
        for q, (ic, lab, cue) in enumerate(items):
            x = x0 + q * gap
            body += f'<div class="fnode" id="{I(f"n{q}")}" style="left:{x - 90:.0f}px"><div class="fbox{" on" if q == n - 1 else ""}">{icon(ic, 84)}</div><div class="flab">{H.escape(lab)}</div></div>'
            if q: lines += f'<line id="{I(f"l{q}")}" x1="{x - gap + 110:.0f}" y1="470" x2="{x - 110:.0f}" y2="470" stroke="#5a5c63" stroke-width="4" stroke-dasharray="10 12"/>'
        h = f'<svg class="hline">{lines}</svg>{body}'
        last = t
        for q, (_, _, cue) in enumerate(items):
            at = max(W(cue, last + .7) if q else t + .1, last + .35 if q else t); last = at
            js.append(f'gsap.set("#{I(f"n{q}")}",{{opacity:0}});tl.fromTo("#{I(f"n{q}")}",{{opacity:0,y:30,scale:.85}},{{opacity:1,y:0,scale:1,duration:.35,ease:"back.out(1.6)"}},{P(at)});')
            if q: js.append(f'gsap.set("#{I(f"l{q}")}",{{opacity:0}});tl.fromTo("#{I(f"l{q}")}",{{opacity:0}},{{opacity:1,duration:.3}},{P(at - .2)});'); fx(at, "pop")
    elif kind == "sketch":
        ui = s["ui"]; inner = sketch_ui(ui, s, I)
        h = f'<div class="skwin" id="{I("w")}"><div class="bar"><i></i><i></i><i></i></div><div class="skbody">{inner}</div></div>'
        js.append(f'tl.fromTo("#{I("w")}",{{y:50,opacity:0}},{{y:0,opacity:1,duration:.35,ease:"expo.out"}},{P(t)});tl.fromTo("#{I("w")}",{{scale:1}},{{scale:1.03,duration:{d:.2f},ease:"none"}},{P(t)});')
        if ui == "wall": js.append(f'tl.fromTo("#{I("")} .wb",{{scaleX:0}},{{scaleX:1,duration:.22,ease:"power2.out",stagger:.1}},{P(W("wall", t + 2.5) - 1.0)});')
        if ui == "prompt":
            txt = s["text"]; step = min(.05, 1.4 / len(txt)); at = W(txt.split()[0], t + .3)
            js.append(f'document.querySelectorAll("#{I("pt")} .ch").forEach((n,q)=>tl.set(n,{{opacity:1}},{R(at):.3f}+q*{step:.3f}));')
        chips = ""
        for q, (txt, col, cue) in enumerate(s.get("chips", [])):
            chips += f'<div class="chip2 {col}" id="{I(f"c{q}")}"><i></i>{H.escape(txt)}</div>'
            at = W(cue, t + .6 + q * .8); js.append(f'gsap.set("#{I(f"c{q}")}",{{opacity:0}});tl.fromTo("#{I(f"c{q}")}",{{opacity:0,y:24,scale:.9}},{{opacity:1,y:0,scale:1,duration:.3,ease:"back.out(1.7)"}},{P(at - .05)});'); fx(at, "pop")
        if chips: h += f'<div class="skchips">{chips}</div>'
    elif kind == "words":
        size = s.get("size", 150); gold = s.get("gold", set()); n = 0; lines = ""; cands = list(s["w"]); ci = 0
        for ln in s["lines"]:
            sp = ""
            for wd in ln:
                at = None
                for q in range(ci, len(cands)):
                    if clean(cands[q]["w"]) == clean(wd): at = cands[q]["s"]; ci = q + 1; break
                if at is None: at = t + .12 * n
                wid = I(f"u{n}"); g = " goldg" if wd in gold else ""
                sp += f'<span class="u{g}" id="{wid}">{H.escape(wd)}</span>'
                js.append(f'tl.fromTo("#{wid}",{{yPercent:120}},{{yPercent:0,duration:.42,ease:"expo.out"}},{P(at - .05)});'); n += 1
            lines += f'<span class="ln">{sp}</span>'
        h = f'<div class="words" style="font-size:{size}px">{lines}</div>'
    elif kind == "term":
        body = ""; last = t + .2
        for q, (typ, text, cue) in enumerate(s["lines"]):
            at = max(W(cue, last) if cue else last, last); lid = I(f"l{q}")
            if typ == "cmd":
                chars = "".join(f"<span class=\"ch\">{H.escape(c)}</span>" for c in text); step = min(.045, 1.2 / max(len(text), 1))
                js.append(f'document.querySelectorAll("#{lid} .ch").forEach((n,q)=>tl.set(n,{{opacity:1}},{R(at):.3f}+q*{step:.3f}));')
                ck = f'<span class="ck" id="{lid}k">&#10003;</span>' if s.get("checks") else ""
                if ck: js.append(f'gsap.set("#{lid}k",{{opacity:0}});tl.fromTo("#{lid}k",{{opacity:0,scale:.4}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},{R(at + len(text) * step + .25):.3f});'); fx(at + len(text) * step + .25, "pop")
                body += f'<div class="tl cmd" id="{lid}">{chars}{ck}</div>'; last = at + len(text) * step + .4
            elif typ == "wall":
                bars = "".join(f'<i id="{lid}b{b}" style="width:{[96,88,93,79,91,85,97,72,90,83,94,66][b]}%"></i>' for b in range(12))
                js.append(f'tl.fromTo("#{lid} i",{{scaleX:0}},{{scaleX:1,duration:.25,ease:"power2.out",stagger:.12}},{P(at)});')
                body += f'<div class="wall" id="{lid}">{bars}</div>'
            else:
                body += f'<div class="tl {typ}" id="{lid}">{H.escape(text)}</div>'
                if at > t + .25: js.append(f'gsap.set("#{lid}",{{opacity:0}});tl.fromTo("#{lid}",{{opacity:0,y:14}},{{opacity:1,y:0,duration:.25,ease:"power2.out"}},{P(at)});')
                last = at + .3
            if s.get("mark_line") == q:
                js.append(f'tl.fromTo("#{lid}",{{boxShadow:"0 0 0 0 rgba(242,194,0,0)"}},{{boxShadow:"0 0 0 5px #F2C200",duration:.3}},{P(at + .4)});')
        h = f'<div class="term{" light" if s.get("light") else ""}" id="{I("c")}"><div class="bar"><i></i><i></i><i></i><span class="lb">{H.escape(s["title"])}</span></div><div class="body">{body}</div></div>'
        js.append(f'tl.fromTo("#{I("c")}",{{y:50,opacity:0}},{{y:0,opacity:1,duration:.35,ease:"expo.out"}},{P(t)});')
    elif kind == "card":
        no, nm, sub = REPOS[s["n"]]
        h = f'<div class="tcard"><div class="no" id="{I("a")}">{no} / {TOT}</div><div class="nm" id="{I("b")}">{H.escape(nm)}</div><div class="sb" id="{I("c")}">{H.escape(sub)}</div></div>'
        js.append(f'tl.fromTo(["#{I("a")}","#{I("b")}","#{I("c")}"],{{opacity:0,y:40}},{{opacity:1,y:0,duration:.4,ease:"expo.out",stagger:.12}},{P(t)});')
    elif kind == "hub":
        mode = s["mode"]; pills = ""
        for q, ((no, nm, _), (x, y)) in enumerate(zip(REPOS, HUBXY)):
            on = mode == "all" or mode == q + 1
            # names stay blurred until their section, so viewers stay to see all seven (static blur, revealed with a pop)
            hid = mode in ("intro", "tease") or s.get("keep_blur") or (isinstance(mode, int) and q + 1 >= mode)
            pills += f'<div class="pill{" on" if on else ""}{" bl" if hid else ""}" id="{I(f"p{q}")}" style="left:{x}px;top:{y}px"><em>{no}</em><b id="{I(f"pb{q}")}">{H.escape(nm)}</b></div>'
        if isinstance(mode, int) and not s.get("keep_blur"):
            # unblur the name in place (no class swap, no cut), the pill lights up gold
            rv = W(s["reveal_at"], t + .55) if s.get("reveal_at") else t + .55; pq = I(f"p{mode - 1}"); bq = I(f"pb{mode - 1}")
            js.append(f'gsap.set("#{bq}",{{filter:"blur(11px)"}});tl.to("#{bq}",{{filter:"blur(0px)",duration:.6,ease:"power2.out"}},{P(rv)});'
                      f'tl.to("#{pq}",{{borderColor:"#F2C200",boxShadow:"0 0 50px rgba(242,194,0,.35)",duration:.5}},{P(rv)});tl.to("#{pq} em",{{color:"#B98500",duration:.5}},{P(rv)});')
            fx(rv, "ding_sparkle")
        lines = "".join(f'<line x1="960" y1="540" x2="{x}" y2="{y}" stroke="#2c2e35" stroke-width="3"/>' for x, y in HUBXY)
        h = f'<div class="hubcam" id="{I("cam")}"><svg class="hline">{lines}</svg><div class="hubc" id="{I("c")}"><b>{len(REPOS)}</b><span>{HUBLABEL}</span></div>{pills}</div>'
        if mode == "tease":
            js.append(f'tl.fromTo("#{I("cam")} .pill",{{opacity:0,scale:.7}},{{opacity:1,scale:1,duration:.3,ease:"back.out(1.6)",stagger:.06}},{P(t)});')
            js.append(f'tl.fromTo("#{I("cam")}",{{scale:1.12,rotation:-2}},{{scale:1,rotation:0,duration:{d:.2f},ease:"power2.out"}},{P(t)});')
            js.append(f'tl.fromTo("#{I("c")}",{{scale:1}},{{scale:1.08,duration:.5,yoyo:true,repeat:{max(int(d / .5) - 1, 1)},ease:"sine.inOut"}},{P(t)});')
        elif mode == "intro":
            six = W("three", t + .8)
            js.append(f'tl.fromTo("#{I("c")}",{{scale:.5,opacity:0}},{{scale:1,opacity:1,duration:.45,ease:"back.out(1.6)"}},{P(t)});')
            js.append(f'tl.fromTo("#{I("cam")} .pill",{{opacity:0,scale:.6}},{{opacity:1,scale:1,duration:.35,ease:"back.out(1.6)",stagger:.09}},{P(six - .2)});')
            js.append(f'tl.fromTo("#{I("cam")}",{{scale:1}},{{scale:1.05,duration:{d:.2f},ease:"none"}},{P(t)});')
        elif mode == "all":
            js.append(f'tl.fromTo("#{I("cam")}",{{scale:1.08}},{{scale:1,duration:{min(d, 3):.2f},ease:"power2.out"}},{P(t)});')
            for q, wd in ():
                at = W(wd, None)
                if at: js.append(f'tl.fromTo("#{I(f"p{q}")}",{{scale:1}},{{scale:1.18,duration:.25,yoyo:true,repeat:1,ease:"power2.out"}},{P(at)});'); fx(at, "pop")
        else:
            x, y = HUBXY[mode - 1]; d0 = t
            if s.get("intro"):   # the map builds first ("three things"), then the camera moves to the habit
                six = W("three", t + .4); d0 = max(W(s.get("reveal_at", ""), t + 1.5) - 1.0, six + .6)
                js.append(f'tl.fromTo("#{I("c")}",{{scale:.5,opacity:0}},{{scale:1,opacity:1,duration:.45,ease:"back.out(1.6)"}},{P(t)});tl.fromTo("#{I("cam")} .pill",{{opacity:0,scale:.6}},{{opacity:1,scale:1,duration:.35,ease:"back.out(1.6)",stagger:.09}},{P(six - .2)});')
            js.append(f'gsap.set("#{I("cam")}",{{transformOrigin:"{x}px {y}px"}});tl.fromTo("#{I("cam")}",{{scale:1}},{{scale:1.45,x:{(960 - x) * .55:.0f},y:{(540 - y) * .55:.0f},duration:{max(e - d0, .8):.2f},ease:"power2.inOut"}},{P(d0)});')
            for q in range(len(REPOS)):
                if q != mode - 1: js.append(f'tl.to("#{I(f"p{q}")}",{{opacity:.22,duration:.3}},{P(d0 + .1)});')
            js.append(f'tl.to("#{I("c")}",{{opacity:.35,duration:.3}},{P(d0 + .1)});')
            fx(t + .5, "ding_sparkle") if False else None
    elif kind == "split":
        L, Rr = s["left"], s["right"]
        # fit=True : smaller panes that show the whole page, nothing cropped
        ps = ";top:250px;height:560px;background:#fff" if s.get("fit") else ""; vs = ' style="object-fit:contain"' if s.get("fit") else ""; ts = ";top:160px" if s.get("fit") else ""
        h = (f'<div class="plate"></div><div class="pane" id="{I("l")}" style="left:80px{ps}">{vid(I("lv"), L["src"], t0, t, d, L.get("mstart", 0), vs)}</div><div class="tag r" id="{I("lt")}" style="left:80px{ts}">{H.escape(L["tag"])}</div>'
             f'<div class="pane" id="{I("r")}" style="left:980px{ps}">{vid(I("rv"), Rr["src"], t0, t, d, Rr.get("mstart", 0), vs)}</div><div class="tag g" id="{I("rt")}" style="left:980px{ts}">{H.escape(Rr["tag"])}</div>')
        js.append(f'tl.fromTo(["#{I("l")}","#{I("lt")}"],{{opacity:0,x:-60}},{{opacity:1,x:0,duration:.35,ease:"expo.out"}},{P(t)});tl.fromTo(["#{I("r")}","#{I("rt")}"],{{opacity:0,x:60}},{{opacity:1,x:0,duration:.35,ease:"expo.out"}},{P(t + .25)});')
    elif kind == "film":
        items = s["items"]; seg = d / len(items)
        for q, src in enumerate(items):
            a = t + q * seg
            inner = vid(I(f"v{q}"), src, t0, a, seg) if src.endswith(".mp4") else f'<img src="assets/{src}" alt="" />'
            h += f'<div class="imgbox" id="{I(f"f{q}")}" style="left:260px;top:120px;width:1400px;height:840px">{inner}</div>'
            js.append(f'gsap.set("#{I(f"f{q}")}",{{opacity:0}});tl.fromTo("#{I(f"f{q}")}",{{opacity:0,scale:.96}},{{opacity:1,scale:1,duration:.3,ease:"expo.out"}},{P(a)});tl.set("#{I(f"f{q}")}",{{opacity:0}},{P(a + seg)});')
            if q: fx(a, "pop")
    elif kind == "pick2":
        (ln, ls, lc), (rn, rs, rc) = s["left"], s["right"]
        h = (f'<div class="pk" id="{I("l")}" style="left:150px"><b>{H.escape(ln)}</b><span>{H.escape(ls)}</span></div>'
             f'<div class="pk on" id="{I("r")}" style="left:990px"><b>{H.escape(rn)}</b><span>{H.escape(rs)}</span></div><div class="pkor">or</div>')
        la, ra = W(lc, t + .2), W(rc, t + 1.6)
        js.append(f'gsap.set(["#{I("l")}","#{I("r")}"],{{opacity:0}});tl.fromTo("#{I("l")}",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.35,ease:"expo.out"}},{P(la - .1)});tl.fromTo("#{I("r")}",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.35,ease:"expo.out"}},{P(ra - .1)});')
        fx(ra, "pop")
    elif kind in NEW:
        h, more = NEW[kind](s, t, e, d, I, W, P, R, fx, t0); js += more
    else:
        raise SystemExit("unknown kind " + kind)
    # the shot wrapper is untimed (a timed wrapper around a timed <video> breaks frame extraction): show/hide it on the timeline
    js.insert(0, f'gsap.set("#{I("")}",{{opacity:0}});tl.set("#{I("")}",{{opacity:1}},{R(t):.3f});tl.set("#{I("")}",{{opacity:0}},{R(e):.3f});')
    return f'<div id="{I("")}" class="shot">{h}</div>', js

import os
ONLY = os.environ.get("ONLY")  # e.g. ONLY=hook renders just that section, voice and sfx included
if ONLY:
    keep = [n for _, n in SECTIONS].index(ONLY); SEC_T[keep + 1] = SEC_T[keep + 1]  # boundaries unchanged
(P / "compositions").mkdir(parents=True, exist_ok=True)
import shutil as _sh
for f in ("hyperframes.json", "package.json"):
    if not (P / f).exists(): _sh.copy(KIT / "project_template" / f, P / f)
for f in ((V / "assets").rglob("*") if (V / "assets").exists() else []):
    if f.is_file():
        dst = P / "assets" / f.relative_to(V / "assets")
        if not dst.exists() or dst.stat().st_mtime < f.stat().st_mtime: dst.parent.mkdir(parents=True, exist_ok=True); _sh.copy2(f, dst)
(P / "assets").mkdir(parents=True, exist_ok=True)
_sh.copy2(V / "audio" / VOICE, P / "assets" / VOICE)
hosts = []
for si, (ph, name) in enumerate(SECTIONS):
    t0, t1 = SEC_T[si], SEC_T[si + 1]
    if ONLY and name != ONLY: continue
    items = [(k, s) for k, s in enumerate(SHOTS) if t0 - .01 <= s["t"] < t1 - .01]
    html_, js = [], []
    for k, s in items:
        b, j = build(s, k, t0); html_.append(b); js += j
    doc = f'''<template id="{name}-template">
<div id="root" data-composition-id="{name}" data-width="1920" data-height="1080" data-start="0" data-duration="{t1 - t0:.3f}">
<style>{CSS}</style>
<div class="glow"></div>
{chr(10).join(html_)}
<script>
(function () {{
  const tl = gsap.timeline({{ paused: true }});
  {chr(10).join("  " + x for x in js)}
  window.__timelines = window.__timelines || {{}};
  window.__timelines["{name}"] = tl;
}})();
</script>
</div>
</template>
'''
    (P / "compositions" / f"{name}.html").write_text(TH.apply(doc), encoding="utf8")
    hosts.append((name, round(t0, 3), round(t1 - t0, 3)))

VOL = {"whoosh": ("whoosh", .14, .4), "pop": ("pop", .1, .3), "typing_short": ("typing", .07, .8), "ding_sparkle": ("ding", .1, .7),
       "click_toggle": ("click", .14, .3), "error_buzz": ("error", .08, .8), "bass_hit": ("hit", .09, .5),
       "record_scratch": ("scratch", .1, .6), "vine_boom": ("boom", .09, .9), "impact_boom": ("boom", .09, .9)}
ALIAS = {"click": "click_toggle", "ding": "ding_sparkle", "typing": "typing_short"}
(P / "assets" / "sfx").mkdir(parents=True, exist_ok=True); HAVE = {}
for key, (nm, _, _) in VOL.items():
    hit = next(iter(sorted((STUDIO / "sfx").glob(nm + ".*"))), None) if (STUDIO / "sfx").exists() else None
    if hit and hit.suffix.lower() in (".wav", ".mp3", ".ogg", ".m4a"): _sh.copy2(hit, P / "assets" / "sfx" / hit.name); HAVE[key] = hit.name
SFX = [(a, ALIAS.get(n, n)) for a, n in SFX]
miss = sorted({n for _, n in SFX if n not in HAVE})
if not HAVE: print("  ! youtube-studio/sfx/ has no sound files: this edit will have no sound effects (see youtube-studio/sfx/README.md)")
if miss: print("  ! no sound file in youtube-studio/sfx/ for: " + ", ".join(VOL[n][0] if n in VOL else n for n in miss) + " (skipped)")
last, sfx = -1, []
for at, nm in sorted(SFX):
    if nm in HAVE and at - last >= .35: _, v, d = VOL[nm]; sfx.append((at, HAVE[nm], v, d)); last = at
END = SEC_T[-1]
if ONLY:
    a_, b_ = SEC_T[[n for _, n in SECTIONS].index(ONLY)], SEC_T[[n for _, n in SECTIONS].index(ONLY) + 1]
    hosts = [(n, 0.0, d) for n, a, d in hosts]; sfx = [(x - a_, f, v, d) for x, f, v, d in sfx if a_ <= x < b_]; END = b_ - a_
root = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      {TH.font_link()}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: #F5F4EE; }}
    </style>
  </head>
  <body>
    <div id="main" data-composition-id="main" data-start="0" data-duration="{END:.3f}" data-width="1920" data-height="1080">
''' + "\n".join(f'      <div id="{n}-host" class="clip" data-composition-src="compositions/{n}.html" data-composition-id="{n}" data-start="{a}" data-duration="{d}" data-track-index="1" data-track-kind="graphics"></div>' for n, a, d in hosts) + f'''
      <audio id="vo" class="clip" src="assets/{VOICE}" data-start="0" data-duration="{(END if ONLY else VOICE_END + .3):.3f}" data-media-start="{(a_ if ONLY else 0):.3f}" data-track-index="20" data-volume="1"></audio>
''' + "\n".join(f'      <audio id="sfx{q}" class="clip" src="assets/sfx/{f}" data-start="{a:.3f}" data-duration="{d}" data-track-index="21" data-volume="{v}" data-fade-out="0.05"></audio>' for q, (a, f, v, d) in enumerate(sfx)) + '''
    </div>
    <script>
      window.__timelines = window.__timelines || {};
      window.__timelines["main"] = gsap.timeline({ paused: true });
    </script>
  </body>
</html>
'''
(P / "index.html").write_text(TH.apply(root), encoding="utf8")
print(f"{len(SHOTS)} shots, {len(hosts)} sections, {len(sfx)} sfx, length {END:.1f}s")
for s in SHOTS: print(f'{s["t"]:7.2f} {s["e"] - s["t"]:5.2f}  {s["kind"]:7} {s["at"]}')
json.dump([{"k": k, "t": round(s["t"], 2), "e": round(s["e"], 2), "kind": s["kind"], "at": s["at"]} for k, s in enumerate(SHOTS)],
          open(V / "shot_times.json", "w", encoding="utf8"), indent=1)
