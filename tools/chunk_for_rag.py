#!/usr/bin/env python3
"""Create RAG-friendly chunks from scraped markdown files.
Outputs JSONL files per document under `rag_chunks/` with metadata.
"""
import os
import re
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRAPED = ROOT / 'scraped_osdcloud'
META = ROOT / 'json_metadata'
OUT = ROOT / 'rag_chunks'

# Approximate chunk size (characters)
CHUNK_SIZE = 3000
OVERLAP = 300


def split_text(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    # First try splitting by headings
    parts = re.split(r'(?:^|\n)(?=#{1,3} )', text, flags=re.M)
    chunks = []
    buf = ''
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if len(buf) + len(part) < chunk_size:
            buf = (buf + "\n\n" + part).strip()
        else:
            if buf:
                chunks.append(buf)
            # if part is huge, break it
            if len(part) > chunk_size:
                for i in range(0, len(part), chunk_size - overlap):
                    chunks.append(part[i:i+chunk_size])
                buf = ''
            else:
                buf = part
    if buf:
        chunks.append(buf)
    # add overlaps
    if overlap and len(chunks) > 1:
        out = []
        for i, c in enumerate(chunks):
            if i == 0:
                out.append(c)
            else:
                prev = out[-1]
                # create overlap by taking last N chars of prev + current
                overlap_text = (prev + '\n' + c)[-overlap:]
                out.append(overlap_text + '\n' + c)
        return out
    return chunks


def main():
    OUT.mkdir(exist_ok=True)
    docs = list(SCRAPED.rglob('*.md'))
    print('Found', len(docs), 'markdown files to chunk')
    total_chunks = 0
    for md in docs:
        rel = md.relative_to(SCRAPED)
        meta_file = META / (md.name.replace('.md', '') + '_metadata.json')
        source_url = None
        title = md.stem
        if meta_file.exists():
            try:
                m = json.loads(meta_file.read_text(encoding='utf-8'))
                source_url = m.get('source_url')
                title = m.get('title') or title
            except Exception:
                pass
        text = md.read_text(encoding='utf-8', errors='ignore')
        chunks = split_text(text)
        if not chunks:
            continue
        out_file = OUT / (md.name.replace('.md', '') + '_chunks.jsonl')
        with open(out_file, 'w', encoding='utf-8') as f:
            for i, c in enumerate(chunks, start=1):
                doc = {
                    'id': f"{md.stem}#chunk-{i}",
                    'title': title,
                    'chunk_index': i,
                    'content': c,
                    'source_url': source_url,
                    'relative_path': str(rel)
                }
                f.write(json.dumps(doc, ensure_ascii=False) + '\n')
        total_chunks += len(chunks)
    print('Wrote chunk files to', OUT, 'total chunks:', total_chunks)


if __name__ == '__main__':
    main()
