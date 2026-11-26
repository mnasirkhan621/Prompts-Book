# Shot plan. Each shot starts on the FIRST word of its "at" phrase, written exactly as the transcript has it
# (audio/words_tight.json). One dict per visual change; aim for a change every 2-3 s. Files are paths inside assets/.
# All kinds and options: tools-and-workflows/hyperframes-edit-kit/edit_kit/KINDS.md

GIFS = {}      # framed GIFs: name -> ("gifs/file.mp4", width, height, seconds)   (make files with tools-and-workflows/hyperframes-edit-kit/gif2mp4.py)
REPOS = []     # items for the "hub" map and "card" kinds: [("01", "NAME", "one-line sub"), ...]
HUBLABEL = ""  # word under the number in the map's centre, e.g. "tools"
FILES = {}     # files for the "file" kind: {"name": ("window title", ["line 1", "line 2"])}

SHOTS = [
    dict(at="first words of your hook", kind="words", lines=[["FIRST", "BIG"], ["LINE"]], gold={"LINE"}),
    # dict(at="so I opened", kind="screen", src="screens/site.mp4", label="site.com", mark=(120, 300, 500, 80), mark_at="pricing", sfx="whoosh"),
]
