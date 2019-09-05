from flask import render_template
from main import app, flatpages
from config import Config

@app.route("/")
def posts():
    posts = [p for p in flatpages if p.path.startswith(Config.POSTS_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=False)
    return render_template('posts.html', posts=posts)

@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(Config.POSTS_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)
