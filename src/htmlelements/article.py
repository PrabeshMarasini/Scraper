import scrapy

def articleScrape(response):
    article = response.css('article::text').getall()

    if not article:
        article = ["No articles found"]

    return article