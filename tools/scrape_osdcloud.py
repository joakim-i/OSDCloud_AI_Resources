#!/usr/bin/env python3
"""Scrape OSDCloud markdown pages listed in llms.txt and save locally.
Saves pages under `scraped_osdcloud/` mirroring site paths and
creates simple metadata JSON files under `json_metadata/`.
"""
import os
import re
import json
import time
from pathlib import Path
from urllib import request, parse, error

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / 'scraped_osdcloud'
META_DIR = ROOT / 'json_metadata'
LLMS_URL = 'https://www.osdcloud.com/llms.txt'

USER_AGENT = 'osdcloud-scraper/1.0 (+https://github.com)'


def http_get(url):
    req = request.Request(url, headers={'User-Agent': USER_AGENT})
    try:
        with request.urlopen(req, timeout=30) as r:
            content = r.read()
            ct = r.headers.get('Content-Type', '')
            return content, ct
    except error.HTTPError as e:
        print(f"HTTP error {e.code} for {url}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return None, None


def ensure_parent(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)


def save_file(path: Path, data: bytes):
    ensure_parent(path)
    with open(path, 'wb') as f:
        f.write(data)


def extract_title(md_text: str):
    # find first H1 or H2
    for line in md_text.splitlines():
        line = line.strip()
        if line.startswith('# '):
            return line.lstrip('# ').strip()
        if line.startswith('## '):
            return line.lstrip('# ').strip()
    # fallback: first non-empty line
    for line in md_text.splitlines():
        if line.strip():
            return line.strip()[:80]
    return ''


def slug_from_url(url: str):
    p = parse.urlparse(url).path
    return p.lstrip('/')


def main():
    OUT_DIR.mkdir(exist_ok=True)
    META_DIR.mkdir(exist_ok=True)

    print('Fetching llms.txt...')
    data, _ = http_get(LLMS_URL)
    if not data:
        print('Failed to fetch llms.txt')
        return
    text = data.decode('utf-8', errors='ignore')
    # find all markdown URLs
    urls = set(re.findall(r'https?://[\w\-\.\/:@?&=+,%#]+?\.md', text))
    print(f'Found {len(urls)} markdown URLs')

    index = []
    for url in sorted(urls):
        rel = slug_from_url(url)
        out_path = OUT_DIR / rel
        meta_path = META_DIR / (Path(rel).name.replace('.md', '') + '_metadata.json')
        if out_path.exists():
            print('Skipping (exists):', rel)
            continue
        print('Downloading:', url)
        content, ct = http_get(url)
        if not content:
            print('  -> failed')
            continue
        # Save markdown
        save_file(out_path, content)
        try:
            md_text = content.decode('utf-8', errors='ignore')
        except Exception:
            md_text = ''
        title = extract_title(md_text) or Path(rel).stem
        meta = {
            'title': title,
            'source_url': url,
            'path': str(out_path.relative_to(ROOT)),
            'fetched_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'size_bytes': len(content),
        }
        with open(meta_path, 'w', encoding='utf-8') as mf:
            json.dump(meta, mf, indent=2, ensure_ascii=False)
        index.append(meta)
        # be polite
        time.sleep(0.2)

    # write index
    idx_file = ROOT / 'scraped_index.json'
    with open(idx_file, 'w', encoding='utf-8') as f:
        json.dump({'generated_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'count': len(index), 'documents': index}, f, indent=2)
    print('Saved', len(index), 'documents to', OUT_DIR)
    print('Metadata in', META_DIR)


if __name__ == '__main__':
    main()
