import scrapy

def ulScrape(response):
    ul = response.css('ul li *::text, ul li::text').getall()
    ul = [text.strip() for text in ul if text.strip()]  

    if not ul:
        ul = ["No ul found"]
        
    return ul
