import urllib.request,json
from .models import Source,Articles

# Getting api key
apiKey = None
# Getting the movie base url
base_url = None
articles_url= None

def configure_request(app):
    global apiKey, base_url,articles_url
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_URL']
    articles_url = app.config['ARTICLES_BASE_URL']
    print('hey')
    print(articles_url)
    print(apiKey)
#     articles_url=app.config['NEWS_API_URL']

def get_source(category):
    '''function that gets the json response to the url request
    '''
    print('Hello')
    print(base_url)
    print(apiKey)
    get_source_url = base_url.format(category, apiKey)
    print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)



    return source_results
def process_results(source_list):
    '''
    '''

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        country = source_item.get('country')
        category = source_item.get('category')
        source_object = Source(id,name,description,url,country,category)
        source_results.append(source_object)

    return source_results

def get_articles(id):
 '''
 Function that processes the articles and returns a list of articles objects
 '''
 print(id)
 print(apiKey)
 print(articles_url)
 get_articles_url = articles_url.format(id,apiKey)
 print(get_articles_url)
 with urllib.request.urlopen(get_articles_url) as url:
   articles_results = json.loads(url.read())
   articles_object = None
   if articles_results['articles']:
     articles_object = process_articles(articles_results['articles'])
 return articles_object
def process_articles(articles_list):
 '''
 '''
 articles_object = []
 for article_item in articles_list:
   id = article_item.get('id')
   author = article_item.get('author')
   title = article_item.get('title')
   content = article_item.get('content')
   description = article_item.get('description')
   url = article_item.get('url')
   image = article_item.get('urlToImage')
   date = article_item.get('publishedAt')
   if image:
     articles_result = Articles(id,title, description, image, date, author, url,content)
     articles_object.append(articles_result)
 return articles_object