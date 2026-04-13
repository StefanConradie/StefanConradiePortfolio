import os
import dash
from dash import Dash, html, dcc, clientside_callback, Input, Output, State

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    title="Stefan Conradie",
    update_title=None,
)

# Inject anti-flash theme script before CSS loads
app.index_string = """<!DOCTYPE html>
<html lang="en">
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <script>
            (function() {
                try {
                    var stored = localStorage.getItem('sc-theme');
                    var prefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
                    var theme = stored || (prefersLight ? 'light' : 'dark');
                    document.documentElement.setAttribute('data-theme', theme);
                } catch(e) {
                    document.documentElement.setAttribute('data-theme', 'dark');
                }
            })();
        </script>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""


def navbar():
    return html.Header(
        id="main-header",
        children=[
            html.Nav(
                id="navigation-menu",
                **{"aria-label": "Main menu"},
                className="nav-inner",
                children=[
                    html.Span(
                        dcc.Link("stefanconradie", href="/", className="nav-brand"),
                        className="nav-brand-wrap",
                    ),
                    html.Div(
                        className="nav-right",
                        children=[
                            html.Span(
                                id="nav-links",
                                className="nav-links",
                                children=[
                                    dcc.Link("Home", href="/", id="nav-home", className="nav-link nav-active"),
                                    dcc.Link("CV", href="/cv", id="nav-cv", className="nav-link nav-dim"),
                                ],
                            ),
                            html.Button(
                                id="theme-toggle",
                                type="button",
                                **{"data-theme-toggle": "", "aria-label": "Toggle color mode"},
                                className="theme-btn",
                                children=[
                                    html.Span("🌙", **{"aria-hidden": "true", "data-theme-icon": ""}, id="theme-icon"),
                                    html.Span("Dark", **{"data-theme-label": ""}, id="theme-label"),
                                ],
                            ),
                        ],
                    ),
                ],
            )
        ],
    )


app.layout = html.Div(
    id="app-root",
    children=[
        dcc.Store(id="theme-store", storage_type="local", data="dark"),
        html.Div(id="theme-dummy", style={"display": "none"}),
        navbar(),
        html.Div(
            className="page-wrapper",
            children=[
                html.Main(id="main-content", children=dash.page_container),
            ],
        ),
        html.Div(className="noise-overlay"),
    ],
)


# Toggle theme on button click
clientside_callback(
    """
    function(n_clicks, current_theme) {
        if (!n_clicks) return window.dash_clientside.no_update;
        return current_theme === 'light' ? 'dark' : 'light';
    }
    """,
    Output("theme-store", "data"),
    Input("theme-toggle", "n_clicks"),
    State("theme-store", "data"),
    prevent_initial_call=True,
)

# Apply theme to <html> element and update button UI
clientside_callback(
    """
    function(theme) {
        theme = theme || 'dark';
        document.documentElement.setAttribute('data-theme', theme);
        try { localStorage.setItem('sc-theme', theme); } catch(e) {}
        var icon = document.getElementById('theme-icon');
        var label = document.getElementById('theme-label');
        if (icon) icon.textContent = theme === 'light' ? '☀️' : '🌙';
        if (label) label.textContent = theme === 'light' ? 'Light' : 'Dark';
        return '';
    }
    """,
    Output("theme-dummy", "children"),
    Input("theme-store", "data"),
)

# Highlight active nav link based on current URL (uses Dash Pages' internal location)
clientside_callback(
    """
    function(pathname) {
        var homeClass = pathname === '/' ? 'nav-link nav-active' : 'nav-link nav-dim';
        var cvClass = pathname && pathname.startsWith('/cv') ? 'nav-link nav-active' : 'nav-link nav-dim';
        return [homeClass, cvClass];
    }
    """,
    Output("nav-home", "className"),
    Output("nav-cv", "className"),
    Input("_pages_location", "pathname"),
)


server = app.server  # exposed for gunicorn: gunicorn app:server

if __name__ == "__main__":
    debug = os.getenv("DEBUG", "true").lower() == "true"
    app.run(debug=debug)
