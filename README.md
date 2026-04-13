## Stefan Conradie Portfolio

A focused portfolio site for **Senior Data Analyst** work, built with **Python** and **Dash**.  
The site showcases projects, a full CV page, and a small easter-egg page.

## Features

- **Multi-page Dash app**: Uses Dash Pages for client-side routing between `/`, `/cv`, and `/happy`.
- **Light / Dark theme toggle**:
  - Global toggle in the navbar, persisted in `localStorage`.
  - Flash-free — theme is applied before first render via an inline script.
  - Implemented via CSS variables and Dash clientside callbacks.
- **Homepage (`/`)**:
  - Terminal-inspired hero section with location, work, interests, contact, and social links.
  - Curated project grid linking to SQL, Python, Tableau, and forecasting repos.
  - CV preview section with link to the full CV page and downloadable PDF.
- **CV page (`/cv`)**:
  - Renders contact info, summary, experience, projects, education, skills, and certifications.
  - All content defined in `data/cv_data.py` — edit there to update the page.
- **Responsive design**: Layout adapts to mobile, tablet, and desktop.
- **Easter egg**: Konami code (↑↑↓↓←→←→BA) redirects to `/happy`.

## Getting Started

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run locally

```bash
python app.py
```

Then open `http://127.0.0.1:8050` in your browser.

## Project Structure

```text
.
├── app.py                  # Main Dash app (entry point)
├── requirements.txt        # Python dependencies
├── data/
│   └── cv_data.py          # All CV content as Python dicts
├── pages/
│   ├── home.py             # Homepage (/)
│   ├── cv.py               # CV page (/cv)
│   ├── happy.py            # Easter egg (/happy)
│   └── not_found_404.py    # 404 page
└── assets/
    ├── styles.css          # All CSS (light/dark themes, layout, components)
    ├── konami.js           # Konami code easter egg
    ├── noise.svg           # Background texture
    ├── favicon.ico         # Favicons and icons
    └── cv/
        └── Stefan_Conradie_CV.pdf   # Downloadable CV
```

## Customization

- **CV content**: Edit `data/cv_data.py` to update summary, experience, projects, education, skills, and certifications.
- **Projects**: Edit the project list directly in `pages/home.py`.
- **Theme & colors**: Adjust CSS variables at the top of `assets/styles.css`.

## Deployment

Dash apps can be deployed to any platform that supports Python:

- **Render / Railway / Fly.io**: Deploy as a Python web app.
- **Heroku**: Add a `Procfile` with `web: python app.py`.
- **Docker**: Containerise with a standard Python image.

For production, set `debug=False` in `app.run()` and use a WSGI server such as `gunicorn`:

```bash
gunicorn app:server
```
