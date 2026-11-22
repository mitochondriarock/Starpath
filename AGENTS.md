# STARPATH — Codex engineering guidance

## Purpose
STARPATH is an educational celestial-navigation adventure and survival-science lab. Preserve and improve the existing playable prototype; do not replace it with a landing page or a nonfunctional mock-up.

## First task
Read `CODEX_FIRST_TASK.md` and execute the work described there, including tests and a GitHub Pages deployment. The canonical repository is `https://github.com/mitochondriarock/Starpath` (capital S in repository path). It was initially empty. Do not modify unrelated repositories.

## Application and constraints
- The entire existing application is in `index.html`; no network calls or external assets are required to run the game.
- Preserve Expedition, Observatory, and Survival Lab modes and their mobile UI.
- Maintain scientific transparency: the sky uses approximate star coordinates / local sidereal time, and Snell's-law water exercise is schematic. Do not claim instrument-grade or real-world survival reliability.
- Wild mushrooms and plants should never be marked safe to eat solely by visual/app identification. Make uncertainty, local expert verification and risk avoidance part of gameplay.
- Preserve offline capability and usability from Safari/Chrome on Mac/iPhone.
- Keep the app accessible: keyboard controls, labels, touch targets and legible text.
- For any scientific feature, write tests of expected numerical/behavioral invariants, and label simplifications in docs.
- Avoid adding unnecessary dependencies; if a build system becomes useful, document how to run it and keep static deployment working.

## Validation
Run `python3 tests/check_static.py`; then `python3 tests/check_static.py --extract-js /tmp/starpath.js` and `node --check /tmp/starpath.js`. Optional smoke tests in `tests/browser_smoke.py` use Playwright/Chromium.

## Publishing
- Use only `mitochondriarock/Starpath`.
- Preserve user work if the repository has changed since the handoff; inspect the remote before push.
- Configure GitHub Pages using the supplied workflow and Pages source set to **GitHub Actions**; publishing depends on repository settings/permissions.
- Do not assert deployment succeeded without checking the actual run and hosted page.
- Report the final commit, page URL, test results and any necessary manual steps.
