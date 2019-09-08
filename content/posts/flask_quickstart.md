title: Getting started with Python-Flask web framework
date: 2013-09-08
description: This is a flask quickstart tutorial

# Quickstart

Eager to get started? This page gives a good introduction to Flask. It assumes you already have Flask installed. If you do not, head over to the Installation section.

### A Minimal Application

A minimal Flask application looks something like this

```python 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```