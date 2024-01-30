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
                    className="ms-1 footer-link"
                ),
            ],
            className="mt-3"
        ),
        html.P(
            children=[
                "© 2024 EEG Explorer by ",
                html.A(
                    "Spectre Biotech",
                    href="https://www.spectre-biotech.com",
                    target="_blank",
                    className="ms-1 footer-link"
                ),
            ],
            className="mt-3"
        )
    ]
)
