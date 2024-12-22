import scrapy
from scrapy.crawler import CrawlerProcess
from htmlelements.title import titleScrape
from htmlelements.h import headingsScrape
from htmlelements.article import articleScrape
from htmlelements.li import liScrape
from htmlelements.ol import olScrape
from htmlelements.p import pScrape
from htmlelements.section import sectionScrape
from htmlelements.span import spanScrape
from htmlelements.ul import ulScrape
from htmlelements.a import aScrape

class Scraper(scrapy.Spider):
    name = "html_scraper"
    
    def start_requests(self):
        url = input("Enter the website link: ").strip()
        if not url.startswith("https://"):
            url = "https://" + url
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = titleScrape(response)
        headings = headingsScrape(response)
        article = articleScrape(response)
        li = liScrape(response)
        ol = olScrape(response)
        paragraph = pScrape(response)
        section = sectionScrape(response)
        span = spanScrape(response)
        ul = ulScrape(response)
        a = aScrape(response)
        
        print(f"Page Title: {title}")
        
        for tag, texts in headings.items():
            print(f"{tag.upper()}:")
            for text in texts:
                print(f"  - {text}")
        
        print("ARTICLES:")
        for article in article:
            print(f"  - {article}")
        
        print("LIST ITEMS:")
        for item in li:
            print(f"  - {item}")
        
        print("ORDERED LISTS:")
        for ol in ol:
            print(f"  - {ol}")
        
        print("PARAGRAPHS:")
        for paragraph in paragraph:
            print(f"  - {paragraph}")
        
        print("SECTIONS:")
        for section in section:
            print(f"  - {section}")
        
        print("SPANS:")
        for span in span:
            print(f"  - {span}")
        
        print("UNORDERED LISTS:")
        for ul in ul:
            print(f"  - {ul}")
        
        print("ANCHORS:")
        for link in a:
            print(f"  - {link}")

process = CrawlerProcess(settings={
    "LOG_ENABLED": False,
})

process.crawl(Scraper)
process.start()
