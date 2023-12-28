""" Navbar component """

import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Accueil", href="/home", active="exact")),
        dbc.NavItem(dbc.NavLink("Explorer", href="/explorer", active="exact")),
        dbc.NavItem(dbc.NavLink("Se connecter", href="/login", active="exact")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Mon historique", href="/profile/history"),
                dbc.DropdownMenuItem("Mes coordonnées", href="/profile/edit"),
                dbc.DropdownMenuItem("Supprimer le compte", href="/profile/delete"),
            ],
            nav=True,
            in_navbar=True,
            label="Mon compte",
            menu_variant="dark",
            align_end=True,
        ),
    ],
    color="#00152e",
    dark=True,
)