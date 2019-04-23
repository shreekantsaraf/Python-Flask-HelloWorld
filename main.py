from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
  return 'Hey its Python Flask application deployed by Shree!'

@app.route('/about')
def about():
  return 'Hey its about route in Python Flask application!'
	
if __name__ == '__main__':
  app.run()
