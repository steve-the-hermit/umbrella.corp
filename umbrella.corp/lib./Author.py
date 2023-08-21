class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set([article.magazine() for article in self._articles]))

    def add_article(self, magazine, title):
        new_article = (self, magazine, title)
        self._articles.append(new_article)
        
    def topic_areas(self):
        return list(set([magazine.category() for magazine in self.magazines()]))

    def __str__(self):
        return self._name
