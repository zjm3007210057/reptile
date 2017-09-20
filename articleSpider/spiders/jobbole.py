# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112218/']

    def parse(self, response):
        re_selector = response.xpath('/html/body/div[1]/div[3]/div[1]/div[1]/h1')
        print(re_selector.xpath("//*"))
        re_selector1 = response.xpath('//*[@id="post-112218"]/div[1]/h1')
        re_selector2 = response.xpath('///div[@class="entry-header"]/h1/text()')
        pass
