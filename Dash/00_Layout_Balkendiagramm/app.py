# Die Web startest du nach dem Aufruf von "python3 app.py" im Browser unter: http://127.0.0.1:8050/ 


from dash import Dash, html, dcc
from flask import Flask
import plotly.express as px
import pandas as pd

server = Flask(__name__)
app = Dash(__name__, server=server)

# Pandas DataFrame erstellen:
df = pd.DataFrame({
    "Modelle": ["Golf", "Passat", "Tiguan", "Golf", "Passat", "Tiguan"],
    "Anzahl": [4, 1, 2, 2, 4, 5],
    "Stadt": ["Braunschweig", "Braunschweig", "Braunschweig", "Hannover", "Hannover", "Hannover"]
})

# Plotly Express für die Erstellung des Balkendiagramms nutzen
fig = px.bar(df, x="Modelle", y="Anzahl", color="Stadt", barmode="group")

# app.layout erstellt die HTML - Seite
app.layout = html.Div(children=[
    html.H1(children='Mein erstes Dashboard'),

    html.Div(children='''
        Dash: Ein Web-Applikation-Framework für deine Daten.
    '''),
    # dcc.Graph zeigt diverse Grafiken an, unter anderem auch Plotly Express Diagramme
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True) # Debug Mode anschalten
