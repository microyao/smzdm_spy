import scrapy

class SmzdmSpider(scrapy.Spider):
    name = "smzdm"
    allowed_domains = ["smzdm.com"]
    start_urls = {"http://www.smzdm.com"}
