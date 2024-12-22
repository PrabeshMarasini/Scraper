import scrapy

def sectionScrape(response):
    section = response.css('section::text').getall()

    if not section:
        section = ["No sections found"]

    return section