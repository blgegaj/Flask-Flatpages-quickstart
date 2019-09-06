from flask import render_template
from main import app, flatpages
from flask_flatpages import pygments_style_defs
from config import Config
import random

# @app.route('/pygments.css')
# def pygments_css():
#     return pygments_style_defs("monokai"), 200, {"Content-Type":"text/css"}

@app.route("/")
def index():
    posts = []
    for index, post in enumerate(flatpages):
        print(post.path)
        metadata = post._meta.title().split("\n")
        title = metadata[0].split(":")[1]
        date = metadata[1].split(":")[1]
        posts.append([title, date,  post.body[:random.randint(120, 170)] + "....", post.path])
        if index == 3:
            break
    return render_template("index.html", posts=posts)

@app.route("/posts/")
def posts():
    posts = []
    for post in flatpages:
        if post.path.startswith(Config.POSTS_DIR):
            metadata = post._meta.title().split("\n")
            title = metadata[0].split(":")[1]
            date = metadata[1].split(":")[1]
            posts.append([title, date,  post.body[:random.randint(120, 170)] + "....", post.path])
    return render_template('posts.html', posts=posts)

@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(Config.POSTS_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)
