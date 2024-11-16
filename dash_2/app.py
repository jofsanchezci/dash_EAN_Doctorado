
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Cargar datos desde el archivo
df_data = pd.read_excel('data1.xlsx', sheet_name='Data')

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    html.H1("Dashboard de Análisis de Empleados", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Selecciona un país:"),
        dcc.Dropdown(
            id='dropdown-country',
            options=[{'label': country, 'value': country} for country in df_data['Country'].unique()],
            value='United States',
            clearable=False
        ),
    ], style={'width': '30%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Selecciona un género:"),
        dcc.Dropdown(
            id='dropdown-gender',
            options=[{'label': gender, 'value': gender} for gender in df_data['Gender'].unique()],
            value='Male',
            clearable=True
        ),
    ], style={'width': '30%', 'display': 'inline-block', 'marginLeft': '10px'}),

    html.Div([
        html.Label("Selecciona un departamento:"),
        dcc.Dropdown(
            id='dropdown-department',
            options=[{'label': dept, 'value': dept} for dept in df_data['Department'].unique()],
            value='Engineering',
            clearable=True
        ),
    ], style={'width': '30%', 'display': 'inline-block', 'marginLeft': '10px'}),

    dcc.Graph(id='bar-ethnicity-salary'),
    dcc.Graph(id='scatter-age-salary')
])

# Callback para actualizar los gráficos
@app.callback(
    [Output('bar-ethnicity-salary', 'figure'),
     Output('scatter-age-salary', 'figure')],
    [Input('dropdown-country', 'value'),
     Input('dropdown-gender', 'value'),
     Input('dropdown-department', 'value')]
)
def update_dashboard(selected_country, selected_gender, selected_department):
    # Filtrar los datos según las selecciones
    filtered_data = df_data[
        (df_data['Country'] == selected_country) &
        (df_data['Gender'] == selected_gender) &
        (df_data['Department'] == selected_department)
    ]
    
    # Gráfico de barras: Salario promedio por etnicidad
    fig_ethnicity_salary = px.bar(
        filtered_data.groupby('Ethnicity')['Annual_Salary'].mean().reset_index(),
        x='Ethnicity', y='Annual_Salary',
        title='Salario Promedio por Etnicidad',
        labels={'Annual_Salary': 'Salario Promedio', 'Ethnicity': 'Etnicidad'}
    )
    
    # Gráfico de dispersión: Edad vs Salario por Etnicidad
    fig_age_salary = px.scatter(
        filtered_data, x='Age', y='Annual_Salary',
        color='Ethnicity',
        title='Relación entre Edad y Salario Anual',
        labels={'Age': 'Edad', 'Annual_Salary': 'Salario Anual'}
    )
    
    return fig_ethnicity_salary, fig_age_salary

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
