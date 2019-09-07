title: Should it be YYYY-MM-DD or YYYY-DD-MM? My Thoughts
date: 2013-09-01
description: This is a simple python Flask Application that utilizes flask-flatpages to render markdown

Lorem, ipsum dolor sit amet consectetur adipisicing elit. Omnis quae sed quasi laborum quas vero unde, veniam consequuntur a dolores. Vero quaerat earum impedit ipsum eaque pariatur quae autem vitae. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Omnis quae sed quasi laborum quas vero unde, veniam consequuntur a dolores. Vero quaerat earum impedit ipsum eaque pariatur quae autem vitae. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Omnis quae sed quasi laborum quas vero unde, veniam consequuntur a dolores. Vero quaerat earum impedit ipsum eaque pariatur quae autem vitae. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Omnis quae sed quasi laborum quas vero unde, veniam consequuntur a dolores. Vero quaerat earum impedit ipsum eaque pariatur quae autem vitae. 
Lorem, ipsum dolor sit amet consectetur adipisicing elit. Omnis quae sed quasi laborum quas vero unde, veniam consequuntur a dolores. Vero quaerat earum impedit ipsum eaque pariatur quae autem vitae. 
# Test

```python
import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', debug=True)
```