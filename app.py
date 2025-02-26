from flask import flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home(): 
    return "<h1>Jeff's Flask App</h1>"

if __name__ == "__main__":
    app.run()