import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

df = pd.read_csv('tit.csv', delimiter=';')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#F0E68C',
    'text': '#0000FF',
    'font': "#FFFFFF",
    'Namme': '#FF0000'
}
fig = px.scatter(df, x="Fatalities", y="Race", color="Gender")
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig.show()
"""app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['Date'].min(),
        max=df['Date'].max(),
        value=df['Date'].min(),
        marks={str(Date): str(Date) for Date in df['Date'].unique()},
        step=None
    ),
])"""

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Анализ массовых стрельб в США за 2000-17 года',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Зависимость убийств в США от пола преступника, его рассовой принадлежности ', style={
        'textAlign': 'center',
        'color': colors['Namme']
    }),
html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=5,
    ),
    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )

])





if __name__ == '__main__':
    app.run_server(debug=True)
