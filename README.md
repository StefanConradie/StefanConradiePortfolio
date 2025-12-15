## Stefan Conradie Portfolio

A focused portfolio site for **Senior Data Analyst** work, built with **HTML**, **Tailwind CSS via CDN**, and **vanilla JavaScript**.  
The site showcases projects, a CV page rendered from structured data, and a small easter-egg page.

## Features

- **Static, no build step**: Pure HTML + JS, can be hosted on any static host.
- **Tailwind CSS via CDN**: Utility-first styling with a custom color palette.
- **Light / Dark theme toggle**:
  - Global toggle in the navbar shared by `index.html` and `cv.html`.
  - Theme persisted in `localStorage` and respects system preference.
  - Implemented via CSS variables and `js/theme.js`.
- **Portfolio homepage (`index.html`)**:
  - Terminal-inspired hero section with location, work, interests, contact, and social links.
  - Curated project grid linking to SQL, Python, Tableau, and forecasting repos.
  - CV preview section with link to the full CV page and downloadable PDF.
- **CV page (`cv.html`)**:
  - Renders contact info, summary, experience, projects, education, skills, and certifications.
  - All content defined as structured data in `js/cv.js` and formatted via `js/utils.js`.
- **Responsive design**: Layout adapts to mobile, tablet, and desktop.
- **Easter egg**: Konami code redirects to `happy.html`.

## Getting Started

### Install dependencies (optional but recommended)

Dependencies are only needed if you want to use the provided `npm` scripts for a local dev server.

```bash
npm install
```

### Run locally

You can use any static file server. A convenience script is provided:

```bash
# Recommended: use the dev script (see package.json)
npm run dev

# Or using Python
python -m http.server 8000

# Or using Node.js http-server
npx http-server
```

Then open `http://localhost:3000` (or the port shown by your server) in your browser.

> **Note:** ES modules (used on `cv.html`) require running from a server, not directly from the file system.

## Project Structure

```text
.
├── index.html          # Homepage / portfolio
├── cv.html             # CV page (renders from js/cv.js)
├── happy.html          # Easter egg page (Konami code)
├── 404.html            # 404 error page
├── assets/
│   └── cv/
│       └── Stefan_Conradie_CV.pdf   # Downloadable CV
├── js/
│   ├── config.js       # Project list and site configuration
│   ├── utils.js        # Shared utilities (e.g. date formatting)
│   ├── index.js        # Homepage logic (projects rendering, nav state)
│   ├── cv.js           # Structured CV data and accessors
│   └── theme.js        # Light/dark theme management and navbar toggle
├── public/             # Static assets (favicons, manifest, noise, share image)
│   ├── favicon*.png / .ico
│   ├── apple-touch-icon.png
│   ├── safari-pinned-tab.svg
│   ├── share.jpg       # Open Graph / social preview image
│   ├── noise.svg       # Background texture used by <noise> element
│   └── site.webmanifest
└── content/
    └── blog/
        └── hello-world/
            └── bluemarble.jpg       # Legacy/example blog asset
```

## Theming

- Theme is controlled via a `data-theme` attribute on `<html>`:
  - `data-theme="dark"` (default)
  - `data-theme="light"`
- `js/theme.js`:
  - Reads stored preference from `localStorage` (`sc-theme`).
  - Falls back to `prefers-color-scheme` when no stored value.
  - Attaches click handlers to `[data-theme-toggle]` buttons and updates icons/labels.
- `index.html` and `cv.html`:
  - Define CSS variables for light/dark palettes.
  - Override key Tailwind utility colors (e.g. `.bg-black/30`, `.text-white`, `.text-gray-400`) to use theme-aware variables.

## Customization

- **Projects**: Edit `js/config.js` to add or update portfolio projects.
- **CV content**: Edit `js/cv.js` to change summary, experience, projects, education, skills, and certifications.
- **Theme & colors**:
  - Adjust CSS variables in the `<style>` blocks in `index.html` / `cv.html`.
  - Update behavior in `js/theme.js` if you want different behavior (e.g., no system preference).
- **Layout & components**:
  - All markup is in `index.html` and `cv.html`, styled via Tailwind utilities and small custom classes.

## Deployment

Because this is a static site:

- You can deploy to any static host (e.g. GitHub Pages, Netlify, Vercel, S3, etc.).
- Ensure your host serves files from the project root so `/public/*` assets resolve correctly.
# StefanConradiePortfolio
