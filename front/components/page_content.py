""" Page content component """

from dash import dcc, html

from front.components.header import header
from front.components.navbar import navbar
from front.components.footer import footer

app_layout = html.Div(className='content-wrapper', children=[
    header,
    navbar,
    dcc.Store(id='redirect-url'),
    dcc.Store(id='redirect-logout'),
    dcc.Location(id='url', refresh=False),
    html.Div(id="page-content"),
    footer
])
