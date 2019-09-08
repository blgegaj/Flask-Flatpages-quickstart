
from flask import render_template_string
import pygments, markdown

def my_markdown(text):
    markdown_text = render_template_string(text)
    pygmented_text = markdown.markdown(markdown_text, extensions=["codehilite", "fenced_code", "tables"])
    return pygmented_text

class Config(object):
    FLATPAGES_AUTO_RELOAD = True
    FLATPAGES_EXTENSION = ".md"
    FLATPAGES_ROOT = "content"
    POSTS_DIR = "posts"
    FREEZER_RELATIVE_URLS = False
    FLATPAGES_HTML_RENDERER = my_markdown

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True