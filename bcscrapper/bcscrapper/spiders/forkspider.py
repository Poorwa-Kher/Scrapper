import scrapy

class ForkSpider(scrapy.Spider):
    name = "forks"
    def start_requests(self):
        url = "http://forkdrop.io/"
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        item = {}
        table = response.css("table-header")
        
        # bitcoins = response.css("div.ag-body-container")
        # item["name"] = bitcoins.css("a::text").extract_first()
        # item['date'] = response.xpath(
        #     "//*[@id='table-bitcoin']/following-sibling::span[1]/text()"
        # ).extract_first()
        # """ item['description'] = response.xpath(
        #     "//div[@id='product_description']/following-sibling::p/text()"
        # ).extract_first()
        # item['price'] = response.css('p.price_color ::text').extract_first() """
        # yield item