import scrapy
from scrapy.crawler import CrawlerProcess

class Scraper(scrapy.Spider):
    name = "html_scraper"
    
    def start_requests(self):
        url = input("Enter the website link: ").strip()
        if not url.startswith("https://"):
            url = "https://" + url
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.text)

process = CrawlerProcess()
process.crawl(Scraper)
process.start()
