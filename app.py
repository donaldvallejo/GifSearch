from flask import Flask, render_template, request
import requests
import json
import pprint
from random import choice
from random import sample

""" Settings for server, api and pretty print """
app = Flask(__name__)
pp = pprint.PrettyPrinter(indent=1)
params = {
    "q" : "Im not sure how this built-in works??",
    "apikey" : "6KSAHML0KPXD",
    "lmt" : 10
}

""" Route for the home page """
@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return render_template('index.html', gifs = gifSearch())

""" Main function for the Gif search """
def gifSearch():
    search = request.args.get('search')
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, params['apikey'], params['lmt']))    

    
    """ Loop for printed Gifs """
    gifList = []
    gif = r.json()
    resultsList = gif['results']

    for gifs in resultsList:
        medialist = gifs['media']
        for medias in medialist:
            gifList.append(medias['gif']['url'])
            pp.pprint(medias['gif']['url'])

    pp.pprint(['results'])

    return gifList

    

    
    # """ Route Test's """
    # class AppTests(unittest.TestCase): 

    # def setUp(self):
    #     self.app = app.test_client()
    #     self.app.testing = True 

    # def test_home_status_code(self):
    #     result = self.app.get('/') 

    #     self.assertEqual(result.status_code, 200)
    #     self.assertEqual(result.status_code, 500)
    #     self.assertEqual(result.status_code, 404)

if __name__ == "__main__":
    app.run(debug=True)