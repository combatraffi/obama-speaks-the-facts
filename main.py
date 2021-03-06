import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def damnitobaaama(ourfact):
    URL2 = "http://talkobamato.me/synthesize.py?"
    r = requests.post(URL2, {'input_text': ourfact}, allow_redirects=False)
    return r.headers['Location']


@app.route('/')
def home():
    fact = get_fact()
    body = damnitobaaama(fact)

    return Response(response=body, mimetype='text/plain')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

#I DID SOMEHTING BEFORE CLASS!