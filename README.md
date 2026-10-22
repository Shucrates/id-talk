# id-talk

Demos Anon presentation — the story of [id.patilshubham.me](https://id.patilshubham.me), a pop-culture ID card generator built by [@shuisbored](https://www.instagram.com/shuisbored/).

A scrollable, animated HTML page built for a 7-minute talk.

## Run locally

Put `index.html`, `bored-files.mp4`, and `cmiygl-reel.mp4` in the same folder and serve:

```bash
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080).

## Build from source

`src.html` is the template with `{{key}}` placeholders. `a/assets.json` has base64 data URIs for all images. Build with:

```bash
python3 -c "
import json, re
with open('a/assets.json') as f: assets = json.load(f)
with open('src.html') as f: src = f.read()
out = re.sub(r'\{\{(\w+)\}\}', lambda m: assets.get(m.group(1), m.group(0)), src)
with open('index.html','w') as f: f.write(out)
"
```

## Controls

- **Arrow keys / Space / PageDown** — next stop
- **PageUp** — previous stop
- **F** — toggle fullscreen
