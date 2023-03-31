
import pyttsx3
# command line
#py -m pip install pyttsx3
#py -m pip install flask
#py -m pip install gunicorn
#py -m pip freeze > requirements.txt

from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Nguyen Cong Tam</h1>"

@app.route("/login")
def login():
    return "<h1>Login Nguyen Cong Tam</h1>"

#app.run(host="127.0.0.1", port=5001)
if __name__ == '__main__':
    app.run()