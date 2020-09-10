# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:27:36 2020

@author: Paras.Taneja
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


df = pd.read_excel('Index.xlsx',index_col=0)
index_options=['--All Indices--','SPX','NDX','RTY']

app = dash.Dash()
server = app.server

app.layout = html.Div([
    html.H2("Index Series"),
    html.Div(
        [
            dcc.Dropdown(
                id="Index",
                options=[{
                    'label': i,
                    'value': i
                } for i in index_options],
                value='All Indices'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='example-graph'),
])

@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('Index', 'value')])

def update_graph(Index):
    data=[]
    if Index == "--All Indices--":
        df_plot = df.copy(deep=True)
        trace1 = go.Scatter(x=df_plot.index, y=df_plot['SPX'], name='SPX')
        trace2 = go.Scatter(x=df_plot.index, y=df_plot['RTY'], name='RTY')
        trace3 = go.Scatter(x=df_plot.index, y=df_plot['NDX'], name='NDX')
        data=[trace1,trace2,trace3]
    else:
        df_plot = df[[Index]]
        trace1 = go.Scatter(x=df_plot.index, y=df_plot[Index], name=Index)
        data=[trace1]
    
    
    return {
        'data': data,
        'layout':
        go.Layout(xaxis={'title': 'Time'},
                    yaxis={'title': 'Levels'})
    }


if __name__ == '__main__':
    app.run_server()
