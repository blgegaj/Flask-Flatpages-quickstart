class Config(object):
    FLATPAGES_AUTO_RELOAD = True
    FLATPAGES_EXTENSION = ".md"
    FLATPAGES_ROOT = "content"
    POSTS_DIR = "posts"
    FREEZER_RELATIVE_URLS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True