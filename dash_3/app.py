
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Cargar datos desde el archivo
df_new_data = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    html.H1("Dashboard de Análisis Socioeconómico", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Selecciona un género:"),
        dcc.Dropdown(
            id='dropdown-gender',
            options=[{'label': gender, 'value': gender} for gender in df_new_data['sex'].unique()],
            value='Mujer',
            clearable=True
        ),
    ], style={'width': '30%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Rango de edad:"),
        dcc.RangeSlider(
            id='range-age',
            min=df_new_data['edad'].min(),
            max=df_new_data['edad'].max(),
            step=1,
            marks={i: str(i) for i in range(df_new_data['edad'].min(), df_new_data['edad'].max()+1, 10)},
            value=[df_new_data['edad'].min(), df_new_data['edad'].max()]
        ),
    ], style={'width': '90%', 'padding': '20px'}),

    dcc.Graph(id='bar-education-income'),
    dcc.Graph(id='scatter-education-income')
])

# Callback para actualizar los gráficos
@app.callback(
    [Output('bar-education-income', 'figure'),
     Output('scatter-education-income', 'figure')],
    [Input('dropdown-gender', 'value'),
     Input('range-age', 'value')]
)
def update_dashboard(selected_gender, age_range):
    # Filtrar los datos según las selecciones
    filtered_data = df_new_data[
        (df_new_data['sex'] == selected_gender) &
        (df_new_data['edad'] >= age_range[0]) &
        (df_new_data['edad'] <= age_range[1])
    ]
    
    # Gráfico de barras: Promedio de ingreso mensual por nivel educativo
    fig_education_income = px.bar(
        filtered_data.groupby('nivel_edu')['ingreso_mensual'].mean().reset_index(),
        x='nivel_edu', y='ingreso_mensual',
        title='Promedio de Ingreso Mensual por Nivel Educativo',
        labels={'nivel_edu': 'Nivel Educativo', 'ingreso_mensual': 'Ingreso Promedio'}
    )
    
    # Gráfico de dispersión: Relación entre años de escolaridad y el ingreso mensual
    fig_scatter = px.scatter(
        filtered_data, x='anios_esc', y='ingreso_mensual',
        color='nivel_edu',
        title='Relación entre Años de Escolaridad e Ingreso Mensual',
        labels={'anios_esc': 'Años de Escolaridad', 'ingreso_mensual': 'Ingreso Mensual'}
    )
    
    return fig_education_income, fig_scatter

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
