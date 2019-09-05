from flask import Flask

from flask_ask import Ask, statement, question, session

from lightsTemplate import *

from serial import Serial
ser = Serial('/dev/ttyACM0',9600,timeout = None)


app = Flask(__name__)

ask = Ask(app, "/")

lastStatus = ""

@app.route("/")
def starting():
    return "<span style = color:blue>These are template lines:</span><br>--" + "<br>--".join(d.values())

@ask.launch

def launch_skill():

    welcome_msg = d["welcome"]
    return question(welcome_msg)

@ask.intent("describeIntent")

def description():
    about = d["about_the_skill"]
    ser.write(b'L')
    return question(about)

@ask.intent("switchingLights", convert={'key':str})

def switch_light(key):
    response = ''
    global lastStatus
    if key == "on" or key == "off":
        if lastStatus == key:
            response = "The light is already turned {0}".format(key)
        else:
            lastStatus = key
            response = d["switch_on_off_template"].format(key)
            if key=="on":
                ser.write(b'H')
            elif key == "off":
                ser.write(b'L')
    else:
        response = d["invalid_switch"]
    return question(response)

@ask.intent("AMAZON.HelpIntent")

def switch_help():
    response = d["help_template"]
    return question(response)
@ask.intent("AMAZON.StopIntent")

def switch_stop():
    response = d["stop_template"]
    ser.write(b'L')
    return statement(response)

if __name__ == '__main__':

    app.run(port=8000,debug=True)