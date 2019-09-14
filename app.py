from flask import Flask, render_template, request
import requests
import json
import pprint
from random import choice
from random import sample

""" Settings for server, api and pretty print """
app = Flask(__name__)
pp = pprint.PrettyPrinter(indent=4)
params = {
    "q" : "Im not sure how this built in works??",
    "apikey" : "6KSAHML0KPXD",
    "lmt" : 10
}

""" Route for the home page """
@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return render_template('index.html', gif = gifSearch())

""" Main function for the Gif search """
def gifSearch():
    search = request.args.get('search')
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, params['apikey'], params['lmt']))
    gif = r.json()['results']
    return gif[1]
    

if __name__ == "__main__":
    app.run(debug=True)


"""Return homepage."""
    # TODO: Extract the query term from url using request.args.get()

    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'

    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'


"""
# our test search
search_term = "love"

# get the top 8 GIFs for the search term
r = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s" %   
     (search_term, apikey, lmt, anon_id))

if r.status_code == 200:
    # load the GIFs using the urls for the smaller GIF sizes
    pp = pprint.PrettyPrinter(indent=4)
    top_8gifs = json.loads(r.content)
    pp.pprint(top_8gifs) #pretty prints the json file.
    for i in range(len(top_8gifs['results'])):
        url = top_8gifs['results'][i]['media'][0]['gif']['url'] #This is the url from json.
        print (url)
        urllib.request.urlretrieve(url, str(i)+'.gif') #Downloads the gif file.
else:
    top_8gifs = None

@app.route('/gifSearch')
def get_gif():

    name = request.args.get('name')
    show_gifs = request.args.get('show_gifs')
    print('show_gifs:', show_gifs)
    gifs_to_show = sample(gifs)

    return render_template(
        'gifs.html', 
        name=name, 
        show_gifs=show_gifs, 
        gifs=gifs_to_show)   
"""