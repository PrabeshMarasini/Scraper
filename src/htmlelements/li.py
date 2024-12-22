import scrapy

def liScrape(response):
    li = response.css('li::text').getall()

    if not li:
        li = ["No li items found"]

    return li