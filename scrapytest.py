import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://pcforum.sk/']

    def parse(self, response):
        print("TYYY")