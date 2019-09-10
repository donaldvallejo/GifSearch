from flask import Flask, request, render_template
from random import choice
from random import sample
app = Flask(__name__)

# gifs = ['stuff', 'things']

@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return render_template('index.html')


# @app.route('/gifSearch')
# def get_gif():
#     """Give the user a gif"""
#     name = request.args.get('name')
#     show_gifs = request.args.get('show_gifs')
#     print('show_gifs:', show_gifs)
#     gifs_to_show = sample(gifs)

#     return render_template(
#         'gifs.html', 
#         name=name, 
#         show_gifs=show_gifs, 
#         gifs=gifs_to_show)   