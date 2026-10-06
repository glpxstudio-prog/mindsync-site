# MindSync — Website

Marketing site for MindSync: websites + sales systems (CRM, automations, booking, reviews) for Central Florida businesses.

Single static page (`index.html`), no build step. Hosted on GitHub Pages.

## Before launch
- Replace `$X` prices in the Pricing section
- Swap Featured Builds gradients for real client screenshots
- Replace the founder monogram with a photo
- Wire the contact form to your CRM webhook (see the script at the bottom of `index.html`)

## Area pages
`areas/<city>/index.html` is a city hub; `areas/<city>/<service>.html` is one service in that city (8 cities × 5 services).
Edit the copy in `build_areas.py`, then run `python3 build_areas.py` to regenerate. `sitemap.xml` is rebuilt too.
