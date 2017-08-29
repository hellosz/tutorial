import scrapy

from tutoiral.items import TutoiralItem

class TutorialSpider(scrapy.Spider):
    #爬虫名称
    name = "tutorial"

    #允许的域名
    allowed_domains = ['dmoztools.net']

    #起始url -> scrapy.request
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/"
    ]

    #结果解析 -> scrapy.http.Response
    def parse(self, response):

        #2.展示标签里的内容
        for sel in response.xpath('//ul/li'):
            item = TutoiralItem()
            item['title']= sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item