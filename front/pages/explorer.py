import dash_bootstrap_components as dbc
from dash import html, dcc
from pages.title import title_container

explorer_layout = html.Div([
    title_container,
    html.Div([
        html.P("Ceci est la page d'exploration de notre application."),
        dbc.Textarea(id='query', rows=3, placeholder='Ecrivez ici votre requête'),
        html.Br(),
        dbc.Button('Lancer la requête', n_clicks=0, id='search-button'),
        dcc.Loading([
            html.Div(
                [
                    dbc.Card(
                        [
                            html.H2("Résultat de la requête"),
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
    ], id="explore-container",
    className="common-container-style"),
], style={'width': '95%', 'margin': 'auto', 'align-items': 'center', 'justify-content': 'center'})

