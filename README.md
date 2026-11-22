# STARPATH

**Celestial navigation through exploration.** STARPATH is an offline-capable educational browser game that teaches night-sky navigation through an interactive Rocky Mountains expedition and a small survival-science laboratory.

**Version:** 0.2 (November 8, 2026) · **Status:** playable educational prototype · **Platforms:** Safari, Chrome, Firefox, Edge; desktop and mobile layouts.

## Play

Open **[STARPATH on GitHub Pages](https://mitochondriarock.github.io/Starpath/)** once the repository has been created, its files committed, and GitHub Pages activated. Until publication, open `index.html` on a computer. On iOS, a hosted HTTPS URL is more reliable than an HTML file opened through Files.

STARPATH does not request device location or access external services. The app currently uses a single `index.html` with all styling and JavaScript embedded. No build system or backend is needed.

## Current activities

| Mode | What you can do |
|---|---|
| **Expedition** | Locate the Big Dipper pointer stars, find Polaris, measure its altitude to estimate latitude, and determine a true map bearing to a fictional rescue station. |
| **Observatory** | Change observer latitude/longitude and date/time; explore how bright-star positions change with local sidereal time, including a Southern Hemisphere preset. |
| **Survival Lab** | Practice a water-refraction aiming exercise using a simplified Snell's-law model, and evaluate identification uncertainty for plants and fungi. |

### How to play

1. Start in **Expedition** and follow the mission prompts. Tap stars in the chart; on mobile, use the navigation controls to change the viewing direction.
2. Work through the four objectives; hints are optional and affect XP.
3. Switch to **Observatory** to experiment with location and UTC time.
4. Try **Survival Lab** for physics and safety-oriented field-identification exercises.

## Scientific fidelity and safety

The bright-star sky uses approximate catalog coordinates and local horizontal-coordinate calculations. Atmospheric refraction, terrain masking, precession, and many other corrections are not modeled. The flat sky projection is for teaching, not instrument-grade navigation; the rescue map is fictional.

The water-refraction lab uses a two-dimensional model of Snell's law with a stationary water surface, not a substitute for real spearfishing instruction. The plant/fungus training focuses on *identification uncertainty and conservative decisions*. **Never eat a wild plant or mushroom because an app or game identifies it.** Local laws, conservation rules, and real-world safety matter.

See [Technical notes](docs/TECHNICAL_NOTES.md) and the [roadmap](docs/ROADMAP.md).

## Development

No dependencies are required to play. This repository intentionally starts with a simple codebase.

```bash
python3 tests/check_static.py
python3 tests/check_static.py --extract-js /tmp/starpath.js
node --check /tmp/starpath.js
```

Optional end-to-end browser regression test:

```bash
python3 -m pip install playwright
python3 -m playwright install chromium
python3 tests/browser_smoke.py
```

The GitHub Actions workflow validates the source and then deploys the self-contained site to GitHub Pages on pushes to `main`. In **Settings → Pages**, select **GitHub Actions** as the source. GitHub Pages availability depends on repository and account settings.

## Stewardship

The goal is educational transfer: understanding *why* an observation works, recognizing error and uncertainty, and gradually applying skills outdoors with appropriate real-world precautions. This project is not an emergency navigation service, a wild-food edibility classifier, or a replacement for qualified instruction.

The project license is not yet selected; no open-source license has been added by default.
