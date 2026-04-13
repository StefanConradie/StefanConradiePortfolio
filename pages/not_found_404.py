import dash
from dash import html, dcc, clientside_callback, Input, Output, State

dash.register_page(__name__)


def layout():
    return html.Div(
        className="error-page",
        children=[
            html.Div(
                className="error-card",
                children=[
                    html.Div(
                        className="terminal-card",
                        **{"role": "region"},
                        children=[
                            html.Div(
                                className="terminal-content",
                                children=[
                                    # Error header
                                    html.Div(
                                        className="error-header",
                                        children=[
                                            html.P("🤔", style={"fontSize": "2.5rem"}),
                                            html.Div(children=[
                                                html.H1("404", className="error-code"),
                                                html.P("Page Not Found",
                                                       style={"color": "var(--text-muted)", "fontSize": "0.75rem"}),
                                            ]),
                                        ],
                                    ),

                                    # Error message box
                                    html.Div(
                                        className="error-message-box",
                                        children=[
                                            html.Span("ERROR:", className="error-label"),
                                            html.P(
                                                "The requested resource could not be found on this server. "
                                                "The page you are trying to access does not exist or has been moved.",
                                                className="error-text",
                                            ),
                                        ],
                                    ),

                                    html.Hr(className="divider"),

                                    # Error details
                                    html.Div(
                                        className="error-details",
                                        children=[
                                            html.Div(className="error-detail-row", children=[
                                                html.Span("Status", className="error-detail-key"),
                                                html.Span("404 Not Found", className="error-detail-val red"),
                                            ]),
                                            html.Div(className="error-detail-row", children=[
                                                html.Span("Request", className="error-detail-key"),
                                                html.Span(id="error-path", className="error-detail-val",
                                                          children="—"),
                                            ]),
                                            html.Div(className="error-detail-row", children=[
                                                html.Span("Server", className="error-detail-key"),
                                                html.Span("terminus v1.0", className="error-detail-val"),
                                            ]),
                                            html.Div(className="error-detail-row", children=[
                                                html.Span("Timestamp", className="error-detail-key"),
                                                html.Span(id="error-time", className="error-detail-val",
                                                          children="—"),
                                            ]),
                                        ],
                                    ),

                                    html.Hr(className="divider", style={"margin": "0.75rem 0"}),

                                    # Suggestions
                                    html.Div(
                                        className="suggestions",
                                        children=[
                                            html.P("Suggested actions:", className="suggestion-label"),
                                            html.P(children=[
                                                html.Span("01. ", className="suggestion-num"),
                                                "Check the URL for typos",
                                            ], className="suggestion-item"),
                                            html.P(children=[
                                                html.Span("02. ", className="suggestion-num"),
                                                "Return to the ",
                                                dcc.Link("homepage", href="/", className="accent-link"),
                                            ], className="suggestion-item"),
                                            html.P(children=[
                                                html.Span("03. ", className="suggestion-num"),
                                                "View my ",
                                                dcc.Link("CV", href="/cv", className="accent-link"),
                                            ], className="suggestion-item"),
                                        ],
                                    ),
                                ],
                            )
                        ],
                    )
                ],
            )
        ],
    )


# Populate path and timestamp from the browser
clientside_callback(
    """
    function(pathname) {
        var now = new Date().toISOString();
        return [pathname || window.location.pathname, now];
    }
    """,
    Output("error-path", "children"),
    Output("error-time", "children"),
    Input("_pages_location", "pathname"),
)
