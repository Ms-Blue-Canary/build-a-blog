from flask import Flask, request, redirect, render_template, session, flash
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
def blog_entries():
    blogs = Blog.query.all()
    post_id = request.args.get('id')
    if (post_id):
        post = Blog.query.get(post_id)
        return render_template("one_post.html", post=post)
    else:
        full_blog = Blog.query.all()
        return render_template('full_blog.html', full_blog=full_blog)

@app.route('/new_post', methods = ['GET', 'POST'])
def new_post():
    if request.method == 'POST':    
        new_name = request.form['name']
        new_body = request.form['body']
        new_post = Blog(new_name, new_body)

        if new_name == "":
            flash ("You forgot a title", 'error')

        if new_body == "":
            flash("You forgot to write something", 'error')

    else:
        db.session.add(new_post)
        db.session.commit()
        return redirect("new_post.html")

if __name__ == '__main__':
    app.run()

