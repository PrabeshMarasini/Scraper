import scrapy

def sectionScrape(response):
    section = response.css('section *::text').getall()  
    section = [text.strip() for text in section if text.strip()]

    if not section:
        section = ["No sections found"]
        
    return section
