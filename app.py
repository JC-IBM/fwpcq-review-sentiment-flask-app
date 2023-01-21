from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/getsentiment', methods=['POST'])
def getsentiment():
    # get the URL from the form
    url = request.form['url']

    # TODO:
    # Scrap the url
    # Get the reviews 

    # Varible used to store emotion results and emotion scores
    # Get the emotion classification result
    
    
    reviews= {pretty good}
    results= "Joy:0.2 \tSadness=0.2 \tAnger=0.2 \tdisgust=0.2 \tFear=0.2"
    score = [0.2,0.2,0.2,0.2,0.2]

    # Return template with data
    return render_template('getsentiment.html', url=url, reviews=reviews, results=results, score=score)

if __name__ == '__main__':
    app.run()


