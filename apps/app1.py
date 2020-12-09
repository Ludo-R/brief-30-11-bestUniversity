#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:05:53 2020

@author: randon
"""

import dash_table
import pandas as pd
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px


df = pd.read_csv('timesData.csv')
 
dfValue = df
dfValue.income = pd.to_numeric(dfValue.income, errors='coerce')

grouped = dfValue.groupby('country')
y=grouped['income'].agg(np.mean).sort_values(ascending=False).iloc[:50]
print (y)
print ("______")
print (y.index.get_level_values(0).tolist())
print ("______")

trace = go.Bar(
                x = y.index.get_level_values(0).tolist(),
                y = y,
                name = "Le score universitaire pour le transfert de connaissances par pays",
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                             line = dict(color ='rgb(0,0,0)',width =1.5)),
                text = y.index.get_level_values(0).tolist())

layout = go.Layout(barmode = "group")
fig = go.Figure(data = trace, layout = layout)


colors = {
    'background': 'black',
    'text': '#7FDBFF'
}

layout = html.Div(children=[
    html.Div(children=[
        html.H1(
            children='TOP 50 par pays',
            style={
                'textAlign': 'center',
                'color':'grey'
                }
            )
        ]),

    html.Div(children=[
        html.H1(
            children='Income TOP',
            style={
                'textAlign': 'center'
                }
            )
        ]),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
        ),
    
    html.Div(children=[
        html.H1(
            children='International TOP',
            style={
                'textAlign': 'center'
                }
            )
        ]),

    ],style={'textAlign': 'center'})
