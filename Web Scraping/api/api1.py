import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
        return "<h2>Distant Archive</h2><p>This site is a prototype API for distant reading of science fiction novels.</p>"

app.run()
