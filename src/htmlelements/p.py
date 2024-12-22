import scrapy

def pScrape(response):
    p = response.css('p::text').getall()  
    p = [text.strip() for text in p if text.strip()]  

    if not p:
        p = ["No p found"]
        
    return p
