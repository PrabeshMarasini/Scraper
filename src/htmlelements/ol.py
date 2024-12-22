import scrapy

def olScrape(response):
    ol = response.css('ol li *::text, ol li::text').getall()
    ol = [text.strip() for text in ol if text.strip()]

    if not ol:
        ol = ["No ol found"]
        
    return ol
