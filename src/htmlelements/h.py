import scrapy

def headingsScrape(response):
    headings = {}
    for i in range(1, 7):
        heading_tag = f'h{i}'
        heading = response.css(f'{heading_tag}::text').getall()

        if not heading:
            heading = ["No headings found"]
        headings[heading_tag] = heading
    return headings
