from flask import Flask, request, redirect, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:blogz@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/', methods=['GET','POST'])
def index():
   
   return render_template('base.html', title="Build a Blog")

@app.route('/newpost', methods=['GET', 'POST'])
def new_post():
    if  request.method == 'GET':
        return render_template("newpost.html")
    
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
 
    post = Blog(title=title, body=body)
    db.session.add(post)
    db.session.commit()

    return render_template('base.html', title="Build a Blog")
app.secret_key = 'Thiswillbeagreatjourney2win'

if __name__ == '__main__':
    app.run()