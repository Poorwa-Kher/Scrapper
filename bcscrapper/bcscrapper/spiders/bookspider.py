import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["forkdrop.io"]
    start_urls = ["http://forkdrop.io/"]

    def parse(self, response):
        pass
