#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:07:42 2020

@author: randon
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from app import app
from apps import app1, app2
import dash_table
from dash_extensions import Download
from dash_extensions.snippets import send_data_frame

df = pd.read_csv('timesData.csv')
df2016 = df[df.year == 2016]


app.layout = html.Div([
        # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    dcc.Link('Back to Data DLL Menu', href='/'),
    html.Br(),
    dcc.Link('Page 1', href='/apps/app1'),
    html.Br(),
    dcc.Link('Page 2', href='/apps/app2'),
        # content will be rendered in this element
    html.Div(id='page-content'),
    html.Div(children=[
        html.H1(
            children='Best University !',
            style={
                'textAlign': 'center',
                'color': 'grey'
                }
            ),


        ],style={'textAlign': 'center'}),
    html.Div([
        dash_table.DataTable(
            data=df2016.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df2016.columns],
            export_format='csv',
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'height': '400px',
                         'margin': '50px',
                         'textAlign':'center'},
            style_cell={
                'height': 'auto',
                'width': 'auto',
                'whiteSpace': 'normal',
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white'
                }
            )
        ],style={'textAlign': 'center'}),
])

#@app.callback(Output("download", "data"), [Input("btn", "n_clicks")])
#def generate_csv(n_clicks):
#    return send_data_frame(df.to_csv, filename="timesData.csv")




@app.callback(Output('page-content','children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True)