import scrapy

def divScrape(response):
    div = response.css('div *::text').getall()  
    div = [text.strip() for text in div if text.strip()]

    if not div:
        div = ["No div elements found"]

    return div
