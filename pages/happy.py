import dash
from dash import html

dash.register_page(__name__, path="/happy", title="No need to be upset - Stefan Conradie")


def layout():
    return html.Div(
        className="happy-page",
        children=[
            html.Iframe(
                src="https://www.youtube.com/embed/I_NkBrDmGxM?si=aOwcN8js3gwgg5vE&controls=0",
                title="YouTube video player",
                className="happy-video",
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share",
            )
        ],
    )
