import scrapy

class TutorialSpider(scrapy.Spider):
    #爬虫名称
    name = "tutorial"

    #允许的域名
    allowed_domains = ['dmoz.org']

    #起始url -> scrapy.request
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    #结果解析 -> scrapy.http.Response
    def parse(self, response):
        filename = response.url.split("/")[-2];
        print(filename)
        with open(filename, 'wb') as f:
            f.wirte(response.body)
