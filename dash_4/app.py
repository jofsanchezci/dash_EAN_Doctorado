# Instala Dash si no lo tienes
# pip install dash plotly pandas

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Leer datos
df = pd.read_csv("superservicios_dashboard_data.csv")

# Crear app Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Accidentes Superservicios"),
    
    dcc.Dropdown(
        id='anio-dropdown',
        options=[{'label': str(a), 'value': a} for a in sorted(df['ANIO'].dropna().unique())],
        value=2014,
        clearable=False
    ),
    
    dcc.Graph(id='grafico-lesiones'),

    dcc.Graph(id='grafico-causas')
])

@app.callback(
    Output('grafico-lesiones', 'figure'),
    Output('grafico-causas', 'figure'),
    Input('anio-dropdown', 'value')
)
def actualizar_graficos(anio):
    df_filtrado = df[df['ANIO'] == anio]
    
    fig1 = px.histogram(df_filtrado, x='TIPO_LESION', color='TIPO_LESION',
                        title=f"Tipos de Lesión en {anio}")
    
    fig2 = px.histogram(df_filtrado, x='CAUSA_ACCIDENTE', color='CAUSA_ACCIDENTE',
                        title=f"Causas de Accidentes en {anio}")
    
    return fig1, fig2

if __name__ == '__main__':
    app.run_server(debug=True)
