import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.express as px

# Crear datos sintéticos
np.random.seed(42)
categories = ['Electrónica', 'Ropa', 'Alimentos', 'Hogar']
data = {
    'Fecha': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'Categoría': np.random.choice(categories, 365),
    'Ventas': np.random.randint(50, 500, 365),
    'Ciudad': np.random.choice(['Bogotá', 'Medellín', 'Cali', 'Barranquilla'], 365)
}
df = pd.DataFrame(data)
df['Mes'] = df['Fecha'].dt.month_name()

# Crear la app
app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    html.H1("Dashboard de Ventas", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Selecciona una categoría:"),
        dcc.Dropdown(
            id='dropdown-categoria',
            options=[{'label': cat, 'value': cat} for cat in categories],
            value='Electrónica',
            clearable=False
        ),
    ], style={'width': '30%', 'display': 'inline-block'}),
    
    dcc.Graph(id='ventas-mes'),
    
    dcc.Graph(id='ventas-ciudad')
])

# Callback para actualizar los gráficos
@app.callback(
    [Output('ventas-mes', 'figure'),
     Output('ventas-ciudad', 'figure')],
    [Input('dropdown-categoria', 'value')]
)
def actualizar_dashboard(categoria_seleccionada):
    # Filtrar datos por categoría
    df_filtrado = df[df['Categoría'] == categoria_seleccionada]
    
    # Gráfico de ventas por mes
    fig_mes = px.bar(
        df_filtrado.groupby('Mes')['Ventas'].sum().reset_index(),
        x='Mes', y='Ventas', title=f'Ventas Mensuales - {categoria_seleccionada}'
    )
    
    # Gráfico de ventas por ciudad
    fig_ciudad = px.pie(
        df_filtrado.groupby('Ciudad')['Ventas'].sum().reset_index(),
        names='Ciudad', values='Ventas', title=f'Ventas por Ciudad - {categoria_seleccionada}'
    )
    
    return fig_mes, fig_ciudad

# Ejecutar la app
if __name__ == '__main__':
    app.run_server(debug=True)
