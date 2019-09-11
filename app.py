from flask import Flask, render_template
import requests
import json
import urllib.request,urllib.parse,urllib.error
import pprint
from random import choice
from random import sample

app = Flask(__name__)

apikey="6KSAHML0KPXD"
search_term = "happy"
lmt = 1
pp = pprint.PrettyPrinter(indent=4)

@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return render_template('index.html', gif = gifSearch())

def gifSearch():
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))
    gif = r.json()['results']
    return gif[0]
    

gifSearch()
if __name__ == "__main__":
    app.run(debug=True)







# # our test search
# search_term = "love"

# # get the top 8 GIFs for the search term
# r = requests.get(
#     "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s" %   
#      (search_term, apikey, lmt, anon_id))

# if r.status_code == 200:
#     # load the GIFs using the urls for the smaller GIF sizes
#     pp = pprint.PrettyPrinter(indent=4)
#     top_8gifs = json.loads(r.content)
#     pp.pprint(top_8gifs) #pretty prints the json file.
#     for i in range(len(top_8gifs['results'])):
#         url = top_8gifs['results'][i]['media'][0]['gif']['url'] #This is the url from json.
#         print (url)
#         urllib.request.urlretrieve(url, str(i)+'.gif') #Downloads the gif file.
# else:
#     top_8gifs = None

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