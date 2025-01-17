import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

app = Dash(__name__)

# Load data
skill_data = pd.read_json("../data/skill_analysis.json", typ='series')

# Create bar chart
fig = px.bar(
    skill_data, x=skill_data.index, y=skill_data.values,
    labels={"x": "Skill", "y": "Frequency"},
    title="Skill Frequency in Job Postings"
)

# Define layout
app.layout = html.Div([
    html.H1("Job Market Analyzer"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
