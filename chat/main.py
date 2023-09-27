from flask import Flask, request
from engine import engine

app = Flask("app")


@app.route('/')
def hello(): 
    with open("index.html", "r", encoding="utf-8") as f:
        text = f.read()
    return text

@app.route('/ask')
def ask():
    q = request.args.get("q")
    print(q)
    ans = engine.ask(q)
    return str(ans).replace('\n', '<br>').replace('\t', '&nbsp;&nbsp;&nbsp;&nbsp;')