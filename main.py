from flask import Flask, render_template_string
import pygments, markdown
from flask_flatpages import FlatPages, pygments_style_defs

app = Flask(__name__)
def my_markdown(text):
    markdown_text = render_template_string(text)
    pygmented_text = markdown.markdown(markdown_text, extensions=["codehilite", "fenced_code", "tables"])
    return pygmented_text

app.config["FLATPAGES_HTML_RENDERER"] = my_markdown
flatpages = FlatPages(app)

from routes import *

HOST = "localhost"
PORT = 5000
# Production debug_mode = off
# app.config.from_object("config.ProductionConfig")

# Development debug_mode = on
app.config.from_object("config.DevelopmentConfig")
if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
