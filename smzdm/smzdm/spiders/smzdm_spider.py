import scrapy
from smzdm.items import SmzdmItem
class SmzdmSpider(scrapy.Spider):
    name = "smzdm"
    allowed_domains = ["smzdm.com"]
    start_urls = {"http://www.smzdm.com"}

    def parse(self,response):
#        filename = "ps4.txt"
#        with open(filename,"ab") as f:
        for sel in response.xpath('//ul/li'):
            item = SmzdmItem()
            item['link'] = sel.xpath('a/@href').extract()
            
            #f.write(link)
            yield item
                
