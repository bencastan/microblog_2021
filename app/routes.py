from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Benc'} # Fake object just for testing 
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Sydney!'
        },
        {
            'author': {'username':'Susan'},
            'body': 'The avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='Home', user=user, posts=posts)