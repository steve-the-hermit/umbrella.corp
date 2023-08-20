class Magazine:
    _all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        self._all.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    @classmethod
    def all(cls):
        return cls._all

    def contributors(self):
        return list(set([article.author() for article in self._articles]))

    def add_article(self, author, title):
        article = article(author, self, title)
        self._articles.append(article)

    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls._all if magazine.name() == name), None)

    @classmethod
    def article_titles(cls):
        return [article.title() for magazine in cls._all for article in magazine._articles]

    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            author = article.author()
            authors_count[author] = authors_count.get(author, 0) + 1
        return [author for author, count in authors_count.items() if count > 2]
