from flask import Flask, render_template, request

'''

    It creates an instance of the Flask class,
    which will be your WSGI (Web server gateway interface) application

'''

## WSGI application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html> <h1> Hii Hardik  </h1> </html>"

@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")


    
@app.route('/submit',methods=['POST'])
def submit():
    name = request.form['name']
    return f'Welcome {name}'    
        


@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True, port=8080)