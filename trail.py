from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "<h1>hello, this is our first flask website</h1>" ;  
  
if __name__ =='__main__':  
    app.run(debug = True)  




from flask import  *
app = Flask(__name__)  
@app.route('/')  
def message():  
      return render_template('index.html')    
if __name__ == '__main__':  
   app.run(debug = True)  