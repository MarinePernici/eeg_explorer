""" footer component"""

from dash import html

footer = html.Footer(
    children=[
        html.P(
            children=[
                "Pour plus d'informations, n'hésitez pas à",
                html.A(
                    "nous contacter.",
                    href="/contact",
                    className="ms-1"
                ),
            ],
            className="mt-3"
        ),
        html.P(
            children=[
                "© 2024 EEG Explorer by ",
            ],
            className="mt-3"
        )
    ]
)
