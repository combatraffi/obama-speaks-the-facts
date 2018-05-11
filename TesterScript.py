#testerscript.py

import requests

URL = "http://talkobamato.me"
URL2 = "http://talkobamato.me/synthesize.py?"
message = 'My name is Megan Kuchan'
r = requests.post(URL2, {'input_text': message}, allow_redirects = False)
print(r.headers['Location'])