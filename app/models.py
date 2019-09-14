class Source:
    '''
    articles class to define article Objects
    '''

    def __init__(self,id,name,description,url,country,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.country = country
        self.category = category
        
class Articles:
    '''
    articles class to define article objects
    '''
    def __init__(self,id,title, description, image, date, author, url,content):
        self.id = id
        self.title = title
        self.description = description
        self.image = image
        self.date = date
        self.author = author
        self.url = url