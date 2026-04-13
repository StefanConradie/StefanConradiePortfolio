import dash
from dash import html

from data.cv_data import (
    SUMMARY, CONTACT, WORK_EXPERIENCE, PROJECTS,
    EDUCATION, SKILLS, CERTIFICATIONS,
)

dash.register_page(__name__, path="/cv", title="CV - Stefan Conradie")


def layout():
    return html.Div(
        className="cv-page",
        children=[
            # Contact bar
            html.Div(
                className="cv-contact-bar",
                children=[
                    html.Span(CONTACT["phone"]),
                    html.Span("·"),
                    html.A(CONTACT["email"], href=f"mailto:{CONTACT['email']}", className="accent-link"),
                    html.Span("·"),
                    html.A(CONTACT["linkedin"], href=CONTACT["linkedin_url"],
                           target="_blank", rel="noopener noreferrer", className="accent-link"),
                ],
            ),

            # Summary
            html.Div(
                className="cv-section-block",
                children=[
                    html.H2("Summary", className="cv-section-title"),
                    html.P(SUMMARY, className="summary-text"),
                ],
            ),

            # Work Experience
            html.Div(
                className="cv-section-block",
                children=[
                    html.H2("Work Experience", className="cv-section-title"),
                    *[_work_entry(job) for job in WORK_EXPERIENCE],
                ],
            ),

            # Projects
            html.Div(
                className="cv-section-block",
                children=[
                    html.H2("Projects", className="cv-section-title"),
                    *[_project_entry(p) for p in PROJECTS],
                ],
            ),

            # Education
            html.Div(
                className="cv-section-block",
                children=[
                    html.H2("Education", className="cv-section-title"),
                    *[_education_entry(e) for e in EDUCATION],
                ],
            ),

            # Skills
            html.Div(
                className="cv-section-block",
                children=[
                    html.H2("Technical Skills", className="cv-section-title"),
                    html.Div(
                        className="skills-grid",
                        children=[_skill_category(name, items) for name, items in SKILLS.items()],
                    ),
                ],
            ),

            # Certifications
            html.Div(
                className="cv-section-block",
                children=[
                    html.H2("Certifications", className="cv-section-title"),
                    html.Div(
                        className="cert-list",
                        children=[_cert_entry(c) for c in CERTIFICATIONS],
                    ),
                ],
            ),

            # Download
            html.Div(
                className="cv-download-area",
                children=[
                    html.A(
                        "⬇️ Download CV (PDF)",
                        href="/assets/cv/Stefan_Conradie_CV.pdf",
                        download="Stefan_Conradie_CV.pdf",
                        className="btn-secondary",
                    )
                ],
            ),
        ],
    )


def _work_entry(job):
    end = job["end_date"] or "Present"
    date_str = f"{job['start_date']} – {end}"
    return html.Div(
        className="cv-entry",
        children=[
            html.Div(
                className="cv-entry-header",
                children=[
                    html.Div(children=[
                        html.Span(job["title"], className="cv-entry-title"),
                        html.Span(f" · {job['company']}", className="cv-entry-subtitle"),
                    ]),
                    html.Span(date_str, className="cv-entry-date"),
                ],
            ),
            html.P(job["location"], className="cv-entry-location"),
            html.Ul(
                className="cv-bullet-list",
                children=[html.Li(r) for r in job["responsibilities"]],
            ),
        ],
    )


def _project_entry(project):
    return html.Div(
        className="cv-entry",
        children=[
            html.Div(
                className="cv-entry-header",
                children=[
                    html.Span(project["title"], className="cv-entry-title"),
                    html.Span(project["year"], className="cv-project-year"),
                ],
            ),
            html.Div(
                className="cv-project-tech",
                children=[
                    html.Span("Tech:", className="cv-project-tech-label"),
                    html.Span(project["technologies"], className="cv-project-tech-value"),
                ],
            ),
            html.P(project["description"], className="cv-project-desc"),
        ],
    )


def _education_entry(edu):
    date_str = (
        edu["start_date"] if edu["start_date"] == edu["end_date"]
        else f"{edu['start_date']} – {edu['end_date']}"
    )
    return html.Div(
        className="cv-entry",
        children=[
            html.Div(
                className="cv-entry-header",
                children=[
                    html.Div(children=[
                        html.Span(edu["degree"], className="cv-entry-title"),
                        html.Span(f" · {edu['institution']}", className="cv-entry-subtitle"),
                    ]),
                    html.Span(date_str, className="cv-entry-date"),
                ],
            ),
            html.P(edu["location"], className="cv-entry-location"),
        ],
    )


def _skill_category(name, items):
    return html.Div(
        className="skill-category",
        children=[
            html.P(name, className="skill-category-name"),
            html.Div(
                className="skill-tags",
                children=[html.Span(item, className="skill-tag") for item in items],
            ),
        ],
    )


def _cert_entry(cert):
    return html.Div(
        className="cert-entry",
        children=[
            html.Div(children=[
                html.P(cert["name"], className="cert-name"),
                html.P(cert["issuer"], className="cert-issuer"),
            ]),
            html.Span(cert["issue_date"], className="cert-date"),
        ],
    )
