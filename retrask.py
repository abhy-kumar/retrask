from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "index"
@app.route("/projectfile")
def projectfile():
    return("projectfile")

if __name__ == "__main__":
	app.run()