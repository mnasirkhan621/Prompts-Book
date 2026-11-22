# Lyric Writing Rules & Syllabic Meter for AI Vocals

AI singing engines (Suno, Udio) sing based on phonetic rhythm and syllabic stress. Badly metered lyrics cause rushed singing, garbled words, or awkward pauses.

---

## 1. The Syllable Count Balance Rule

Keep syllable counts consistent between rhyming lines:

### ❌ Unbalanced Meter (Garbled Audio):
```text
I walked into the dark night alone (8 syllables)
And the entire universe was unraveling before my very eyes like a kaleidoscope (26 syllables)
```
*Why it fails:* The model has to speed up into an unnatural frantic auctioneer chant to squeeze 26 syllables into the musical bar.

### ✅ Balanced Meter (Natural Vocal Delivery):
```text
I walked into the night alone (7 syllables)
The pavement cold beneath my feet (7 syllables)
A quiet truth already known (7 syllables)
With every shadow on the street (7 syllables)
```

---

## 2. Phonetic Pronunciation Spelling

When Suno mispronounces names, technical terms, or brand words, spell them phonetically:

| Intended Word | Phonetic Spelling in Lyrics Box |
| :--- | :--- |
| **Suno** | `SOO-noh` |
| **Cybernetic** | `SY-ber-net-ik` |
| **Nietzsche** | `NEE-chuh` |
| **Algorithm** | `AL-go-rith-um` |

---

## 3. Controlling Pauses & Timing

* **The Ellipsis (`...`)**: Adds a breathy 0.5s pause before the next word.
* **The Hyphen (`-`)**: Enforces staccato, syllable-by-syllable delivery (`In-de-pen-dent`).
* **CAPITAL LETTERS**: Triggers vocal emphasis, louder projection, or an emotional belt (`I WILL NEVER SURRENDER!`).
* **Repetition**: Repeat words explicitly in text rather than hoping the model loops (`Run, run, run away`).
