import scrapy

def headingsScrape(response):
    headings = {}
    for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        texts = response.css(f'{tag}::text').getall()  
        texts = [text.strip() for text in texts if text.strip()]  
        headings[tag] = texts if texts else [f"No {tag.upper()} headings found"]  
        
    return headings
