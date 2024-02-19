""" Navbar component """

import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(
                "Accueil",
                href="/home",
                active="exact",
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Explorer",
                href="/explorer",
                active="exact",
                disabled=True,
                id="explorer_link"
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Se connecter",
                href="/login",
                active="exact",
                id="login_link"
            )
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem(
                    "Mon historique",
                    href="/profile/history",
                    disabled=True,
                    id="history_link",
                ),
                dbc.DropdownMenuItem(
                    "Mes informations",
                    href="/profile/edit",
                    disabled=True,
                    id="edit_link",
                ),
                dbc.DropdownMenuItem(
                    "Supprimer le compte",
                    href="/profile/delete",
                    disabled=True,
                    id="delete_link",
                ),
            ],
            nav=True,
            in_navbar=True,
            label="Mon compte",
            menu_variant="dark",
            align_end=True,
            disabled=True,
            id="account_dropdown"
        ),
    ],
    color="#1a1950",
    dark=True,
)
