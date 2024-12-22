import scrapy

def articleScrape(response):
    article = response.css('article *::text').getall()  
    article = [text.strip() for text in article if text.strip()]  

    if not article:
        article = ["No articles found"]
        
    return article
