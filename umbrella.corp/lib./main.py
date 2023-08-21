from Author import Author
from Magazine import Magazine
from Article import Article

author1 = Author("John Doe")
author2 = Author("Jane Smith")

magazine1 = Magazine("Tech Today", "Technology")
magazine2 = Magazine("Fashion Weekly", "Fashion")

author1.add_article(magazine1, "Python Programming")
author1.add_article(magazine2, "Fashion Trends")
author2.add_article(magazine2, "Eco-Friendly Fashion")

print("Author 1 Articles:", [article.title() for article in author1.articles()])
print("Author 1 Magazines:", [magazine.name() for magazine in author1.magazines()])
print("Author 1 Topic Areas:", author1.topic_areas())

print("Magazine 2 Contributors:", [contributor.name() for contributor in magazine2.contributors()])
print("Magazine 2 Article Titles:", magazine2.article_titles())
print("Magazine 2 Contributing Authors:", [contributor.name() for contributor in magazine2.contributing_authors()])
