from dash import html

title_container = html.Div(
    [
        html.H1("EEG Explorer "),
        html.H3(" by Spectre Biotech", className="text-primary"),
    ],
    id="title-container",
)