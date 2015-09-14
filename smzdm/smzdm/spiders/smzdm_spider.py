import scrapy

class SmzdmSpider(scrapy.Spider):
    name = "smzdm"
    allowed_domains = ["smzdm.com"]
    start_urls = {"http://www.smzdm.com"}

    def parse(self,response):
        filename = "ps4.txt"
        with open(filename,"wb") as f:
            f.write(response.body)
