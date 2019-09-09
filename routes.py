from flask import render_template, redirect, url_for
from main import app, flatpages
from flask_flatpages import pygments_style_defs
from config import Config
import math
import random

# How many posts to be displayed on each page
POST_PAGES = 4

# On 404 just redirect to the index page
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("index"))

# This is the index route of the application
@app.route("/")
def index():
    # Get all posts from the content/posts folder and sort them by date
    posts = [post for post in flatpages if post.path.startswith(Config.POSTS_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=True)
    tmp = []
    # for each post in the posts array until the 3rd one get some data like title, data, description, etc
    for post in posts[:3]:
        metadata = post._meta.title().split("\n")
        title = metadata[0].split(":")[1]
        date = metadata[1].split(":")[1]
        description = metadata[2].split(":")[1]
        tmp.append([title, date,  description, post.path])
    # and then pass these data to the index.html template (these data can be referred from the index.html from the posts variables)
    return render_template("index.html", posts=tmp)


# This is a simple function that is called inside the /posts/page route function
def get_post_details(post):
    metadata = post._meta.title().split("\n")
    title = metadata[0].split(":")[1]
    date = metadata[1].split(":")[1]
    description = metadata[2].split(":")[1]
    body = post.body[:random.randint(120, 170)] + "...."
    return [title, date, description, post.path, body]
    

# /posts/1/, posts/2/, etc route
# the number is for the pagination of the posts
@app.route("/posts/<int:page>/")
def posts(page):

    # Get all posts from the content/posts fodler and sort them by date
    posts = [post for post in flatpages if post.path.startswith(Config.POSTS_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=True)

    # the following is the logic for the pagination(which posts need to be returned)
    # get the total number of the posts
    num_posts = len(posts)
    # calculate how many pages there are in total
    pages = math.ceil(num_posts / POST_PAGES)
    previous_page = False
    next_page = False

    tmp = []    

    # if the page requested is not valid
    # then get return the posts from the first page
    if page>pages or page <= 0:
        posts = posts[:POST_PAGES]
        for post in posts:
            tmp.append(get_post_details(post))
        posts = tmp
        page = 1
        if page < pages:
            next_page = page+1
        return render_template('posts.html', posts=posts, previous_page=previous_page, next_page=next_page, page=page)

    # calculate if the next and previous buttons need to be enabled in the front-end
    if page > 0:
        previous_page = page-1
    if page < pages:
        next_page = page+1 

    # calculate the section of the posts depending on the page requested
    start = (page-1)*POST_PAGES
    end = start + POST_PAGES    
    posts = posts[start:end]

    for post in posts:
        tmp.append(get_post_details(post))
    posts = tmp
    
    return render_template('posts.html', posts=posts, previous_page=previous_page, next_page=next_page, page=page)

# in this route just get the content from the markdown file and render it to the user through the post.html template
@app.route('/post/<name>/')
def post(name):
    path = '{}/{}'.format(Config.POSTS_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)
