

from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
   return "Hello TMC",401

   
if __name__ == '__main__':
   app.run(debug=True)
