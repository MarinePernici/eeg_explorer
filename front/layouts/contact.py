from dash import html, dcc
import dash_bootstrap_components as dbc
from front.layouts.title import title_container


contact_form_layout = html.Div([
    dbc.Container([
        dbc.Row(
            dbc.Col(
                title_container, width={"size": 8, "offset": 2},
            ),
        ),
        dbc.Row(
            dbc.Col(
                html.H2("Contactez-nous", className="text-center mb-4"),
                width=12
            )
        ),
        dbc.Row(
            dbc.Col([
                dbc.Label("Nom", html_for="contact-name"),
                dbc.Input(type="text", id="contact-name", placeholder="Entrez votre nom", value=""),
            ], width=12, lg=6), justify="center"
        ),
        dbc.Row(
            dbc.Col([
                dbc.Label("Email", html_for="contact-email"),
                dbc.Input(type="email", id="contact-email", placeholder="Entrez votre email", value=""),
            ], width=12, lg=6), justify="center"
        ),
        dbc.Row(
            dbc.Col([
                dbc.Label("Sujet", html_for="contact-subject"),
                dbc.Input(type="text", id="contact-subject", placeholder="Sujet de votre message", value=""),
            ], width=12, lg=6), justify="center"
        ),
        dbc.Row(
            dbc.Col([
                dbc.Label("Message", html_for="contact-message"),
                dbc.Textarea(id="contact-message", placeholder="Votre message", rows=4),
            ], width=12, lg=6), justify="center"
        ),
        dbc.Row(
            dbc.Col([
                dbc.Button("Envoyer", color="primary", id="contact-submit", className="mt-2", style={'width': '100%'}),
                html.Div(id='form-output')
            ], width=2), justify="center"
        ),
    ], fluid=True),
])
