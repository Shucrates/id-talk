import json, re

# Links that aren't images. Kept here rather than in the templates so they're easy to change.
EXTRA = {
    'linkedin': 'https://www.linkedin.com/in/shubhamnileshpatil/',
}

with open('a/assets.json') as f:
    assets = {**json.load(f), **EXTRA}

for src, out in [('src.html', 'index.html'), ('links.src.html', 'links.html')]:
    with open(src) as f:
        html = f.read()
    html = re.sub(r'\{\{(\w+)\}\}', lambda m: assets.get(m.group(1), m.group(0)), html)
    missing = re.findall(r'\{\{\w+\}\}', html)
    if missing:
        raise SystemExit(f'{src}: no asset for {sorted(set(missing))}')
    with open(out, 'w') as f:
        f.write(html)
    print(f'{out}: {len(html) / 1e6:.1f} MB')
