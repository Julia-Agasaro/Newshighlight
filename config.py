import os

class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?{}?api_key={}'
    NEWS_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    pass

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}