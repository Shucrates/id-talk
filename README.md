# id-talk

Demos Anon presentation — the story of [id.patilshubham.me](https://id.patilshubham.me), a pop-culture ID card generator built by [@shuisbored](https://www.instagram.com/shuisbored/).

A scrollable, animated HTML page built for a 7-minute talk.

## Run locally

Put `index.html` and the videos (`bored-files.mp4`, `cmiygl-reel.mp4`, `loki-tva.mp4`, `tasm.mp4`, `collab.mp4`) in the same folder and serve:

```bash
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080).

## Build from source

`src.html` (the talk) and `links.src.html` (the links page) are templates with `{{key}}` placeholders. `a/assets.json` has base64 data URIs for all images; non-image values like the LinkedIn URL live at the top of `build.py`. Build both pages with:

```bash
python3 build.py
```

## Controls

- **Arrow keys / Space / PageDown** — next stop
- **PageUp** — previous stop
- **F** — toggle fullscreen
