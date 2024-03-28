import pymongo
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import threading
connection_string = "mongodb+srv://EddieT26:@cluster0.ktcqfar.mongodb.net/test"

client = pymongo.MongoClient(connection_string)
db = client["nsf_projects"]
collection = db["projects"]

all_projects = pd.read_csv(r"D:\Spring 2023 Senior Year\CS 4243 Large Scale Data Management\Assignments\Project\NSF_DIBBS_final3_output.csv")
collection.insert_many(all_projects.to_dict("records"))
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("NSF Projects Dashboard"),
    dcc.Dropdown(
        id='funding_agency_dropdown',
        options=[{'label': agency, 'value': agency} for agency in all_projects['Funding_agency'].unique()],
        value=None,
        placeholder='Select a Funding Agency',
        multi=True
    ),
    dcc.Graph(id='funding_agency_bar_chart'),
    dcc.Graph(id='keywords_bar_chart')
])

@app.callback(
    Output('funding_agency_bar_chart', 'figure'),
    Input('funding_agency_dropdown', 'value'))
def update_funding_agency_bar_chart(selected_agencies):
    if not selected_agencies:
        selected_agencies = all_projects['Funding_agency'].unique()
    
    data = all_projects[all_projects['Funding_agency'].isin(selected_agencies)]
    funding_agency_counts = data['Funding_agency'].value_counts().reset_index()
    funding_agency_counts.columns = ['Funding_agency', 'count']
    figure = px.bar(funding_agency_counts, x='Funding_agency', y='count', title='Number of Projects Funded by Agency')
    return figure

@app.callback(
    Output('keywords_bar_chart', 'figure'),
    Input('funding_agency_dropdown', 'value'))
def update_keywords_bar_chart(selected_agencies):
    if not selected_agencies:
        selected_agencies = all_projects['Funding_agency'].unique()
    
    data = all_projects[all_projects['Funding_agency'].isin(selected_agencies)]
    keywords = data['LDA_abstract_keywords'].explode().value_counts().reset_index().head(10)
    keywords.columns = ['LDA_abstract_keywords', 'count']
    figure = px.bar(keywords, x='LDA_abstract_keywords', y='count', title='Top Keywords Used in Projects')
    return figure

def run_dash_app():
    app.run_server(debug=False, use_reloader=False, host='0.0.0.0', port=8050)

if __name__ == '__main__':
    dash_thread = threading.Thread(target=run_dash_app)
    dash_thread.start()