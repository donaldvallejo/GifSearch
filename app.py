from flask import Flask, render_template, request
import requests
import json
import pprint
from random import choice
from random import sample

app = Flask(__name__)

apikey="6KSAHML0KPXD"
lmt = 10
pp = pprint.PrettyPrinter(indent=4)

@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return render_template('index.html', gif = gifSearch())

def gifSearch():
    search = request.args.get('search')
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, apikey, lmt))
    gif = r.json()['results']
    return gif[2]

if __name__ == "__main__":
    app.run(debug=True)




#Ben was here
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

