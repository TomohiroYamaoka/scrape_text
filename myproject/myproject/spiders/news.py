import scrapy
from myproject.items import Headline

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['http://news.yahoo.co.jp/']

    def parse(self, response):
        for url in response.css('ul.topicsList_main a::attr("href")').re(r'/pickup/\d+$'):
            yield response.follow(url,self.parse_topics)
    
    def parse_topics(self,response):
       item=Headline()
       item['title']=response.css('.tpcNews_title::text').get()
       item['body']=response.css('.tpcNews_summary').xpath('string()').get()
       yield item
