from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    body = db.Column(db.String(500))

    def __init__(self, name, body):
        self.name = name
        self.body = body

@app.route('/', methods = ['GET'])
def full_blog():
    return render_template("full_blog.html")

@app.route('/', methods = ['POST'])
def new_post():
    return render_template("new_post.html")


if __name__ == '__main__':
    app.run()

