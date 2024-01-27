import dash_bootstrap_components as dbc
from dash import html, dcc
from pages.title import title_container


explorer_layout = html.Div([
    dbc.Container(
        [
            *title_container,
            dbc.Row(
                dbc.Col([
                    html.Div(
                        id="dynamic-username",
                        style={'fontSize': '1.5rem'}
                    ),
                    html.P(
                        """C'est ici que vous pouvez interroger notre base de
                        données. Vous pouvez écrire votre question dans le
                        champ ci-dessous et lancer la recherche."""
                    ),
                    html.Div([
                        html.P(
                            """Pour en savoir plus sur notre base de données
                            et son contenu, vous pouvez consulter la """
                        ),
                        html.A(
                            "documentation.",
                            href="/documentation",
                            target="_blank",
                            className="mx-1",
                        ),
                    ], style={'display': 'flex'}),
                ], width={"size": 8, "offset": 2}),
            ),
            dbc.Row(
                dbc.Col(
                    [
                        dbc.Textarea(
                            id='query',
                            rows=4,
                            placeholder="""Ecrivez ici votre question
par exemple : combien y'a-t-il d'enregistrements EEG?
ou bien : quel est la valeur moyenne du pic alpha en F3 chez les personnes souffrant d'autisme?"""
                        ),
                        dbc.FormText(
                            "EEG Explorer utilise Chat GPT 4 pour traiter vos"
                            + " questions, il peut faire des erreurs, pensez à"
                            + " vérifier les informations importantes.",
                            color="info",
                        )
                    ],
                    width={"size": 8, "offset": 2}, className="mb-4 text-end",
                ),
            ),
            dbc.Row(
                dbc.Col(
                    dbc.Button(
                        'Interroger la base de données',
                        n_clicks=0,
                        id='search-button',
                        disabled=True,
                    ),
                    width={"size": 8, "offset": 2},
                    style={'textAlign': 'right'},
                ),
            ),
            dbc.Row(
                dbc.Col(
                    html.Div(
                        dcc.Loading([
                            html.Div(
                                [
                                    dbc.Card(
                                        [
                                            html.H2("Résultat de la requête"),
                                            html.Div(
                                                id='query-reminder',
                                                style={'fontStyle': 'italic'}
                                            ),
                                            html.Br(),
                                            html.Div(id='search-result'),
                                        ],
                                        id='query-result-card',
                                        class_name="common-card-style",
                                        style={'display': 'flex'}
                                    )
                                ], style={'display': 'none'},
                                id="query-card-container",
                                className="common-container-style"
                            ),
                        ], type='graph'),
                        className="my-4 py-4",
                    ),
                    width={"size": 8, "offset": 2},
                ),
            ),
        ],
        fluid=True,
        className="py-3"
    ),
])
