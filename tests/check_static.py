#!/usr/bin/env python3
"""Dependency-free structural checks for the STARPATH static application."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / 'index.html'

class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.scripts = []
        self.external_resources = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                raise AssertionError(f'duplicate element id: {attrs["id"]}')
            self.ids.add(attrs['id'])
        if tag in ('script', 'img', 'link') and 'src' in attrs:
            self.external_resources.append(attrs['src'])
        if tag == 'script' and 'src' in attrs:
            self.scripts.append(attrs['src'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--extract-js', type=Path, help='Write the inline script to a file for node --check')
    args = ap.parse_args()
    html = PAGE.read_text(encoding='utf-8')
    scan = Scan()
    scan.feed(html)
    must_exist = {'sky', 'expeditionPanel', 'observatoryPanel', 'survivalSection',
                  'waterScene', 'missionAction', 'latitude', 'longitude', 'utc'}
    assert must_exist <= scan.ids, f'missing elements: {sorted(must_exist - scan.ids)}'
    assert not scan.scripts, 'expected a single self-contained app, not external JS'
    scripts = re.findall(r'<script(?:\s[^>]*)?>(.*?)</script>', html, re.I | re.S)
    assert len(scripts) == 1, f'expected one embedded application script, found {len(scripts)}'
    for marker in ('function horizontal(', 'function renderMission(', 'function rayGeometry('):
        assert marker in scripts[0], f'missing core simulation: {marker}'
    if args.extract_js:
        args.extract_js.parent.mkdir(parents=True, exist_ok=True)
        args.extract_js.write_text(scripts[0], encoding='utf-8')
        print(f'wrote embedded script to {args.extract_js}')
    print(f'PASS: app structure, {len(scan.ids)} unique IDs, one embedded JS module, core models present')

if __name__ == '__main__':
    main()
