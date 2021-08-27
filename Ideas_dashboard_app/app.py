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
df = df.assign(År = df['Dato'].dt.year.astype(str),
               Månder = df['Dato'].dt.month_name())
df_area = df.groupby(by=['År', 'Månder', 'Linje', 'Område']).agg(Kaizens = ('ID', 'count')).reset_index()
df_comp = df.groupby(by=['År', 'Linje', 'Trinn', 'Kriterier']).agg(Status = ('ID', 'count')).reset_index()
df_person = df.groupby(by=['År', 'Linje', 'Trinn', 'Navn']).agg(Count = ('ID', 'count')).reset_index()

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
    html.H1(children='Ideas Management Dashboard',  className='header-title'),

    html.Div(children=[
        html.H3(children='Year', className='dropdown-title'),
        html.H3(children='Line', className='dropdown-title')
    ], className='dropdown-heading'),

    html.Div(children=[
        html.Div(children=[
            dcc.Dropdown(id='Year', options=[{'label': i, 'value': i} for i in df_area['År'].unique()],
            value='2021', clearable=False)], className='dropdown'),
        html.Div(children=[
            dcc.Dropdown(id='Line', options=[{'label': i, 'value': i} for i in df_area['Linje'].unique()],
            value='J4', clearable=False)], className='dropdown'),
    ], className='dropdown-container'),

    html.Div(children=[
        html.Div(children=[dcc.Graph(id='kaizens-graph')], className='bar-chart'),
        html.Div(children=[dcc.Graph(id='status-graph')], className='bar-chart'),
        html.Div(children=[dcc.Graph(id='p-graph')], className='bar-chart')
    ], className='graphs-container')
    
], className='main-layout')

# Setting up the callback function
@app.callback(
    Output(component_id='kaizens-graph', component_property='figure'),
    Output(component_id='status-graph', component_property='figure'),
    Output(component_id='p-graph', component_property='figure'),
    [Input(component_id='Year', component_property='value'),
    Input(component_id='Line', component_property='value')])

def update_graphs(selected_year, selected_line):

    df_kaizens = df_area[(df_area['År']==selected_year) & (df_area['Linje']==selected_line)].copy()
    df_completed = df_comp[(df_comp['År']==selected_year) & (df_comp['Linje']==selected_line)].copy()
    df_per = df_person[(df_person['År']==selected_year) & (df_person['Linje']==selected_line)].copy()
    
    fig_1 = px.bar(df_kaizens, x='Månder', y='Kaizens', color='Område',
                title=f'{selected_year} - Generated Ideas in {selected_line}',
                category_orders={'Månder': ['May', 'June', 'July', 'August']},
                range_y=[0,25])
    fig_1.add_hline(y=20)
    fig_1.update_layout(title_x=0.5)

    fig_2 = px.bar(df_completed, x='Trinn', y='Status', color='Kriterier',
                title=f'{selected_year} - Completed Ideas in {selected_line}',
                color_discrete_sequence=['#007FFF', '#2A9D8F', '#800080'])
    fig_2.layout.update(title_x=0.5) #showlegend=False,

    fig_3 = px.bar(df_per, x='Navn', y='Count', color='Trinn',
                title=f'{selected_year} - Generated Ideas per person in {selected_line}',
                color_discrete_sequence=['#007FFF', '#2A9D8F', '#800080'])
    fig_3.layout.update(title_x=0.5) #showlegend=False,


    return fig_1, fig_2, fig_3

# Running in local server
if __name__ == '__main__':
    app.run_server(debug=True)