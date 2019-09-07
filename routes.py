from flask import render_template
from main import app, flatpages
from flask_flatpages import pygments_style_defs
from config import Config
import math
import random

# @app.route('/pygments.css')
# def pygments_css():
#     return pygments_style_defs("monokai"), 200, {"Content-Type":"text/css"}

POST_PAGES = 4

@app.route("/")
def index():

    posts = [post for post in flatpages if post.path.startswith(Config.POSTS_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=True)
    tmp = []
    for post in posts[:3]:
        metadata = post._meta.title().split("\n")
        title = metadata[0].split(":")[1]
        date = metadata[1].split(":")[1]
        description = metadata[2].split(":")[1]
        tmp.append([title, date,  description, post.path])
    return render_template("index.html", posts=tmp)


def get_post_details(post):
    metadata = post._meta.title().split("\n")
    title = metadata[0].split(":")[1]
    date = metadata[1].split(":")[1]
    description = metadata[2].split(":")[1]
    body = post.body[:random.randint(120, 170)] + "...."
    return [title, date, description, post.path, body]
    

@app.route("/posts/<int:page>")
def posts(page):

    posts = [post for post in flatpages if post.path.startswith(Config.POSTS_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=True)
    num_posts = len(posts)
    pages = math.ceil(num_posts / POST_PAGES)
    previous_page = False
    next_page = False

    tmp = []    

    if page>pages or page <= 0:
        posts = posts[:POST_PAGES]
        for post in posts:
            tmp.append(get_post_details(post))
        posts = tmp
        return render_template('posts.html', posts=posts, previous_page=previous_page, next_page=next_page, page=1)

    if page > 0:
        previous_page = page-1
    if page < pages:
        next_page = page+1   

    print(previous_page)
    print(next_page) 

    start = (page-1)*POST_PAGES
    end = (page-1)*POST_PAGES + POST_PAGES    
    posts = posts[start:end]

    for post in posts:
        tmp.append(get_post_details(post))
    posts = tmp
    
    return render_template('posts.html', posts=posts, previous_page=previous_page, next_page=next_page, page=page)

@app.route('/post/<name>/')
def post(name):
    path = '{}/{}'.format(Config.POSTS_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)
