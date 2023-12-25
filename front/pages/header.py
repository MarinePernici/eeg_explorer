""" layout for header """

from dash import html

header = html.Header(
    children=[
        html.Img(
            src='../assets/img/logo.png',
            style={'height': '100px'},
        ),
        html.Img(
            src='../assets/img/header.jpg',
            style={
                'height': '100px',
                'width': '100%',
                'objectFit': 'cover',
            },
        ),
    ],
    style={
        'width': '100%',
        'display': 'flex',
        'alignItems': 'center',
        'justifyContent': 'space-between'
    },
)
