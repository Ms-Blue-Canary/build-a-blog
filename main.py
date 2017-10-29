from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = "It's_a_secret_to_everyone" 

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
        return render_template("one_post.html", new_post=post)
    else:
        full_blog = Blog.query.all()
        return render_template('full_blog.html', full_blog=full_blog)

@app.route('/new_post', methods = ['GET', 'POST'])
def new_post():
    post_id = request.args.get('id')
    if request.method == 'POST':    
        new_name = request.form['name']
        new_body = request.form['body']
    
        if new_name == "":
            flash ("You forgot a title", 'error')
            return render_template("new_post.html")

        if new_body == "":
            flash ("You forgot to write something", 'error')
            return render_template("new_post.html")

        else:
            new_entry = Blog(new_name, new_body)
            db.session.add(new_entry)
            db.session.commit()
            return render_template("one_post.html", new_post=new_entry)

    else:
        return render_template("new_post.html")

if __name__ == '__main__':
    app.run()

