""" footer component"""

from dash import html

footer = html.Footer(
    children=[
        html.P(
            children=[
                "Pour plus d'informations, veuillez visiter notre ",
                html.A(
                    "FAQ",
                    href="/faq",
                    style={'marginRight': '10px', 'marginLeft': '10px'}
                ),
                " ou ",
                html.A(
                    "Nous Contacter",
                    href="/contact",
                    style={'marginRight': '10px', 'marginLeft': '10px'}
                ),
            ],
            style={'marginTop': '15px'}
        ),
        html.P(
            children=[
                "© 2024 EEG Explorer by ",
                html.A(
                    "Spectre Biotech",
                    href="https://www.spectre-biotech.com",
                    target="_blank",
                    style={'marginRight': '10px', 'marginLeft': '10px'}
                ),
            ],
            style={'marginTop': '15px'}
        )
    ]
)
