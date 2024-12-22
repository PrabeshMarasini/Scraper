import scrapy

def liScrape(response):
    li = response.css('li *::text, li::text').getall()
    li = [text.strip() for text in li if text.strip()] 

    if not li:
        li = ["No list items found"]
        
    return li