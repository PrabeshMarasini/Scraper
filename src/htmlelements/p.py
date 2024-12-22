import scrapy

def pScrape(response):
    p = response.css('p::text').getall()

    if not p:
        p = ["No p found"]

    return p