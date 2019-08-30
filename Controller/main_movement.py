from flask import Flask
from flask_ask import session, question, statement, Ask
from controllerTemplates import query

app = Flask(__name__)

@app.route("/")
def homePage():
    return "This is the home page where all the utterances will be shown."

ask = Ask(app,"/")

@ask.launch
def statingIntro():
    response = query["welcome"]
    return question(response)

if __name__ == "__main__":
    app.run(port=4000,debug=True)
    