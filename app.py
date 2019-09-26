from pymongo import MongoClient
client = MongoClient()
db = client.Playlister
playlists = db.playlists
from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     """Return Homepage"""
#     return render_template('home.html', msg = 'Flask is Cool!')

# playlists = [
#     { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
#     { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' },
#     { 'title': 'Celtic Music', 'description': 'Tir na Nog' }
# ]

@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists.find())

if __name__ == '__main__':
    app.run(debug=True)
