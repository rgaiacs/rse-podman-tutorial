from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    try:
        import requests

        r = requests.head('https://en.wikipedia.org/wiki/Special:Random', allow_redirects=True)
        
        return f"<p>Hello, World! Let's read <a href='{r.url}'>{r.url}</a>.</p>"
    except Exception as error:
        return str(error)
