# Get a free YouTube Data API key (≈3 minutes)

Used by `tools-and-workflows/youtube-research/yt.py` for views, likes, comments, channel uploads and search. Free: 10,000 units a day (one channel scan is about 5–10 units, one search is 100).

1. Open **https://console.cloud.google.com/** and sign in with your Google account.
2. Top bar → project dropdown → **New Project** → name it `youtube-tools` → **Create**. Make sure `youtube-tools` is selected in the top bar.
3. Go to **https://console.cloud.google.com/apis/library/youtube.googleapis.com** → click **Enable**.
4. Go to **APIs & Services → Credentials** (https://console.cloud.google.com/apis/credentials) → **+ Create credentials → API key**. Copy the key it shows.
5. Recommended: click the new key → under **API restrictions** choose **Restrict key** → tick **YouTube Data API v3** → **Save**. (Then the key can't be used for anything else if it ever leaks.)
6. Copy `tools-and-workflows/youtube-research/.env.example` to `tools-and-workflows/youtube-research/.env` and paste it after the `=`:
   ```
   YOUTUBE_API_KEY=AIza...your key...
   ```
   Save the file. No quotes, no spaces.
7. Test it:
   ```bash
   python tools-and-workflows/youtube-research/yt.py video NYb4NDjnGFQ
   ```
   You should see "Stop Studying Programming (do this instead)" with its view count.

No billing or card is needed for this API. Never paste the key into chat, a script, or anything you upload or share; `tools-and-workflows/youtube-research/.env` is the only place it lives.
