from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page changed at 1:08PMPT on 4/26/2019'

@app.route('/hello')
def hello():
    return 'Hello, World'
	
if __name__ == '__main__':
  app.run()
