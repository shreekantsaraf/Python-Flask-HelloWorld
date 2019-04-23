from flask import Flask
app = Flask(__name__)

@app.route('/about')
def about():
  return 'Hey its about route in Python Flask application!'

 posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return 'Hey its Home or default route in  Python Flask application!'
  
if __name__ == '__main__':
  app.run()
