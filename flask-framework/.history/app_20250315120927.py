from flask import Flask, render_template

'''

    It creates an instance of the Flask class,
    which will be your WSGI (Web server gateway interface) application

'''

## WSGI application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html> <h1> Hii Hardik  </h1> </html>"

@app.route('/index')
def index():
    return "Hello index!"

if __name__ == '__main__':
    app.run(debug=True, port=8080)