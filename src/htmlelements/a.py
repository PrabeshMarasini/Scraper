import scrapy

def aScrape(response):
    a = response.css('a::attr(href)').getall()
    
    if not a:
        a = ["No links found"]

    return a