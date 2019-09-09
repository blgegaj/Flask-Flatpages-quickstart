from flask import Flask
from flask_flatpages import FlatPages

# Entry point of the application definition of the main app (Flask) module
app = Flask(__name__)
flatpages = FlatPages(app)

# import everything from the routes file
from routes import *


HOST = "localhost"
PORT = 5000
# Definition of the configuration to be used
# Production debug_mode = off
# app.config.from_object("config.ProductionConfig")

# Development debug_mode = on
app.config.from_object("config.DevelopmentConfig")

# Only when i run this file the following code is to be executed
if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
