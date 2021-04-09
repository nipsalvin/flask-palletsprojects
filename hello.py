from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world ():
    return 'Hello, World'

@app.route('/')
def index():
    return 'Index page'

@app.route('/hello')
def hello(hello):
    return'Hello Wrld'

from markupsafe import escape

@app.route('/user/<username>')
def show_user_profiles(username):
    #show user profile for that user
    return'user %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
