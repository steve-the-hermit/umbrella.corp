from Author import Author
from Article import Article
from Magazine import Magazine

author1 = Author("John Doe")
author2 = Author("Jane Smith")

magazine1 = Magazine("Tech Today", "Technology")
magazine2 = Magazine("Fashion Weekly", "Fashion")

author1.add_article(magazine1, "Python Programming")
author1.add_article(magazine2, "Fashion Trends")
author2.add_article(magazine2, "Eco-Friendly Fashion")

print(author1.articles())
print(author1.magazines())
print(author1.topic_areas())

print(magazine2.contributors())
print(magazine2.article_titles())
print(magazine2.contributing_authors())
