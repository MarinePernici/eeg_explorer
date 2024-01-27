from dash import html, dcc
import dash_bootstrap_components as dbc
from pages.title import title_container


contact_form_layout = html.Div([
    dbc.Container([
        *title_container,
        dbc.Row(
            dbc.Col(
                html.H2("Contactez-nous", className="text-center mb-4"),
                width=12
            )
        ),
        dbc.Row(
            dbc.Col([
                dbc.Label("Nom", html_for="contact-name"),
                dbc.Input(
                    type="text",
                    id="contact-name",
                    placeholder="Entrez votre nom",
                    value=""
                ),
            ], width=12, lg=6), justify="center"
        ),
        dbc.Row(
            dbc.Col([
                dbc.Label("Email", html_for="contact-email"),
                dbc.Input(
                    type="email",
                    id="contact-email",
                    placeholder="Entrez votre email",
                    value=""
                ),
                dbc.FormFeedback(
                    "",
                    type="valid",
                    id='contact-email-feedback-valid'
                ),
                dbc.FormFeedback(
                    "",
                    type="invalid",
                    id='contact-email-feedback-invalid'
                ),
            ], width=12, lg=6), justify="center"
        ),
        dbc.Row(
            dbc.Col([
                dbc.Label("Sujet", html_for="contact-subject"),
                dbc.Input(
                    type="text",
                    id="contact-subject",
                    placeholder="Sujet de votre message",
                    value=""
                ),
            ], width=12, lg=6), justify="center"
        ),
        dbc.Row(
            dbc.Col([
                dbc.Label("Message", html_for="contact-message"),
                dbc.Textarea(
                    id="contact-message",
                    placeholder="Votre message",
                    rows=4
                ),
            ], width=12, lg=6), justify="center", className="mb-3"
        ),
        dbc.Row(
            dbc.Col([
                dbc.Button(
                    "Envoyer",
                    n_clicks=0,
                    color="primary",
                    id="contact-submit",
                    style={'width': '100%'}
                ),
            ], width=2), justify="center", className="mb-3"
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    id='form-output',
                    children=" ",
                    style={'textAlign': 'center'}
                ),
                width=12, lg=6
            ), justify="center",
        ),
    ], fluid=True, className="py-3"),
])
