# Edit kit: extra shot kinds. Each kind: f(s, t, e, d, I, W, P, R, fx, t0) -> (html, [js]).
import html as H, random
import sys as _sys
_S = _sys.modules["shots"]   # the video's shots module (set by cream_build.py)
SKILLS, KEEP, LOADS = getattr(_S, "SKILLS", []), getattr(_S, "KEEP", []), getattr(_S, "LOADS", [])
YT_HYPE, YT_TUTS = getattr(_S, "YT_HYPE", []), getattr(_S, "YT_TUTS", [])
import re

KIT_CSS = r'''
.chip2 { font-size: 58px; padding: 24px 44px; border-radius: 26px; } .chip2 i { width: 24px; height: 24px; } .chipcol { gap: 40px; }
.term.light { background: #1b1c21; } .term.light .bar { background: #26272d; }
.term .body .tl.rl { color: #F4F4F2; }
.gifw { position: absolute; border: 10px solid #F4F4F2; border-radius: 18px; overflow: hidden; box-shadow: 0 34px 80px rgba(0,0,0,.6); background: #000; }
.gifw video { width: 100%; height: 100%; object-fit: cover; display: block; }
.gifw.bare { border: 0; background: transparent; box-shadow: none; border-radius: 0; }
.gcap { position: absolute; left: 0; right: 0; text-align: center; font: 900 70px/1.05 "Montserrat"; text-transform: uppercase; letter-spacing: -.02em; color: #F4F4F2; }
.pill.bl b { filter: blur(11px); }
.mstamp { position: absolute; padding: 14px 34px; border: 8px solid #E5484D; border-radius: 18px; color: #E5484D; font: 900 64px "Montserrat"; text-transform: uppercase; transform: rotate(-8deg); background: rgba(22,23,27,.82); }
.cc { position: absolute; left: 210px; top: 90px; width: 1500px; height: 900px; border-radius: 20px; overflow: hidden; background: #1E1E1D; box-shadow: 0 50px 120px rgba(0,0,0,.7), 0 0 0 2px #2a2c33; font-family: "Montserrat"; }
.cc .ctop { position: absolute; left: 0; right: 0; top: 0; height: 64px; border-bottom: 1px solid #2E2E2C; display: flex; align-items: center; gap: 22px; padding: 0 26px; color: #C9C8C2; font: 500 24px "Montserrat"; }
.cc .ctop .ic { display: flex; gap: 18px; color: #8E8D87; font: 500 22px "JetBrains Mono", monospace; } .cc .ctop .ttl { color: #E8E7E3; }
.cc .ctop .wn { margin-left: auto; display: flex; gap: 34px; color: #8E8D87; font: 400 24px "Montserrat"; }
.cc .cmsgs { position: absolute; left: 150px; right: 150px; top: 110px; bottom: 190px; display: flex; flex-direction: column; gap: 26px; justify-content: flex-end; }
.cc .ub { align-self: flex-end; max-width: 1000px; background: #2F2F2D; border-radius: 22px; padding: 22px 30px; color: #ECECEA; font: 500 40px/1.45 "Montserrat"; }
.cc .cl { color: #E8E7E3; font: 500 40px/1.5 "Montserrat"; position: relative; padding-left: 50px; } .cc .cl .st { position: absolute; left: 0; top: 2px; color: #D97757; font: 700 34px "Montserrat"; display: inline-block; }
.cc .cin { position: absolute; left: 200px; right: 200px; bottom: 74px; height: 92px; border-radius: 20px; background: #262624; border: 1px solid #3A3A38; display: flex; align-items: center; padding: 0 30px; color: #8E8D87; font: 500 34px "Montserrat"; }
.cc .cin .tx { color: #ECECEA; white-space: nowrap; overflow: hidden; max-width: 960px; } .cc .cin .tx .ch { opacity: 0; } .cc .cin .ph { position: absolute; left: 30px; }
.cc .cin .snd { margin-left: auto; width: 46px; height: 46px; border-radius: 12px; background: #3A3A38; flex: none; }
.cc .cft { position: absolute; right: 200px; bottom: 26px; color: #8E8D87; font: 500 22px "Montserrat"; } .cc .cft b { color: #C9C8C2; font-weight: 600; }
.win { position: absolute; border-radius: 22px; overflow: hidden; background: #111216; box-shadow: 0 50px 120px rgba(0,0,0,.7), 0 0 0 2px #2a2c33; }
.win .bar .lb { font-size: 24px; }
.wbody { position: absolute; left: 0; top: 56px; right: 0; bottom: 0; }
.sk { position: absolute; height: 74px; padding: 0 26px; border-radius: 16px; background: #1F2026; border: 2px solid #3a3c43; display: flex; align-items: center; gap: 14px; font: 600 27px "JetBrains Mono", monospace; color: #E6E6E3; white-space: nowrap; }
.sk i { width: 16px; height: 16px; border-radius: 4px; background: #5a5c63; display: block; flex: none; }
.sk.bl span { filter: blur(9px); } .sk.on { border-color: #F2C200; box-shadow: 0 0 40px rgba(242,194,0,.3); } .sk.on i { background: #F2C200; } .sk.bad { border-color: #E5484D; }
.post { position: absolute; width: 640px; padding: 34px 38px; border-radius: 24px; background: #1F2026; border: 2px solid #3a3c43; box-shadow: 0 30px 80px rgba(0,0,0,.55); }
.post .ph { display: flex; align-items: center; gap: 18px; margin-bottom: 22px; } .post .av { width: 64px; height: 64px; border-radius: 50%; background: #3a3c43; }
.post .ph i { display: block; width: 180px; height: 18px; border-radius: 9px; background: #3a3c43; } .post b { display: block; font: 900 50px/1.1 "Montserrat"; color: #F4F4F2; }
.post .ft { display: flex; gap: 40px; margin-top: 26px; } .post .ft i { display: block; width: 70px; height: 16px; border-radius: 8px; background: #2c2e35; }
.thumb { position: absolute; width: 300px; height: 169px; border-radius: 14px; background: #24262d; border: 2px solid #33353d; overflow: hidden; }
.thumb::after { content: ""; position: absolute; left: 0; bottom: 0; height: 7px; width: var(--p, 60%); background: #E5484D; }
.thumb .pl { position: absolute; left: 50%; top: 50%; width: 0; height: 0; border-left: 34px solid #5a5c63; border-top: 21px solid transparent; border-bottom: 21px solid transparent; transform: translate(-40%, -50%); }
.thumb b { position: absolute; left: 16px; top: 16px; width: 55%; height: 14px; border-radius: 7px; background: #4a4c55; }
.pcard { position: absolute; width: 330px; height: 92px; border-radius: 16px; background: #1F2026; border: 2px solid #3a3c43; display: flex; align-items: center; gap: 14px; padding: 0 20px; font: 600 26px "JetBrains Mono", monospace; color: #9a9ba0; }
.pcard i { width: 26px; height: 26px; border-radius: 6px; background: #F2C200; opacity: .7; display: block; }
.pcount { position: absolute; left: 0; right: 0; top: 380px; text-align: center; font: 900 220px/1 "Montserrat"; color: #F4F4F2; text-shadow: 0 20px 60px rgba(0,0,0,.85); }
.pcount small { display: block; font-size: 64px; margin-top: 10px; }
.recipe { position: absolute; width: 330px; height: 430px; border-radius: 22px; background: #F4F4F2; padding: 30px; box-shadow: 0 34px 80px rgba(0,0,0,.55); display: flex; flex-direction: column; gap: 16px; }
.recipe b { font: 900 34px "Montserrat"; color: #16171B; text-transform: uppercase; } .recipe i { display: block; height: 14px; border-radius: 7px; background: #CFCBC0; }
.recipe .img { height: 150px; border-radius: 14px; background: #E7E3D8; margin-bottom: 6px; }
.recipe.gold .img { background: linear-gradient(160deg, #EDE62A, #E8B000); }
.tc { position: absolute; top: 300px; width: 520px; height: 420px; border-radius: 30px; background: #1F2026; border: 3px solid #3a3c43; display: flex; flex-direction: column; justify-content: center; padding: 0 50px; box-shadow: 0 40px 100px rgba(0,0,0,.6); }
.tc em { font: 700 48px "JetBrains Mono", monospace; font-style: normal; color: #6b6c72; } .tc b { font: 900 76px/1 "Montserrat"; color: #F4F4F2; text-transform: uppercase; letter-spacing: -.02em; margin: 18px 0 14px; } .tc span { font: 600 34px "Montserrat"; color: #9a9ba0; }
.tc.on { border-color: #F2C200; box-shadow: 0 0 70px rgba(242,194,0,.25), 0 40px 100px rgba(0,0,0,.6); } .tc.on em { color: #F2C200; }
.boss { position: absolute; left: 810px; top: 110px; width: 300px; height: 300px; border-radius: 50%; overflow: hidden; border: 8px solid #F4F4F2; box-shadow: 0 30px 80px rgba(0,0,0,.6); }
.boss img { width: 100%; height: 100%; object-fit: cover; display: block; }
.bosslab { position: absolute; left: 0; right: 0; top: 430px; text-align: center; font: 700 34px "JetBrains Mono", monospace; color: #9a9ba0; }
.mate { position: absolute; top: 640px; width: 260px; height: 230px; border-radius: 26px; background: #1F2026; border: 2px solid #3a3c43; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 22px; font: 800 36px "Montserrat"; color: #F4F4F2; }
.ccard { position: absolute; width: 150px; height: 104px; border-radius: 14px; background: #1F2026; border: 2px solid #33353d; padding: 16px; display: flex; flex-direction: column; gap: 10px; }
.ccard i { display: block; height: 10px; border-radius: 5px; background: #3a3c43; } .ccard u { display: block; height: 22px; width: 60%; border-radius: 6px; background: #2c2e35; }
.qm { position: absolute; font: 900 120px "Montserrat"; color: #F2C200; }
.fold { position: absolute; top: 260px; width: 700px; height: 330px; box-sizing: border-box; border-radius: 26px; background: #1F2026; border: 3px solid #3a3c43; padding: 40px 46px; box-shadow: 0 40px 100px rgba(0,0,0,.6); }
.fold.on { border-color: #F2C200; } .fold .fh { display: flex; align-items: center; gap: 20px; font: 800 44px "Montserrat"; color: #F4F4F2; margin-bottom: 30px; }
.fold .fr { display: flex; align-items: center; gap: 18px; font: 500 34px "JetBrains Mono", monospace; color: #c9cacf; margin: 18px 0 0 10px; }
.neq { position: absolute; left: 900px; top: 350px; width: 120px; height: 150px; line-height: 150px; text-align: center; font: 900 130px "Montserrat"; color: #E5484D; }
.lrow { display: flex; align-items: baseline; gap: 26px; padding: 22px 34px; border-bottom: 1px solid #23252b; font: 500 30px "JetBrains Mono", monospace; }
.lrow b { color: #F4F4F2; font-weight: 700; flex: none; width: 360px; } .lrow span { color: #6b6c72; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.lrow.on { background: rgba(242,194,0,.08); } .lrow.on b { color: #F2C200; }
.full { padding: 10px 34px 30px 420px; display: flex; flex-direction: column; gap: 14px; } .full i { display: block; height: 16px; border-radius: 8px; background: #3a3c43; }
.bar2 { position: absolute; left: 260px; height: 110px; border-radius: 55px; transform-origin: 0 50%; }
.bar2l { position: absolute; left: 260px; font: 800 46px "Montserrat"; color: #F4F4F2; }
.ck { position: absolute; left: 560px; top: 210px; width: 800px; border-radius: 26px; background: #1F2026; border: 3px solid #3a3c43; padding: 40px 50px; box-shadow: 0 40px 100px rgba(0,0,0,.6); }
.ck .ch { font: 500 30px "JetBrains Mono", monospace; color: #9a9ba0; margin-bottom: 26px; }
.ck .cr { display: flex; align-items: center; gap: 30px; padding: 26px 10px; font: 800 52px "Montserrat"; color: #F4F4F2; border-radius: 16px; }
.ck .bx { width: 64px; height: 64px; border-radius: 14px; border: 4px solid #5a5c63; display: flex; align-items: center; justify-content: center; font: 900 46px "Montserrat"; color: #16171B; flex: none; }
.ck .bx.ok { background: #F2C200; border-color: #F2C200; } .ck .bx.no { background: #E5484D; border-color: #E5484D; color: #fff; } .ck .cr.no { color: #ff9a9d; }
.fls { font: 500 26px/1.45 "JetBrains Mono", monospace; color: #c9cacf; padding: 30px 40px 0; } .fls div { opacity: 0; } .fls b { color: #FF6B6B; font-weight: 700; }
.gp { position: absolute; width: 680px; border-radius: 24px; background: #1F2026; border: 3px solid #3a3c43; padding: 34px 40px; box-shadow: 0 40px 100px rgba(0,0,0,.6); }
.gp.on { border-color: #F2C200; } .gp .pn { display: flex; align-items: center; gap: 20px; font: 700 36px "JetBrains Mono", monospace; color: #F4F4F2; margin-bottom: 20px; }
.gp .ps { display: flex; align-items: center; gap: 18px; font: 500 32px "JetBrains Mono", monospace; color: #c9cacf; margin: 12px 0 0 20px; }
.ubar { position: absolute; left: 360px; top: 480px; width: 1200px; height: 110px; border-radius: 55px; background: #24262c; overflow: hidden; }
.ubar i { display: block; height: 100%; width: 100%; transform-origin: 0 50%; border-radius: 55px; }
.ulab { position: absolute; left: 360px; top: 380px; font: 700 40px "JetBrains Mono", monospace; color: #9a9ba0; } .uend { position: absolute; left: 1360px; top: 630px; font: 800 44px "Montserrat"; color: #E5484D; }
.msg { position: absolute; left: 300px; width: 700px; height: 54px; border-radius: 18px; background: #2F2F2D; }
.msg.c { left: 260px; background: #1F2026; border: 2px solid #33353d; width: 760px; }
.mcount { position: absolute; left: 1140px; top: 300px; font: 900 150px/1 "Montserrat"; color: #F4F4F2; } .mcount small { display: block; font: 700 40px "JetBrains Mono", monospace; color: #9a9ba0; margin-top: 18px; }
.srv { position: absolute; left: 1180px; top: 640px; display: flex; align-items: center; gap: 24px; font: 700 40px "JetBrains Mono", monospace; color: #9a9ba0; }
.tree { position: absolute; left: 380px; top: 130px; width: 1160px; height: 830px; }
.tr2 { font: 500 38px/1.55 "JetBrains Mono", monospace; color: #c9cacf; white-space: pre; padding: 4px 18px; border-radius: 10px; }
.tr2.dir { color: #F4F4F2; font-weight: 700; } .tr2.on { color: #F2C200; background: rgba(242,194,0,.1); }
.sform { position: absolute; left: 140px; top: 200px; width: 680px; height: 700px; border-radius: 22px; overflow: hidden; background: #1a1b20; box-shadow: 0 50px 120px rgba(0,0,0,.7), 0 0 0 2px #2a2c33; }
.sform .in { position: absolute; left: 0; top: 56px; right: 0; bottom: 0; display: flex; flex-direction: column; justify-content: center; gap: 22px; padding: 0 80px; }
.sform .in i { display: block; height: 70px; border-radius: 14px; background: #16171B; border: 2px solid #3a3c43; } .sform .in b { display: block; height: 30px; width: 60%; border-radius: 10px; background: #55575f; margin-bottom: 20px; }
.sform .in u { display: block; height: 76px; border-radius: 14px; background: #F2C200; margin-top: 10px; }
.lnode { position: absolute; left: 960px; width: 820px; height: 120px; border-radius: 26px; background: #1F2026; border: 3px solid #3a3c43; display: flex; align-items: center; gap: 28px; padding: 0 36px; font: 800 42px "Montserrat"; color: #F4F4F2; }
.lnode.red { border-color: #E5484D; color: #ff9a9d; }
.flw { position: absolute; width: 520px; height: 340px; border-radius: 24px; background: #111216; box-shadow: 0 40px 100px rgba(0,0,0,.6), 0 0 0 2px #2a2c33; overflow: hidden; }
/* light page: white cards, dark ink */
.gcap { color: #1F1E1D; } .mstamp { background: rgba(255,255,255,.92); }
.sk { background: #FFFFFF; border-color: #E3DFD4; color: #1F1E1D; box-shadow: 0 10px 30px rgba(31,30,29,.06); } .sk i { background: #CFCBC0; }
.thumb { background: #FFFFFF; border-color: #E3DFD4; box-shadow: 0 14px 34px rgba(31,30,29,.08); } .thumb b { background: #DAD6CB; } .thumb .pl { border-left-color: #A3A199; }
.pcard { background: #FFFFFF; border-color: #E3DFD4; color: #73726C; box-shadow: 0 14px 34px rgba(31,30,29,.08); } .pcount { color: #1F1E1D; text-shadow: none; } .pcount small { color: #1F1E1D; }
.recipe { box-shadow: 0 30px 70px rgba(31,30,29,.16); border: 1px solid #E3DFD4; }
.ubar { background: #E7E3D8; } .ulab { color: #73726C; }
.tc { background: #FFFFFF; border-color: #E3DFD4; box-shadow: 0 30px 80px rgba(31,30,29,.08); } .tc b { color: #1F1E1D; font-size: 64px; } .tc span { color: #73726C; }
.cap.dk { color: #73726C; }
'''

ICONS = {"terminal": "M3 5h18v14H3z M7 9l3 3-3 3 M12 15h5", "folder": "M3 6h6l2 2h10v11H3z", "file": "M6 2h9l5 5v15H6z M15 2v5h5",
         "claude": "M12 3v18 M3 12h18 M5.6 5.6l12.8 12.8 M18.4 5.6L5.6 18.4", "browser": "M3 4h18v16H3z M3 9h18 M6 6.5h.01 M9 6.5h.01",
         "lock": "M6 11h12v10H6z M8 11V7a4 4 0 0 1 8 0v4", "mail": "M3 5h18v14H3z M3 6l9 7 9-7", "key": "M14 10a4 4 0 1 0-1 2.6L21 21 M17 17l2-2",
         "db": "M4 6c0-2 16-2 16 0v12c0 2-16 2-16 0z M4 6c0 2 16 2 16 0 M4 12c0 2 16 2 16 0", "alert": "M12 3L2 21h20z M12 10v5 M12 18h.01",
         "send": "M3 11l18-8-8 18-2-8z"}
def icon(n, size, col="#F4F4F2"):
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="{col}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="{ICONS[n]}"/></svg>'
def vid(i, src, t0, start, dur, mstart=0.0, extra=""):
    return f'<video id="{i}" class="clip" src="assets/{src}" muted playsinline data-start="{start - t0:.3f}" data-duration="{dur:.3f}" data-media-start="{mstart:.2f}" data-track-index="2"{extra}></video>'
def win(I, idn, x, y, w, h, label, inner):
    return f'<div class="win" id="{I(idn)}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><div class="bar"><i></i><i></i><i></i><span class="lb">{H.escape(label)}</span></div><div class="wbody">{inner}</div></div>'
def rise(sel, at, P, y=50, dur=.35):
    return f'tl.fromTo("{sel}",{{y:{y},opacity:0}},{{y:0,opacity:1,duration:{dur},ease:"expo.out"}},{P(at)});'
def chip(I, idn, txt, col, at, P, extra=""):
    # never put text this low (the player bar covers it): chips stay at top <= 760
    extra = re.sub(r"top:(\d+)px", lambda m: f"top:{min(int(m.group(1)), 760)}px", extra)
    return (f'<div class="chip2 {col}" id="{I(idn)}" style="position:absolute;{extra}"><i></i>{H.escape(txt)}</div>',
            f'gsap.set("#{I(idn)}",{{opacity:0}});tl.fromTo("#{I(idn)}",{{opacity:0,y:24,scale:.9}},{{opacity:1,y:0,scale:1,duration:.3,ease:"back.out(1.7)"}},{P(at)});')

def k_pile(s, t, e, d, I, W, P, R, fx, t0):
    rnd = random.Random(4); n = s.get("n", 28); lab = s["label"]
    h = "".join(f'<div class="pcard" id="{I(f"c{q}")}" style="left:{rnd.randint(100, 1480)}px;top:{rnd.randint(100, 900)}px;transform:rotate({rnd.randint(-12, 12)}deg)"><i></i>{H.escape(lab)}</div>' for q in range(n))
    h += f'<div class="pcount" id="{I("n")}"><span id="{I("nv")}">0</span><small>{H.escape(s.get("small", "saved prompts"))}</small></div>'
    step = (d - .5) / n
    js = [f'gsap.set("#{I("")} .pcard",{{opacity:0}});tl.fromTo("#{I("n")}",{{opacity:0,scale:.8}},{{opacity:1,scale:1,duration:.3,ease:"back.out(1.6)"}},{P(t + .1)});',
          f'for(let q=0;q<{n};q++){{tl.fromTo("#{I("c")}"+q,{{opacity:0,y:-50}},{{opacity:1,y:0,duration:.2,ease:"power2.out"}},{R(t + .1):.3f}+q*{step:.3f});tl.set("#{I("nv")}",{{textContent:String(q+1)}},{R(t + .1):.3f}+q*{step:.3f});}}']
    return h, js

def k_chapter(s, t, e, d, I, W, P, R, fx, t0):
    h = f'<div class="tcard"><div class="no" id="{I("a")}">{s["no"]} / 03</div><div class="nm" id="{I("b")}">{H.escape(s["name"])}</div><div class="sb" id="{I("c")}">{H.escape(s["sub"])}</div></div>'
    js = [f'tl.fromTo(["#{I("a")}","#{I("b")}","#{I("c")}"],{{opacity:0,y:40}},{{opacity:1,y:0,duration:.4,ease:"expo.out",stagger:.12}},{P(t)});',
          f'tl.fromTo("#{I("b")}",{{scale:1}},{{scale:1.05,duration:{d:.2f},ease:"none"}},{P(t)});']
    return h, js

def k_bars2(s, t, e, d, I, W, P, R, fx, t0):
    # two bars compared: a=("label", value) grows first, b=("label", value) grows on b_at; widths follow the real values
    (la, va), (lb, vb) = s.get("a", ("small", 1)), s.get("b", ("big", 5)); mx = max(va, vb) or 1
    pr = W(s.get("b_at"), t + 1.6)
    h = (f'<div class="bar2l" style="top:300px" id="{I("la")}">{H.escape(la)}</div><div class="bar2" id="{I("a")}" style="top:370px;width:{max(40, round(1400 * va / mx))}px;background:linear-gradient(180deg,#EDE62A,#E8B000)"></div>'
         f'<div class="bar2l" style="top:580px" id="{I("lb")}">{H.escape(lb)}</div><div class="bar2" id="{I("b")}" style="top:650px;width:{max(40, round(1400 * vb / mx))}px;background:{"#E5484D" if s.get("b_bad", True) else "#1F1E1D"}"></div>'
         f'<div class="cap" style="left:260px;top:180px;text-align:left;color:#73726C">{H.escape(s.get("title", ""))}</div>')
    js = [f'gsap.set(["#{I("a")}","#{I("b")}"],{{scaleX:0}});tl.fromTo("#{I("la")}",{{opacity:0}},{{opacity:1,duration:.2}},{P(t)});tl.to("#{I("a")}",{{scaleX:1,duration:.5,ease:"power2.out"}},{P(t + .2)});',
          f'gsap.set("#{I("lb")}",{{opacity:0}});tl.to("#{I("lb")}",{{opacity:1,duration:.2}},{P(pr - .4)});tl.to("#{I("b")}",{{scaleX:1,duration:.9,ease:"power2.out"}},{P(pr - .3)});']
    fx(pr - .3, "pop")
    return h, js

REF_CSS = r'''
.nd { position: absolute; display: flex; align-items: center; gap: 18px; padding: 22px 34px; border-radius: 26px; background: #FFFFFF; border: 2px solid #E3DFD4; box-shadow: 0 24px 60px rgba(31,30,29,.08); font: 800 40px "Montserrat"; color: #1F1E1D; white-space: nowrap; transform: translate(-50%, -50%); }
.nd.c { padding: 34px; border-radius: 40px; border: 4px solid #F2C200; box-shadow: 0 0 70px rgba(242,194,0,.35), 0 30px 70px rgba(31,30,29,.1); }
.nd.sm { font: 600 26px "JetBrains Mono", monospace; padding: 14px 22px; border-radius: 16px; }
.nd.bad { border-color: #E5484D; box-shadow: 0 0 60px rgba(229,72,77,.3); }
.ndl { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; overflow: visible; }
.tok2 { position: absolute; width: 74px; height: 74px; border-radius: 18px; background: linear-gradient(180deg, #EDE62A, #E8B000); box-shadow: 0 10px 24px rgba(185,133,0,.25); }
.meterlab { position: absolute; left: 0; right: 0; text-align: center; font: 700 40px "JetBrains Mono", monospace; color: #73726C; }
.mcnt { position: absolute; left: 0; right: 0; top: 230px; text-align: center; font: 900 170px/1 "Montserrat"; color: #1F1E1D; }
.bigw { position: absolute; left: 0; right: 0; text-align: center; font: 900 150px/1 "Montserrat"; text-transform: uppercase; letter-spacing: -.03em; color: #1F1E1D; }
.bigw .ln2 { display: inline-block; position: relative; }
.strk { position: absolute; left: -2%; top: 52%; height: 18px; width: 104%; background: #E5484D; border-radius: 9px; transform-origin: 0 50%; }
.try { position: absolute; top: 300px; width: 300px; height: 380px; border-radius: 22px; background: #FFFFFF; border: 2px solid #E3DFD4; box-shadow: 0 24px 60px rgba(31,30,29,.08); padding: 26px; display: flex; flex-direction: column; gap: 14px; }
.try i { display: block; height: 16px; border-radius: 8px; background: #E7E3D8; } .try u { display: block; height: 120px; border-radius: 14px; background: #F1EEE6; margin-bottom: 6px; }
.try b { position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); width: 120px; height: 120px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font: 900 74px "Montserrat"; color: #fff; }
.try b.x { background: #E5484D; } .try b.ok { background: linear-gradient(180deg, #EDE62A, #E8B000); color: #1F1E1D; }
.try.on { border-color: #F2C200; box-shadow: 0 0 70px rgba(242,194,0,.35); }
.tryl { position: absolute; top: 720px; width: 300px; text-align: center; font: 700 30px "JetBrains Mono", monospace; color: #A3A199; }
'''
REF_CSS += r'''
.ytc { position: absolute; width: 420px; }
.ytc .th { width: 420px; height: 236px; border-radius: 16px; overflow: hidden; background: #DAD6CB; box-shadow: 0 16px 40px rgba(31,30,29,.14); }
.ytc .th img { width: 100%; height: 100%; object-fit: cover; display: block; }
.ytc .tt { margin-top: 14px; font: 700 22px/1.3 "Montserrat"; color: #1F1E1D; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.ytc .tt mark { background: #F2C200; color: #1F1E1D; padding: 0 4px; border-radius: 4px; }
.ytc .mt { margin-top: 6px; font: 500 19px "Montserrat"; color: #73726C; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
'''
KIT_CSS += REF_CSS

def k_nodes(s, t, e, d, I, W, P, R, fx, t0):
    """centre node + satellites joined by lines that draw on their cue word """
    cx, cy = s.get("center_xy", (960, 540)); items = s["items"]; bad = s.get("mode") == "tangle"
    h = f'<svg class="ndl" id="{I("svg")}">'
    for q, (lab, x, y, cue) in enumerate(items):
        h += f'<line id="{I(f"l{q}")}" x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="{"#E5484D" if bad else "#CFCBC0"}" stroke-width="4" stroke-dasharray="10 12"/>'
    h += '</svg>'
    h += f'<div class="nd c" id="{I("c")}" style="left:{cx}px;top:{cy}px">{icon("claude", 90, "#D97757")}</div>'
    for q, (lab, x, y, cue) in enumerate(items):
        h += f'<div class="nd{" sm" if bad else ""}" id="{I(f"n{q}")}" style="left:{x}px;top:{y}px">{H.escape(lab)}</div>'
    js = [f'tl.fromTo("#{I("c")}",{{opacity:0,scale:.5}},{{opacity:1,scale:1,duration:.4,ease:"back.out(1.7)"}},{P(t)});',
          f'tl.fromTo("#{I("c")}",{{scale:1}},{{scale:1.06,duration:.6,yoyo:true,repeat:{max(int(d / .6) - 1, 1)},ease:"sine.inOut"}},{P(t + .5)});']
    last = t + .2
    for q, (lab, x, y, cue) in enumerate(items):
        at = W(cue, last + .35) if cue else last + (.08 if bad else .5); at = max(at, last + (.05 if bad else .3)); last = at
        js.append(f'gsap.set(["#{I(f"n{q}")}","#{I(f"l{q}")}"],{{opacity:0}});tl.fromTo("#{I(f"l{q}")}",{{opacity:0}},{{opacity:1,duration:.25}},{P(at - .1)});'
                  f'tl.fromTo("#{I(f"n{q}")}",{{opacity:0,scale:.6}},{{opacity:1,scale:1,duration:.3,ease:"back.out(1.8)"}},{P(at)});')
        if not bad: fx(at, "pop")
    if bad:
        js.append(f'tl.to("#{I("c")}",{{borderColor:"#E5484D",boxShadow:"0 0 80px rgba(229,72,77,.45)",duration:.3}},{P(last + .3)});tl.to("#{I("")} .nd.sm",{{borderColor:"#E5484D",color:"#C0353A",duration:.25,stagger:.02}},{P(last + .3)});')
        fx(last + .3, "error_buzz") if s.get("buzz") else None
    js.append(f'tl.fromTo("#{I("")}",{{scale:1}},{{scale:1.05,duration:{d:.2f},ease:"none"}},{P(t)});')
    return h, js

def k_meter(s, t, e, d, I, W, P, R, fx, t0):
    """capacity meter: a row of token blocks . vanish = they disappear; fill = they pile up to the limit"""
    n = 16; mode = s.get("mode", "vanish"); h = ""
    for q in range(n):
        h += f'<div class="tok2" id="{I(f"k{q}")}" style="left:{230 + q * 92}px;top:500px"></div>'
    h += f'<div class="meterlab" style="top:620px">{H.escape(s.get("label", "tokens"))}</div>'
    js = []
    if mode == "low":   # a fresh chat: only a few blocks used, the rest of the day is still there
        js.append(f'gsap.set("#{I("")} .tok2",{{opacity:.18}});tl.to(["#{I("k0")}","#{I("k1")}","#{I("k2")}"],{{opacity:1,duration:.2,stagger:.12}},{P(t + .2)});')
        return h, js
    if mode == "vanish":
        js.append(f'tl.to("#{I("")} .tok2",{{opacity:0,y:-50,scale:.6,duration:.22,stagger:{{each:{min(.08, (d - .6) / n):.3f},from:"end"}}}},{P(t + .3)});')
        fx(t + .3, "whoosh")
    else:
        js.append(f'gsap.set("#{I("")} .tok2",{{opacity:0}});tl.to("#{I("")} .tok2",{{opacity:1,duration:.15,stagger:{(d - 1.0) / n:.3f}}},{P(t + .2)});')
        js.append(f'tl.to("#{I("")} .tok2",{{background:"#E5484D",duration:.25}},{P(e - .7)});'); fx(e - .7, "bass_hit")
    return h, js

def k_strike(s, t, e, d, I, W, P, R, fx, t0):
    """the old idea gets crossed out in red, the new one rises in gold"""
    old, new = s["old"], s["new"]; sc, nc = W(s["strike_at"], t + .9), W(s["new_at"], t + 2.4)
    h = (f'<div class="bigw" id="{I("a")}" style="top:330px;font-size:{s.get("size_old", 130)}px"><span class="ln2">{H.escape(old)}<i class="strk" id="{I("s")}"></i></span></div>'
         f'<div class="bigw" id="{I("b")}" style="top:560px;font-size:{s.get("size_new", 150)}px"><span class="goldg">{H.escape(new)}</span></div>')
    js = [f'tl.fromTo("#{I("a")}",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.35,ease:"expo.out"}},{P(t)});gsap.set("#{I("s")}",{{scaleX:0}});tl.to("#{I("s")}",{{scaleX:1,duration:.35,ease:"power2.inOut"}},{P(sc)});tl.to("#{I("a")}",{{opacity:.35,duration:.3}},{P(sc + .35)});',
          f'gsap.set("#{I("b")}",{{opacity:0}});tl.fromTo("#{I("b")}",{{opacity:0,y:60}},{{opacity:1,y:0,duration:.45,ease:"expo.out"}},{P(nc)});']
    fx(sc, "pop"); fx(nc, "impact_boom")
    return h, js

def k_tries(s, t, e, d, I, W, P, R, fx, t0):
    """kept testing: attempts fail (red X) one by one until one works (gold check) on the cue word"""
    n = 5; h = ""
    for q in range(n):
        x = 120 + q * 345
        h += f'<div class="try" id="{I(f"c{q}")}" style="left:{x}px"><u></u><i style="width:80%"></i><i style="width:60%"></i><i style="width:70%"></i><b class="{"ok" if q == n - 1 else "x"}" id="{I(f"b{q}")}">{"✓" if q == n - 1 else "✗"}</b></div><div class="tryl" style="left:{x}px">test {q + 1}</div>'
    ok = W(s.get("ok_at"), e - .8); step = max((ok - t - .4) / (n - 1), .25)
    if s.get("fast"): step = .16; ok = min(t + .4 + (n - 1) * step + .1, e - .3)
    js = [f'gsap.set("#{I("")} .try b",{{opacity:0,scale:.4}});tl.fromTo("#{I("")} .try",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.3,ease:"expo.out",stagger:.08}},{P(t)});']
    for q in range(n - 1):
        a = t + .4 + q * step; js.append(f'tl.to("#{I(f"b{q}")}",{{opacity:1,scale:1,duration:.22,ease:"back.out(2)"}},{P(a)});'); fx(a, "pop")
    js.append(f'tl.to("#{I(f"b{n - 1}")}",{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},{P(ok)});tl.set("#{I(f"c{n - 1}")}",{{attr:{{class:"try on"}}}},{P(ok)});tl.to(["#{I("c0")}","#{I("c1")}","#{I("c2")}","#{I("c3")}"],{{opacity:.35,duration:.3}},{P(ok)});')
    fx(ok, "ding_sparkle")
    wa = W(s.get("win_at"), None) if s.get("win_label") else None
    if wa:   # the winning test grows to the middle, "the results I wanted" under it
        js.append(f'tl.to("#{I(f"c{n - 1}")}",{{x:-{120 + (n - 1) * 345 - 810},scale:1.35,duration:.5,ease:"power3.inOut"}},{P(wa - 1.0)});tl.to(["#{I("c0")}","#{I("c1")}","#{I("c2")}","#{I("c3")}","#{I("")} .tryl"],{{opacity:0,duration:.3}},{P(wa - 1.0)});')
        c_, j_ = chip(I, "w", s.get("win_label", ""), "green", wa - .2, P, "left:640px;top:880px"); h += c_; js.append(j_)
    return h, js

def k_ytwall(s, t, e, d, I, W, P, R, fx, t0):
    """a feed of REAL popular Claude videos (thumbnail, title, channel, views), flying in and scrolling like YouTube"""
    vids = YT_HYPE if s["set"] == "hype" else YT_TUTS; h = ""
    hot = re.compile(r"(insane|scary|cooked|too late|master|tutorial|getting started|full workflow|top 1%)", re.I)
    for q, (vid_, title, ch, views) in enumerate(vids):
        x, y = 30 + (q % 4) * 470, 40 + (q // 4) * 360
        tt = H.escape(title)   # no highlights on the titles
        vw = f"{views / 1e6:.1f}M" if views >= 1e6 else f"{views // 1000}K"
        h += f'<div class="ytc" id="{I(f"v{q}")}" style="left:{x}px;top:{y}px"><div class="th"><img src="assets/yt/{vid_}.jpg" alt="" /></div><div class="tt">{tt}</div><div class="mt">{H.escape(ch)} · {vw} views</div></div>'
    h = f'<div id="{I("feed")}" style="position:absolute;inset:0">{h}</div>'
    rows = (len(vids) + 3) // 4
    js = [f'gsap.set("#{I("")} .ytc",{{opacity:0}});tl.fromTo("#{I("")} .ytc",{{opacity:0,y:60,scale:.9}},{{opacity:1,y:0,scale:1,duration:.3,ease:"back.out(1.5)",stagger:{min(.07, (d - .6) / len(vids)):.3f}}},{P(t)});',
          f'tl.fromTo("#{I("feed")}",{{y:0}},{{y:{-max(rows * 360 - 1040, 0)},duration:{d:.2f},ease:"power1.inOut"}},{P(t)});']
    return h, js

LIMIT_CSS = r'''
.lim .cmsgs { justify-content: flex-start; }
.lim .ub.old { opacity: .55; } .lim .cl.old { opacity: .55; }
.limbar { position: absolute; left: 200px; right: 200px; bottom: 60px; height: 132px; border-radius: 22px; background: #2B2220; border: 2px solid #8A3B32; display: flex; align-items: center; gap: 26px; padding: 0 36px; }
.limbar .lt { font: 700 36px "Montserrat"; color: #F4DCD7; } .limbar .ls { font: 500 28px "Montserrat"; color: #C9A9A2; margin-top: 6px; }
.limbar .ug { margin-left: auto; padding: 18px 30px; border-radius: 14px; background: #D97757; color: #1E1E1D; font: 800 28px "Montserrat"; }
'''
KIT_CSS += LIMIT_CSS


REST_CSS = r"""
/* light-page colours for the kinds above */
.mate { background: #FFFFFF; border-color: #E3DFD4; color: #1F1E1D; box-shadow: 0 24px 60px rgba(31,30,29,.08); } .boss { border-color: #FFFFFF; box-shadow: 0 30px 80px rgba(31,30,29,.2); } .bosslab { color: #73726C; }
.ccard { background: #FFFFFF; border-color: #E3DFD4; } .ccard i { background: #E7E3D8; } .ccard u { background: #F1EEE6; }
.post { background: #FFFFFF; border-color: #E3DFD4; box-shadow: 0 30px 80px rgba(31,30,29,.1); } .post b { color: #1F1E1D; } .post .av, .post .ph i { background: #E3DFD4; } .post .ft i { background: #EFECE4; }
.fold { background: #FFFFFF; border-color: #E3DFD4; box-shadow: 0 30px 80px rgba(31,30,29,.08); } .fold .fh { color: #1F1E1D; } .fold .fr { color: #4A4945; }
.bar2l { color: #1F1E1D; }
.ck { background: #FFFFFF; border-color: #E3DFD4; box-shadow: 0 30px 80px rgba(31,30,29,.08); } .ck .cr { color: #1F1E1D; } .ck .bx { border-color: #CFCBC0; } .ck .ch { color: #73726C; }
.gp { background: #FFFFFF; border-color: #E3DFD4; box-shadow: 0 30px 80px rgba(31,30,29,.08); } .gp .pn { color: #1F1E1D; } .gp .ps { color: #4A4945; }
.msg { background: #E3DFD4; } .msg.c { background: #FFFFFF; border-color: #E3DFD4; } .mcount { color: #1F1E1D; } .mcount small, .srv { color: #73726C; }
.lnode { background: #FFFFFF; border-color: #E3DFD4; color: #1F1E1D; box-shadow: 0 20px 50px rgba(31,30,29,.07); } .lnode.red { border-color: #E5484D; color: #C0353A; }
.qm { color: #C99A00; } .neq { color: #E5484D; }
.rcard { background: #FFFFFF; border-color: #E3DFD4; box-shadow: 0 14px 34px rgba(31,30,29,.07); } .rcard b { background: #DAD6CB; } .rcard i { background: #EFECE4; }
.doc { position: absolute; left: 260px; top: 90px; width: 1400px; height: 900px; border-radius: 22px; overflow: hidden; background: #FFFFFF; box-shadow: 0 40px 100px rgba(31,30,29,.22), 0 0 0 1px rgba(31,30,29,.08); }
.doc .bar { background: #EFECE4; } .doc .bar .lb { color: #1F1E1D; font-size: 24px; }
.doc .dl { position: absolute; left: 0; right: 0; top: 56px; padding: 40px 60px; }
.doc .ln { position: relative; font: 500 31px/1.75 "JetBrains Mono", monospace; color: #3A3935; white-space: pre-wrap; padding: 0 12px; border-radius: 8px; }
.doc .ln.h { font-weight: 700; color: #1F1E1D; } .doc .ln.m { color: #A3A199; }
.doc .hlb { position: absolute; inset: 0; background: rgba(242,194,0,.38); border-radius: 8px; transform-origin: 0 50%; }
.ord { position: absolute; width: 330px; height: 170px; border-radius: 24px; background: #FFFFFF; border: 2px solid #E3DFD4; box-shadow: 0 24px 60px rgba(31,30,29,.08); display: flex; align-items: center; justify-content: center; gap: 18px; font: 800 46px "Montserrat"; color: #1F1E1D; }
.ord em { font: 700 36px "JetBrains Mono", monospace; font-style: normal; color: #C99A00; }
.ordq { position: absolute; font: 900 90px "Montserrat"; color: #C99A00; }
.qc { position: absolute; top: 330px; width: 300px; height: 220px; border-radius: 22px; background: #FFFFFF; border: 2px solid #E3DFD4; box-shadow: 0 24px 60px rgba(31,30,29,.08); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 18px; }
.qc b { font: 900 60px "Montserrat"; color: #1F1E1D; } .qc span { font: 600 26px "JetBrains Mono", monospace; color: #73726C; }
.qc.on { border-color: #F2C200; } .qc i { position: absolute; right: 18px; top: 18px; width: 50px; height: 50px; border-radius: 50%; background: linear-gradient(180deg,#EDE62A,#E8B000); display: flex; align-items: center; justify-content: center; font: 900 30px "Montserrat"; font-style: normal; color: #1F1E1D; opacity: 0; }
.draft { position: absolute; left: 660px; top: 260px; width: 600px; height: 520px; border-radius: 26px; background: #FFFFFF; border: 4px solid #F2C200; box-shadow: 0 0 80px rgba(242,194,0,.35); padding: 40px; display: flex; flex-direction: column; gap: 18px; }
.draft b { font: 900 52px "Montserrat"; color: #1F1E1D; } .draft i { display: block; height: 18px; border-radius: 9px; background: #E7E3D8; }
.lc .cmsgs { justify-content: flex-start; } .lc .ub, .lc .cl { font-size: 32px; }
.lc .tagb { display: inline-block; margin-left: 14px; padding: 4px 14px; border-radius: 10px; background: #F2C200; color: #16171B; font: 800 24px "Montserrat"; vertical-align: middle; }
"""
KIT_CSS += REST_CSS

FILES = getattr(_S, "FILES", {})   # {"name": ("window title", ["line 1", "line 2", ...])}

def k_file(s, t, e, d, I, W, P, R, fx, t0):
    """a REAL file in a light window on the cream plate, slow scroll, the spoken line gets a gold highlight on its cue """
    title, lines = FILES[s["file"]]; body = ""
    for q, ln in enumerate(lines):
        cls = "h" if ln.startswith("#") or ln.startswith("name:") else ("m" if ln.strip() in ("---", "") else "")
        body += f'<div class="ln {cls}" id="{I(f"l{q}")}"><i class="hlb" id="{I(f"h{q}")}" style="transform:scaleX(0)"></i><span style="position:relative">{H.escape(ln) or "&nbsp;"}</span></div>'
    h = f'<div class="plate"></div><div class="doc" id="{I("c")}"><div class="bar"><i></i><i></i><i></i><span class="lb">{H.escape(title)}</span></div><div class="dl" id="{I("dl")}">{body}</div></div>'
    js = [f'tl.fromTo("#{I("c")}",{{y:50,opacity:0}},{{y:0,opacity:1,duration:.35,ease:"expo.out"}},{P(t)});tl.fromTo("#{I("c")}",{{scale:.95}},{{scale:1,duration:{d:.2f},ease:"none"}},{P(t)});',
          f'tl.fromTo("#{I("dl")}",{{y:0}},{{y:{-s.get("scroll", 40)},duration:{d:.2f},ease:"none"}},{P(t)});']
    for q, cue in s.get("marks", []):
        a = W(cue, t + .5) if cue else t + .5
        js.append(f'tl.to("#{I(f"h{q}")}",{{scaleX:1,duration:.35,ease:"power2.out"}},{P(a)});'); fx(a, "ding_sparkle")
    return h, js

HAMMER = '<svg viewBox="0 0 24 24" width="150" height="150" fill="none" stroke="#1F1E1D" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4l6 6-3 3-6-6z M11 7L3 15l3 3 8-8"/></svg>'

GAUGE_CSS = r"""
.gauge { position: absolute; left: 510px; top: 170px; width: 900px; height: 520px; }
.glab { position: absolute; left: 0; right: 0; top: 700px; text-align: center; font: 900 64px "Montserrat"; text-transform: uppercase; letter-spacing: -.02em; color: #1F1E1D; }
"""
KIT_CSS += GAUGE_CSS

def k_gauge(s, t, e, d, I, W, P, R, fx, t0):
    """"what actually moves the needle": a gauge whose needle swings into the gold on "needle" """
    arc = ('<svg class="gauge" viewBox="0 0 900 520"><path d="M90 470 A360 360 0 0 1 810 470" fill="none" stroke="#E7E3D8" stroke-width="56" stroke-linecap="round"/>'
           f'<path id="{I("g")}" d="M90 470 A360 360 0 0 1 810 470" fill="none" stroke="#F2C200" stroke-width="56" stroke-linecap="round" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100"/>'
           f'<g id="{I("n")}"><line x1="450" y1="470" x2="450" y2="150" stroke="#1F1E1D" stroke-width="14" stroke-linecap="round"/></g>'
           '<circle cx="450" cy="470" r="34" fill="#1F1E1D"/></svg>')
    lab = s.get("label", ""); acc = s.get("accent_word", "")
    lab_h = " ".join(f'<span class="goldg">{H.escape(x)}</span>' if x == acc else H.escape(x) for x in lab.split())
    h = arc + f'<div class="glab" id="{I("l")}">{lab_h}</div>'
    nd = W(s.get("at_word"), t + 1.2)
    js = [f'gsap.set("#{I("n")}",{{rotation:-80,svgOrigin:"450 470"}});tl.fromTo("#{I("")} .gauge",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.35,ease:"expo.out"}},{P(t)});',
          f'tl.to("#{I("n")}",{{rotation:-55,duration:.6,ease:"sine.inOut",yoyo:true,repeat:1}},{P(t + .2)});',
          f'tl.to("#{I("n")}",{{rotation:68,duration:.7,ease:"back.out(1.4)"}},{P(nd - .2)});tl.to("#{I("g")}",{{strokeDashoffset:12,duration:.7,ease:"power2.out"}},{P(nd - .2)});',
          f'gsap.set("#{I("l")}",{{opacity:0}});tl.fromTo("#{I("l")}",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.3,ease:"expo.out"}},{P(nd - .1)});']
    fx(nd - .2, "ding_sparkle")
    return h, js

NEW = {"gauge": k_gauge, "file": k_file, "ytwall": k_ytwall, "nodes": k_nodes, "meter": k_meter, "strike2": k_strike, "tries": k_tries, "prompts": k_pile,
       "chapter": k_chapter, "bars2": k_bars2}
