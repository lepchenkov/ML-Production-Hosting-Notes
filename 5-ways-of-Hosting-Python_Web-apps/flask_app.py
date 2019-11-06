"""
Talk by Andrew Baker on how to host python web applications.
https://www.youtube.com/watch?v=vGphzPLemZE
"""



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




# Serverless
# The idea is that the code will run only if it is needed
# AWS lambda 
# Zappa is a framework for deployment
# pip install zappa
# zappa init
# then ask all the questions
# zappa deploy production
# zappa makes a lot of APIs call to AWS services
# zappa creates a S3 bucket


# Virtual Machines
# create an instance of ubuntu VM
# VMs we are creating a fake hardware and installing an operating
# system there
# sudo su
# apt install python-pip
# pip install virtualenv
# activate virtual env
# grab repo and clone in
# install requirements
# gunicorn hello:app --log-file - --bind.0.0.0.0:80



# Docker
# touch Dockerfile
###########################
# FROM python:3.5-onbuild

# EXPOSE 5000

# CMD gunicorn hello:app --log-file - --bind.0.0.0.0:5000
#################
# docker build - t atbaker/five-ways
# docker rn -p 5000:5000 atbaer/five-ways
# then push the docker container to the docker hub (that is 
# basically a github for docker containers)

