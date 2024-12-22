import scrapy

def titleScrape(response):
    title = response.css('title::text').get()  
    title = title.strip() if title else "No title found"  
    
    return title
