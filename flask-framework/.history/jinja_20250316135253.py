### Jinja2 Template Engine
'''
{{}} expressions to print output in html

{%...%} conditions, for loops etc

{#...#} this is for comments


'''


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


    
# @app.route('/submit',methods=['POST'])
# def submit():
#     name = request.form['name']
#     return f'Welcome {name}'   

## variable rule
@app.route('/success/<int:score>') #  assigning a rule to the variable 'score' that it should be only int
def success(score):
    res =""
    if score >=50:
        res = "PASSED"
    else :
        res = "FAILED" 
        
    return render_template('result.html', results=res)



@app.route('/successres/<int:score>')
def successres(score):

    res =""
    if score >=50:
        res = "PASSED"
    else :
        res = "FAILED" 
        
    exp = {'score' : score, "res" : res}    
        
    return render_template('result1.html', results=exp)


## if condition
@app.route('/successif/<int:score>')
def success_if(score):
    
    return render_template('result2.html', results=score)



@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', results=score)

@app.route('/submit',method=['POST', 'GET'])
def get_results():
    
    return render_template('get_result.html')
    
 
        


@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True, port=8080)