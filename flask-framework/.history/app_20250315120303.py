from flask import Flask

'''

    It creates an instance of the Flask class,
    which will be your WSGI (Web server gateway interface) application

'''

## WSGI application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome Man!"

if __name__ == '__main__':
    app.run(debug=True, port=8080)