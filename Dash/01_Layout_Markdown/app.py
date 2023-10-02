# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
from flask import Flask


server = Flask(__name__)
app = Dash(__name__, server=server)

markdown_text = '''
### Dash und Markdown Text anstatt HTML-Elemente zu verwenden

Dash Apps können Markdown verwenden. 
Dash nutzt die [CommonMark](http://commonmark.org/)
Spezifikation.    
Siehe auch das [60 Sekunden Markdown Tutorial](http://commonmark.org/help/)  

# Überschrift H1
## Überschrift H2
- List - Element
- List - Element 2

1. Geordnete Liste
2. Geordnete Liste

[Link zu YouTube](https://www.youtube.de/)

*Schräger Text*  
** Fetter Text **  
Zeilenumbruch mit 2 Leerzeichen am Satzende !  
![Bildtext](https://cdn.pixabay.com/photo/2016/11/08/05/20/sunset-1807524_1280.jpg)
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text),
    html.Img(alt="Test", src="https://cdn.pixabay.com/photo/2016/11/08/05/20/sunset-1807524_1280.jpg")
])

if __name__ == '__main__':
    app.run(debug=False)
