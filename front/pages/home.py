""" Layout for the home page of the application."""

import dash_bootstrap_components as dbc
from dash import html, dcc
from pages.title import title_container

home_layout = html.Div([
    dbc.Container(
        [
            title_container,
            dbc.Row([
                
                dbc.Col([
                    html.Div(
                        style={
                            'display': 'flex',  # Utiliser Flexbox
                            'align-items': 'center',  # Centrer verticalement
                            'justify-content': 'center',  # Centrer horizontalement
                            'background-color': '#1a1950',  # Fond coloré
                            'border-radius': '5px',  # Arrondir les coins
                            'height': '100%', # Hauteur 100%
                        },
                        children=html.Img(
                            src='../assets/img/logo.png',
                            style={
                                'max-width': '100%',
                                'max-height': '100%',
                                'border-radius': '5px',
                            },
                        ),
                    ),
                ], width=5, lg=3, md=3,
                className="mb-3 ms-3 d-flex flex-column justify-content-center ",
                style={'background-color': '#1a1950', 'border-radius': '5px',}
                ),
                dbc.Col(
                    html.Div(
                        dcc.Markdown("""
                            Découvrez EEG Explorer, **une application innovante
                            by Spectre Biotech**, la startup pionnière en
                            traitement automatisé du signal EEG.

                            - **Pourquoi EEG Explorer?**

                            _Notre mission_ : démocratiser la pratique
                            de l'EEG en clinique courante et faciliter
                            l'accès aux données EEG, une
                            ressource précieuse mais souvent sous-exploitée.
                            Avec EEG Explorer accédez simplement à **une vaste
                            collection d'enregistrements EEG**.
                            Grâce à l'intelligence artificielle intégrée,
                            interagissez avec notre base de données via de
                            simples questions en langage naturel.

                            - **Rejoignez l'aventure**

                            Que vous soyez un chercheur confirmé, un praticien
                            en quête de données cliniques ou un étudiant
                            passionné par l'étude du cerveau, **EEG Explorer
                            est conçu pour vous**.

                            _Avec EEG Explorer, franchissez le seuil
                            d'**une nouvelle ère de la recherche EEG**, où
                            les données sont vivantes, accessibles et
                            infiniment explorables._
                            """,
                            className='custom-list-style'
                        ), style={'text-align': 'justify'},
                    ),
                    width=12, lg=7, md=7, 
                    className="mb-3 d-flex flex-column justify-content-center"
                )
            ], style={'vertical-align': 'middle'}, className="d-flex align-items-stretch", justify="center",),
            dbc.Row([
                dbc.Col(
                    dbc.Button(
                        "Commencer l'exploration",
                        size='lg',
                        color="primary",
                        className="btn btn-lg",
                        href="/explorer",
                        id="start-exploration-button",
                        style={'width': '100%'},
                    ), width=12, lg={'size': 3, 'offset': 8}, md={'size': 3, 'offset': 8}, className='d-flex align-items-center mb-3',
                ),
            ], 
            # justify="end"
            ),
        ],
        fluid=True,
        className="py-3"
    )
])

# app_description = dcc.Markdown("""
# Découvrez EEG Explorer, une application innovante
# by Spectre Biotech, la startup pionnière en
# neurotechnologie. Notre mission : démocratiser
# l'accessibilité à l'électroencéphalographie, une
# ressource précieuse mais souvent sous-exploitée
# dans la pratique clinique courante. Avec EEG Explorer,
# nous ouvrons de nouvelles portes à la communauté
# scientifique et médicale en fournissant un accès
# simplifié à une vaste collection de plus de 5000
# enregistrements EEG.

# Chez Spectre Biotech, nous croyons en la force de la
# technologie pour transformer la recherche et les soins
# de santé. EEG Explorer incarne cette vision en intégrant
# l'intelligence artificielle de pointe, capable de
# comprendre et de traiter les requêtes en langage naturel.
# Cette interface intuitive élimine les barrières techniques
# et linguistiques, permettant aux utilisateurs de poser des
# questions complexes et de recevoir des réponses détaillées
# avec une facilité déconcertante.

# EEG Explorer est plus qu'une simple application ;
# c'est une extension de notre engagement à faire progresser
# la recherche en neurosciences. Que vous soyez un chercheur
# confirmé, un praticien en quête de données cliniques ou un
# étudiant passionné par l'étude du cerveau, EEG Explorer
# est conçu pour vous.
                
# Nous travaillons sans relâche pour
# que notre technologie soit à la fois puissante et accessible,
# afin que vous puissiez vous concentrer sur ce qui compte
# vraiment : faire avancer la science et améliorer les
# soins aux patients.

# Spectre Biotech est fière de vous inviter à rejoindre cette aventure
# en neurotechnologie. Avec EEG Explorer, franchissez le seuil
# d'une nouvelle ère de la recherche EEG, où les données sont
# vivantes, accessibles et infiniment explorables.
# """)


# app_description = dcc.Markdown('''
# **Découvrez une application innovante en
# neurotechnologie.** Notre mission : _démocratiser
# la pratique de l'EEG en clinique courante et faciliter
# l'accès aux données EEG_.
                
# ## Pourquoi EEG Explorer?
# - **Accès simplifié** à une vaste collection de plus
# de 5000 enregistrements EEG.
# - **Ouverture de nouvelles portes** pour la communauté
# scientifique et médicale.

# ## Technologie de Pointe
# - **Intégration de l'intelligence artificielle** pour
# une compréhension et un traitement en langage naturel.
# - **Interface intuitive** qui élimine les barrières
# techniques et linguistiques.
                
# ## Plus qu'une Application
# - **Outil de recherche et d'exploration** pour les
# chercheurs, praticiens et étudiants.
# - **Engagement fort** pour la progression de la
# recherche en neurosciences.

# ## Rejoignez l'Aventure
# **Spectre Biotech vous invite** à franchir le seuil
# d'une nouvelle ère de la recherche EEG.''')


# illustrations = dbc.Row(
#     [
#         dbc.Col(
#             html.Div([
#                 html.H5("Demandez Simplement", className="text-center"),
#                 html.Div(
#                     style={
#                         'width': '100%',   # Largeur de 100% du conteneur
#                         'padding-top': '100%',  # Padding-top de 100% pour maintenir un aspect carré
#                         'position': 'relative',
#                         'margin': '0 auto'  # Position relative pour le pseudo-élément
#                     },
#                     children=html.Img(
#                         src='assets/img/ask.png',
#                         style={
#                             'max-width': '100%',
#                             'max-height': '100%',
#                             'position': 'absolute',
#                             'top': '0',
#                             'bottom': '0',
#                             'left': '0',
#                             'right': '0',
#                             'margin': 'auto',
#                         },
#                     ),
#                 )
#             ]),
#         width={"size": 2, "offset": 2},
#         className="mb-3"
#         ),
#         dbc.Col(
#             html.Div([
#                 html.H5("Téléchargez les résultats", className="text-center"),
#                 html.Div(
#                     style={
#                         'width': '100%',   # Largeur de 100% du conteneur
#                         'padding-top': '100%',  # Padding-top de 100% pour maintenir un aspect carré
#                         'position': 'relative',
#                         'margin': '0 auto'  # Position relative pour le pseudo-élément
#                     },
#                     children=html.Img(
#                         src='assets/img/download.png',
#                         style={
#                             'max-width': '100%',
#                             'max-height': '100%',
#                             'position': 'absolute',
#                             'top': '0',
#                             'bottom': '0',
#                             'left': '0',
#                             'right': '0',
#                             'margin': 'auto',
#                         },
#                     ),
#                 )
#             ]),
#         width={"size": 2, "offset": 1},
#         className="mb-3"
#         ),
#         dbc.Col(
#             html.Div([
#                 html.H5("Rapidité et Précision", className="text-center"),
#                 html.Div(
#                     style={
#                         'width': '100%',   # Largeur de 100% du conteneur
#                         'padding-top': '100%',  # Padding-top de 100% pour maintenir un aspect carré
#                         'position': 'relative',
#                         'margin': '0 auto'  # Position relative pour le pseudo-élément
#                     },
#                     children=html.Img(
#                         src='assets/img/speed.png',
#                         style={
#                             'max-width': '100%',
#                             'max-height': '100%',
#                             'position': 'absolute',
#                             'top': '0',
#                             'bottom': '0',
#                             'left': '0',
#                             'right': '0',
#                             'margin': 'auto',
#                         },
#                     ),
#                 )
#             ]),
#         width={"size": 2, "offset": 1},
#         className="mb-3"
#         ),
#     ],
#     className="my-3"
# )
