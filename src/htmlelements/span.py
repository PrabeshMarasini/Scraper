import scrapy

def spanScrape(response):
    span = response.css('span::text').getall() 
    span = [text.strip() for text in span if text.strip()]  

    if not span:
        span = ["No spans found"]
        
    return span
