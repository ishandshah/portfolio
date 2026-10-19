# Ishan Shah portfolio

This is the existing static GitHub Pages portfolio. The public routes stay at the repository root; reusable page content is rendered from `site/content.py` into the original HTML templates.

## Preview and build

```bash
python3 -m http.server 8081
```

Open `http://localhost:8081`. To generate clean deployable output and run the site checks:

```bash
python3 scripts/build_site.py --output dist
python3 -m unittest discover -s tests -v
```

The build output contains only the nine HTML routes, site assets, `robots.txt`, `sitemap.xml`, and `.nojekyll`. The runtime site has no package installation step. `scripts/build_resume.py` regenerates the two public resume PDF aliases and requires ReportLab.

## Content and evidence

Edit public claims in `site/content.py`, and layouts in `scripts/build_site.py`. `site/sessionize-snapshot.json` is the dated public Sessionize feed snapshot. Before publishing a new claim, confirm its wording, date, status, attribution, metric scope, and public URL against current source material. Keep recommendation letters, private correspondence, and petition evidence out of this repository and build output. Regenerate, run the checks, and inspect desktop and mobile layouts after content or template changes.

## Routes and deployment

The preserved routes are `index.html`, `about.html`, `projects.html`, `leadership.html`, `speaking.html`, `writing.html`, `service.html`, `resume.html`, and `contact.html`. GitHub Pages is configured for the `main` branch root at `https://ishandshah.github.io/portfolio/`. Pushing to `main` publishes the site; confirm the build and factual review before doing so.
