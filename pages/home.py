import dash
from dash import html, dcc

dash.register_page(__name__, path="/", title="Stefan Conradie")

# SVG icon strings for project thumbnails (stroke="currentColor" picks up CSS color)
_SVG_HOUSE = """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>"""

_SVG_CHART = """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>"""

_SVG_BAR = """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>"""

_SVG_VIDEO = """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>"""

_SVG_USERS = """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>"""

_SVG_TREND = """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 13l4-4 4 4 6-6 4 4M3 17h18"/></svg>"""

_SVG_SALES = """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 19h16M8 17V9m4 8V5m4 12v-6"/></svg>"""

_SVG_LINKEDIN = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" style="width:1.5rem;height:1.5rem"><path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/></svg>"""

_SVG_GITHUB = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" style="width:1.5rem;height:1.5rem"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>"""


def _svg_icon(svg_string, extra_class=""):
    """Wrap an SVG string in a dcc.Markdown for inline rendering."""
    return dcc.Markdown(
        dangerously_allow_html=True,
        children=svg_string,
        className=f"project-icon {extra_class}".strip(),
    )


def _project_card(title, url, svg, description):
    return html.Article(
        className="project-card",
        children=[
            html.Header(
                className="project-card-header",
                children=[
                    html.H2(
                        html.A(title, href=url, target="_blank", rel="noopener noreferrer",
                               className="accent-link"),
                        className="project-card-title",
                    )
                ],
            ),
            html.A(
                href=url, target="_blank", rel="noopener noreferrer",
                className="project-card-thumb",
                children=[_svg_icon(svg)],
            ),
            html.P(description, className="project-desc"),
            html.Ul(
                html.Li(
                    html.A("View Project", href=url, target="_blank", rel="noopener noreferrer",
                           className="btn-primary btn-primary-sm")
                ),
                className="btn-list",
            ),
        ],
    )


def layout():
    return html.Div(
        children=[
            # About / Terminal section
            html.Section(
                id="about",
                className="about-section",
                **{"aria-labelledby": "about-heading"},
                children=[
                    html.Div(
                        className="terminal-card",
                        children=[
                            # Traffic lights header
                            html.Div(
                                className="terminal-header",
                                children=[
                                    html.Div(
                                        className="traffic-lights",
                                        **{"role": "img"},
                                        children=[
                                            html.Div(className="dot dot-red"),
                                            html.Div(className="dot dot-yellow"),
                                            html.Div(className="dot dot-green"),
                                        ],
                                    ),
                                    html.Span(
                                        "terminal — ssh stefanconradie@portfolio",
                                        className="terminal-title",
                                    ),
                                ],
                            ),
                            # Content
                            html.Div(
                                className="terminal-content",
                                children=[
                                    html.Div(
                                        className="about-header",
                                        children=[
                                            html.P("🌱", className="about-emoji"),
                                            html.Div(
                                                children=[
                                                    html.H1("Stefan Conradie", id="about-heading",
                                                            className="about-name"),
                                                    html.P("Senior Data Analyst", className="about-title"),
                                                ]
                                            ),
                                        ],
                                    ),
                                    html.Div(
                                        className="about-bio",
                                        children=[
                                            html.P(
                                                "Welcome to my portfolio! I'm a data analyst passionate about "
                                                "creating value from data and exploring advanced methods to create "
                                                "insights. Here you'll find my projects, skills, and work experiences."
                                            )
                                        ],
                                    ),
                                    html.Hr(className="divider"),
                                    html.Div(className="info-row", children=[
                                        html.Span("Location", className="info-label"),
                                        html.Span("United Kingdom 🌍", className="info-value"),
                                    ]),
                                    html.Div(className="info-row", children=[
                                        html.Span("Work", className="info-label"),
                                        html.Span(children=[
                                            "Senior Analyst @ ",
                                            html.A(
                                                "BDO",
                                                href="https://www.bdo.co.uk/en-gb/services/advisory/bdo-digital/data-analytics-ai-services",
                                                target="_blank", rel="noopener noreferrer",
                                                className="accent-link",
                                                **{"aria-label": "Visit BDO website"},
                                            ),
                                        ], className="info-value"),
                                    ]),
                                    html.Div(className="info-row", children=[
                                        html.Span("Interests", className="info-label"),
                                        html.Span("Technology, data, automation and visualisation",
                                                  className="info-value"),
                                    ]),
                                    html.Div(className="info-row", children=[
                                        html.Span("Contact", className="info-label"),
                                        html.Span(
                                            html.A(
                                                "stefan.alwyn.conradie@gmail.com",
                                                href="mailto:stefan.alwyn.conradie@gmail.com",
                                                className="accent-link",
                                                **{"aria-label": "Send email"},
                                            ),
                                            className="info-value",
                                        ),
                                    ]),
                                    html.Div(className="info-row", children=[
                                        html.Span("Social", className="info-label"),
                                        html.Span(
                                            html.Ul(
                                                className="social-list",
                                                children=[
                                                    html.Li(html.A(
                                                        href="https://linkedin.com/in/stefan-conradie-link",
                                                        target="_blank", rel="noopener noreferrer",
                                                        className="social-link",
                                                        children=[
                                                            dcc.Markdown(dangerously_allow_html=True,
                                                                         children=_SVG_LINKEDIN),
                                                            html.Span("LinkedIn", className="sr-only"),
                                                        ],
                                                    )),
                                                    html.Li(html.A(
                                                        href="https://github.com/StefanConradie",
                                                        target="_blank", rel="noopener noreferrer",
                                                        className="social-link",
                                                        children=[
                                                            dcc.Markdown(dangerously_allow_html=True,
                                                                         children=_SVG_GITHUB),
                                                            html.Span("GitHub", className="sr-only"),
                                                        ],
                                                    )),
                                                ],
                                            ),
                                            className="info-value",
                                        ),
                                    ]),
                                    html.Div(className="info-row tech-row", children=[
                                        html.Span("Tech", className="info-label"),
                                        html.Div(
                                            className="tech-list",
                                            **{"role": "list", "aria-label": "Tech"},
                                            children=[
                                                html.Span("SQL", className="tech-tag", title="SQL"),
                                                html.Span("python", className="tech-tag", title="Python"),
                                                html.Span("PowerBI", className="tech-tag",
                                                          title="PowerBI, Tableau"),
                                                html.Span("gpt", className="tech-tag",
                                                          title="LLMs, GPT-3/4, Claude, etc."),
                                            ],
                                        ),
                                    ]),
                                ],
                            ),
                            html.Div(
                                className="terminal-footer",
                                children=[
                                    html.Span("$", className="dollar"), " cat about.txt",
                                ],
                            ),
                        ],
                    )
                ],
            ),

            # Projects section
            html.Section(
                id="projects",
                className="projects-section",
                children=[
                    html.Div(
                        className="section-card",
                        **{"role": "region", "aria-label": "Project showcase"},
                        children=[
                            html.H2("💻 project samples", className="section-label"),

                            # Featured project
                            html.Article(
                                className="featured-project",
                                children=[
                                    html.Header(
                                        className="featured-header",
                                        children=[
                                            html.H2(
                                                html.A(
                                                    "Data Cleaning in SQL",
                                                    href="https://github.com/StefanConradie/StefanConradiePortfolioProjects/blob/main/NashvilleCleaning.sql",
                                                    target="_blank", rel="noopener noreferrer",
                                                    className="accent-link",
                                                ),
                                                className="featured-title",
                                            ),
                                            html.P("Cleaning housing data using SQL",
                                                   className="featured-subtitle"),
                                        ],
                                    ),
                                    html.A(
                                        href="https://github.com/StefanConradie/StefanConradiePortfolioProjects/blob/main/NashvilleCleaning.sql",
                                        target="_blank", rel="noopener noreferrer",
                                        className="project-thumbnail",
                                        children=[_svg_icon(_SVG_HOUSE, "project-icon-lg")],
                                    ),
                                    html.Ul(
                                        html.Li(
                                            html.A(
                                                "View Project",
                                                href="https://github.com/StefanConradie/StefanConradiePortfolioProjects/blob/main/NashvilleCleaning.sql",
                                                target="_blank", rel="noopener noreferrer",
                                                className="btn-primary",
                                            )
                                        ),
                                        className="btn-list",
                                    ),
                                ],
                            ),

                            # Projects grid
                            html.Div(
                                className="projects-grid",
                                children=[
                                    _project_card(
                                        "Data Exploration in SQL",
                                        "https://github.com/StefanConradie/StefanConradiePortfolioProjects/blob/main/CovidData.sql",
                                        _SVG_CHART,
                                        "Data Exploration in Covid-19 data set in SQL Server.",
                                    ),
                                    _project_card(
                                        "Tableau Projects",
                                        "https://public.tableau.com/app/profile/stefan.conradie#!/?newProfile=&activeTab=0",
                                        _SVG_BAR,
                                        "All of my Tableau Visualization Projects.",
                                    ),
                                    _project_card(
                                        "Movie Correlation with Python",
                                        "https://github.com/StefanConradie/StefanConradiePortfolioProjects/blob/main/MovieCorrelationProject.ipynb",
                                        _SVG_VIDEO,
                                        "Cleaning movie related data as well as determining correlations between "
                                        "different factors that influence gross income in the movie industry.",
                                    ),
                                    _project_card(
                                        "Analysing Employees data",
                                        "https://github.com/StefanConradie/StefanConradiePortfolioProjects/blob/main/EmployeesProject.sql",
                                        _SVG_USERS,
                                        "Analysing of employees data. Looking at the spread of male and female "
                                        "genders in different departments using SQL Server.",
                                    ),
                                    _project_card(
                                        "Forecasting data using statistical and ML methods",
                                        "https://github.com/StefanConradie/Forecasting",
                                        _SVG_TREND,
                                        "Analysing various datasets using statistical and ML methods to predict "
                                        "future trends.",
                                    ),
                                    _project_card(
                                        "Predictive Analytics of sales data",
                                        "https://github.com/StefanConradie/Predictive-Analytics",
                                        _SVG_SALES,
                                        "Exploratory data analysis and clustering on Walmart store sales data to "
                                        "identify patterns, relationships, and groupings among stores.",
                                    ),
                                ],
                            ),

                            html.Div(
                                className="terminal-footer",
                                children=[
                                    html.Span("$", className="dollar"),
                                    " ls -la projects/ | total 7",
                                ],
                            ),
                        ],
                    )
                ],
            ),

            # CV preview section
            html.Section(
                id="cv-preview",
                className="cv-section",
                children=[
                    html.H2("📄 curriculum vitae", className="cv-section-label"),
                    html.Div(
                        className="section-card",
                        **{"role": "region", "aria-label": "CV Preview"},
                        children=[
                            html.P(
                                "View my complete CV for work experience, education, and skills.",
                                className="project-desc",
                            ),
                            html.Div(
                                className="btn-group",
                                children=[
                                    dcc.Link(
                                        "View Full CV →",
                                        href="/cv",
                                        className="btn-primary",
                                    ),
                                    html.A(
                                        "⬇️ Download CV (PDF)",
                                        href="/assets/cv/Stefan_Conradie_CV.pdf",
                                        download="Stefan_Conradie_CV.pdf",
                                        className="btn-secondary",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ]
    )
