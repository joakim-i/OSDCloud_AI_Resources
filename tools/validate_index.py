import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

INDEX_FILES = [
    ROOT / 'complete_index.json',
    ROOT / 'transformation_index.json',
    ROOT / 'document_index.json'
]


def load_json(path: Path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to load {path}: {e}")
        return None


def gather_referenced_files(idx_json):
    refs = set()
    if not idx_json:
        return refs
    # Look for fields that commonly reference filenames
    def walk(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in ('filename', 'metadata_file') and isinstance(v, str):
                    refs.add(v)
                else:
                    walk(v)
        elif isinstance(obj, list):
            for it in obj:
                walk(it)
    walk(idx_json)
    return refs


def main():
    all_refs = set()
    for idx in INDEX_FILES:
        if not idx.exists():
            print(f"Index file missing: {idx}")
            continue
        j = load_json(idx)
        refs = gather_referenced_files(j)
        print(f"From {idx.name}: found {len(refs)} referenced filenames")
        all_refs.update(refs)

    print('\nChecking referenced files:')
    missing = []
    for ref in sorted(all_refs):
        p = ROOT / ref
        if not p.exists():
            missing.append(ref)
            print(f" MISSING: {ref}")
        else:
            print(f" OK: {ref}")

    print('\nSummary:')
    print(f" Total referenced files: {len(all_refs)}")
    print(f" Missing: {len(missing)}")
    if missing:
        print('\nMissing files list:')
        for m in missing:
            print(' -', m)


if __name__ == '__main__':
    main()
