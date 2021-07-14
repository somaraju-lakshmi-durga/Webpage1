from flask import *  
app = Flask(__name__)  

@app.route('/')
def welcome():
    lang = ['python', 'java', 'c++', 'html', 'english', 'telugu']
    return render_template('main.html', lang1 = lang)

@app.route('/display')  
def login(): 
    
    render_template('static/display.html' )

   
if __name__ == '__main__':  
   app.run(debug = True)  