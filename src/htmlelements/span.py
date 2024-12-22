import scrapy

def spanScrape(response):
    span = response.css('span::text').getall()

    if not span:
        span = ["No spans found"]
    
    return span