# Codex first task: publish STARPATH v0.2

## Context
This directory is the existing first playable STARPATH game, prepared in a ChatGPT conversation. The GitHub repository `https://github.com/mitochondriarock/Starpath` exists, is public, uses `main` and was empty during preparation. ChatGPT GitHub connection only had read permissions, so source has NOT been committed there yet. Do not invent completion or silently replace this source.

## Work to perform
1. Inspect the files, read README, technical notes and roadmap, verify current Git status and inspect remote repository for unexpected changes.
2. Run the included static tests, JavaScript syntax checks, and (if feasible) Playwright browser tests at desktop and mobile viewports. Fix serious issues you find while preserving functionality.
3. Put this supplied code into `mitochondriarock/Starpath` on the `main` branch. If the remote is empty, initialize git and commit these files. If not empty, reconcile carefully and avoid overwriting user work. Obtain authorization from the user for authentication/permission prompts as required.
4. The file `.github/workflows/deploy.yml` is intended to publish to GitHub Pages. Verify YAML and action versions, then ensure Pages is configured for **GitHub Actions**. Do not treat pushing files as proof that Pages is enabled. If settings cannot be adjusted automatically, tell the user the exact UI action.
5. Confirm the deployment succeeded and visit `https://mitochondriarock.github.io/Starpath/` in a browser if available. Test an expedition step and both other modes at phone and desktop widths.
6. Report exact GitHub commit link and actual playable URL, plus anything left blocked. Do not leave an unexplained partial push.

## Acceptance criteria
- `index.html` renders and works from deployed GitHub Pages.
- A player can finish the four objectives (pointer stars, Polaris, latitude and bearing).
- Observatory sliders/fields change observed sky in response to latitude, longitude and time.
- Survival Lab refraction exercise and plant/fungus educational uncertainty section remain usable.
- No unsafe message suggesting that game identifications establish edibility.
- On phones, mission controls and sky chart remain reachable without excessive scrolling.
- No new API keys, external services, or costly subscriptions are introduced without the user's approval.

## Suggested next milestone, only after publishing
Refactor and write physics unit tests; ship a corrected view projection and richer learning feedback, then prototype a single outdoor traversal challenge. Prioritize scientifically sound learning over cosmetic expansion.
