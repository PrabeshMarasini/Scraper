import scrapy

def aScrape(response):
    a = response.css('a::attr(href)').getall()  
    a = [link.strip() for link in a if link.strip()]  

    if not a:
        a = ["No anchors found"]
        
    return a
