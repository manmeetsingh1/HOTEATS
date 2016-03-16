
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results/')
def dashboard():
    return render_template('results.html')

import urllib2
import json
locu_api_key = 'dad8814e20be289b1b53b60ca73c7e3735574370'

#def locu_search(query):
#	api_key = locu_api_key
#	url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
#	locality = query.replace(' ', '%20')
#	final_url = url + "&locality=" + locality + "&category=restaurant"
#	json_obj = urllib2.urlopen(final_url)
#	data = json.load(json_obj)
#	for item in data['objects']:
#		print item['name'], item['phone']

@app.route("/locu/")
def locu():
	api_key = locu_api_key
	url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
	locality = "New York".replace(' ', '%20')
	final_url = url + "&locality=" + locality + "&category=restaurant"
	json_obj = urllib2.urlopen(final_url)
	data = json.load(json_obj)
	for item in data['objects']:
		return item['item'], item['phone']

@app.route("/hello/")
def hello():
	return render_template('hello.html')
	
@app.route('/getTestImage/')
def getTestImage():

    url = "https://www.google.de/images/srpr/logo11w.png"

    response = urllib2.urlopen(url)
    img = response.read()
    response.close()

    return app.response_class(img, mimetype='image/png')



if __name__ == '__main__':
    app.run(debug=True)
