import scrapy

def olScrape(response):
    ol = response.css('ol').getall()
    
    if not ol:
        ol = ["No ol found"]

    return ol