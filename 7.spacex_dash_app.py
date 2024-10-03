# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                              options=[
                                                {'label': 'All Sites', 'value': 'ALL'},
                                                {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                                {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                                {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
                                                ],
                                                value='ALL',
                                                placeholder='Select a Lunch Site',
                                                searchable=True
                                            ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(
                                    id='payload-slider',
                                    min=min_payload,
                                    max=max_payload,
                                    step=1000,
                                    marks={
                                        int(min_payload): f'{int(min_payload)}',
                                        int(max_payload/4): f'{int(max_payload/4)}',
                                        int(max_payload/2): f'{int(max_payload/2)}',
                                        int(3*max_payload/4): f'{int(3*max_payload/4)}',
                                        int(max_payload): f'{int(max_payload)}'
                                    },
                                    value=[min_payload, max_payload]
                                ),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # Group and sum by successful launch
        grouped_df = spacex_df.groupby('Launch Site')['class'].sum().reset_index()
        # Pie Chart
        fig = px.pie(
            grouped_df,
            names='Launch Site', 
            title='Success Count for all launch sites',
            values='class'  
        )
    else:
        # Filter by launch sites
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        # Count failures and success
        success_counts = filtered_df['class'].value_counts().reset_index()
        success_counts.columns = ['class', 'count']
        success_counts['class'] = success_counts['class'].map({1: "Success", 0: "Failure"})
        # Pie Chart
        fig = px.pie(
            success_counts,
            values='count',
            names='class',
            title=f"Total Success vs Failure Launches for site {entered_site}"
        )
        fig.update_traces(marker=dict(colors=['red', 'green']))
    return fig
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [
        Input(component_id='site-dropdown', component_property='value'),
        Input(component_id='payload-slider', component_property='value')
    ]
)
def update_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    # Filtrar los datos según el rango de Payload
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered_df = spacex_df[mask]
    
    if entered_site == 'ALL':
        # Crear el Scatter Plot para todos los sitios
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Launch Site',
            title='Correlation between Payload and Success for All Sites',
            hover_data=['Booster Version']
        )
    else:
        # Filtrar los datos para el sitio seleccionado
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        # Crear el Scatter Plot para el sitio seleccionado
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='class',
            title=f'Correlation between Payload and Success for {entered_site}',
            hover_data=['Booster Version']
        )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
