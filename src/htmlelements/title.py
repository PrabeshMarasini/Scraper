import scrapy

def titleScrape(response):
    title = response.css('title::text').get()

    if not title:
        title = "No title found"

    return title