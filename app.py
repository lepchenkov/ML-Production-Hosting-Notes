from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Software 2.0 is coming!</h1>"

if __name__ == '__main__':
    app.run(debug=True)


# ngrok
# download and unzip ngrok file into the some repo
# go to this repo
# run ./ngrok http 5000   if you want to expose 5000 port where
# your local server is running