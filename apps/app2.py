#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:09:48 2020

@author: randon
"""


import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from sklearn.decomposition import PCA
import plotly.express as px
import numpy as np
from sklearn import decomposition
from sklearn import preprocessing
from app import app

df = pd.read_csv("timesData.csv")
# choix du nombre de composantes à calculer
df2016 = df[df.year == 2016]
df2016.num_students  = [str(each).replace(',', '') for each in df2016.num_students]

y = df2016["university_name"]  

dfnums = df2016[['teaching', 'international', 'research', 'citations', 'income', 'total_score', 'num_students',  'student_staff_ratio','international_students' ]]
numeric_cols = ['teaching', 'international', 'research', 'citations', 'income', 'total_score', 'num_students', 'student_staff_ratio','international_students']
for col in numeric_cols:
    dfnums[col] = pd.to_numeric(dfnums[col], errors='coerce')
    
dfnums = dfnums.fillna(0)

n_components = 2

pca = PCA(n_components=n_components)
components = pca.fit_transform(dfnums)

total_var = pca.explained_variance_ratio_.sum() * 100

labels = {str(i): f"PC {i+1}" for i in range(n_components)}
labels['color'] = 'University name'

fig = px.scatter_matrix(
    components,
    color=y,
    dimensions=range(n_components),
    labels=labels,
    title=f'Total Explained Variance: {total_var:.2f}%',
)
fig.update_traces(diagonal_visible=False)

layout = html.Div(children=[
    html.Div(children=[
        html.H1(
            children='Analyse en Composante principale',
            style={
                'textAlign': 'center',
                'color':'grey'
                }
            )
        ]),
    dcc.Graph(
        id='example-graph-3',
        figure=fig
        ),
    html.Div(html.Img(src=app.get_asset_url('fig1.png'))),
    html.Div(html.Img(src=app.get_asset_url('fig2.png'))),
    html.Div(html.Img(src=app.get_asset_url('fig3.png'))),
    html.Div(html.Img(src=app.get_asset_url('fig4.png'))),

    ],style={'textAlign': 'center'}),
    
