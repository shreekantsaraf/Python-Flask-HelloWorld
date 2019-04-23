from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
  return 'Hey its Python Flask application deployed by Shree - home route!'

@app.route("/about")
def about():
  return 'Hey its Python Flask application -- about route!'
	
if __name__ == '__main__':
  app.run()
