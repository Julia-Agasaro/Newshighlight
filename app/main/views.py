from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source, get_articles

from ..models import Source
# Views
@main.route('/')
def index():
    '''
    View movie page function that returns the movie details page and its data
    '''
    title = "Home || News"

    sport_news = get_source('sports')
    general_news = get_source('general')
    tech_news = get_source('technology')
    bus_news = get_source('business')
    sci_news = get_source('science')
    ent_news = get_source('entertainment')
    return render_template('index.html',  title= title, sports = sport_news, general = general_news, technology = tech_news, business = bus_news, science = sci_news, entertainment= ent_news)

@main.route('/news/<id>')
def source(id):
    '''
    function that returns articles by source id
    '''

    article_source = get_articles(id)
    title = f'{id}| Articles'
    return render_template('articles.html',title = title, articles = article_source)

