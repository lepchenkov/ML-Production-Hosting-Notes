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

# while ngrok is running there is a http://localhost:4040 url with a nice 
# admin dashboard where all the requessts that are coming are displayed 




# Heroku
# brew install heroku/brew/heroku
# "heroku login" command to login via browser
# create Procfile
# add requirements.txt
# add runtime.txt
# heroku create
# git push heroku master
# heroku open

