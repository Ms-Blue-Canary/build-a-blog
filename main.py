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

@app.route('/blog', methods=['GET'])
def full_blog():
    post_id = request.args.get('id')
    if (post_id):
        post = Blog.query.get(post_id)
        return render_template("one_post.html", post=post)

@app.route('/new_post', methods = ['GET', 'POST'])
def new_post():
    if request.method == 'POST':    
        new_name = request.form['name']
        new_body = request.form['body']
        new_post = Blog(new_name, new_body)

        new_name_error = ""
        new_body_error = ""

        if new_name == "":
            new_name_error = "You forgot a title"

        if new_body == "":
            new_body_error = "You forgot to write something"

    else:
        return render_template("new_post.html")

if __name__ == '__main__':
    app.run()

