# Importing necessary libraries
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

#Loading and manipulating the dataset
df = pd.read_csv('ideas_db.csv')
df = df[df['Trinn']!='1_Pending']
df['Dato'] = pd.to_datetime(df['Dato'])
df = df.assign(År = df['Dato'].dt.year,
               Månder = df['Dato'].dt.month_name())
df_area = df.groupby(by=['År', 'Månder', 'Linje', 'Område']).agg(Kaizens = ('ID', 'count')).reset_index()
df_comp = df.groupby(by=['År', 'Linje', 'Trinn']).agg(Status = ('ID', 'count')).reset_index()

#Generating external style sheet
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

# Creating the Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Setting up the app layout
app.layout = html.Div(children=[
    html.H1(children='Kaizen Management Dashboard',  className='header-title'),

    html.Div(children=[
        dcc.Dropdown(id='Linje', options=[{'label': i, 'value': i} for i in df_area['Linje'].unique()], value='J4')],
        className='drop-down'),

    html.Div(children=[
        html.Div(children=[dcc.Graph(id='kaizens-graph')], className='bar-chart'),
        html.Div(children=[dcc.Graph(id='status-graph')], className='bar-chart')
    ], className='graphs-containers')
    
], className='main-layout')

# Setting up the callback function
@app.callback(
    Output(component_id='kaizens-graph', component_property='figure'),
    Output(component_id='status-graph', component_property='figure'),
    Input(component_id='Linje', component_property='value')
)
def update_graphs(selected_line):
    df_kaizens = df_area[df_area['Linje']==selected_line]
    df_completed = df_comp[df_comp['Linje']==selected_line]
    
    fig_1 = px.bar(df_kaizens, x='Månder', y='Kaizens',
                    color='Område', title=f'Generated Kaizens in {selected_line}',
                    category_orders={'Månder': ['May', 'June', 'July', 'August']},
                    range_y=[0,25])
    fig_1.add_hline(y=20)

    fig_2 = px.bar(df_completed, x='Trinn', y='Status',
                title=f'Completed Kaizens in {selected_line}')

    return fig_1, fig_2

# Running in local server
if __name__ == '__main__':
    app.run_server(debug=True)