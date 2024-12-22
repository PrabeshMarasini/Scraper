import scrapy

def ulScrape(response):
    ul = response.css('ul').getall()

    if not ul:
        ul = ["No ul found"]
    
    return ul