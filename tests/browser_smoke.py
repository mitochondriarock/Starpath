#!/usr/bin/env python3
"""Optional Playwright browser smoke test for desktop and iPhone-sized layouts."""
from pathlib import Path
from playwright.sync_api import sync_playwright

HTML = Path(__file__).resolve().parents[1] / 'index.html'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, **({'executable_path': '/usr/bin/chromium'} if Path('/usr/bin/chromium').exists() else {}))
    for width, height in ((1280, 800), (390, 844)):
        page = browser.new_page(viewport={'width': width, 'height': height})
        errors = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.set_content(HTML.read_text(encoding='utf-8'), wait_until='load')
        assert 'STARPATH' in page.title()
        assert page.locator('#sky').is_visible()
        page.get_by_role('button', name='02 · Observatory').click()
        assert page.locator('#observatoryPanel').is_visible()
        page.locator('#preset').select_option('patagonia')
        assert page.locator('#sky').is_visible()
        page.get_by_role('button', name='03 · Survival lab').click()
        assert page.locator('#refractionLab').is_visible()
        page.locator('#aimOffset').fill('60')
        page.locator('#throwBtn').click()
        assert page.locator('#labStatus').inner_text()
        page.locator('button[data-lab="fieldguide"]').click()
        assert page.locator('#guideOptions button').count() > 0
        assert not errors, f'JavaScript errors at {width}×{height}: {errors}'
        print(f'PASS: browser smoke test at {width}×{height}')
        page.close()
    browser.close()
