from flask import Flask
from flask_flatpages import FlatPages

app = Flask(__name__)
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
