# -*- coding: utf-8 -*-
import scrapy
# from PSR import data

class AvitoSpider(scrapy.Spider):
    name = 'avito_spider'
    # allowed_domains = ['avito.ru']
    # start_urls = ['http://avito.ru/ekaterinburg']
    allowed_domains = ['yandex.ru']
    start_urls = ['http://yandex.ru/']

    # def parse(self, response):
    #     urls = response.css('div.quote > span > a::attr(href)').extract()
    #     for url in urls:
    #         url = response.urljoin(url)
    #         yield scrapy.Request(url=url, callback=self.parse_details)
    #
    #     next_page_url = response.css('li.next > a::attr(href)').extract_first()
    #     i = 0
    #     if next_page_url or (i <= 10):
    #         next_page_url = response.urljoin(next_page_url)
    #         i += 1
    #         yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = {
                # 'author': response.css('small.author::text').extract_first(),
                # 'text': response.css('span.text::text').extract_first(),
                # 'tags': response.css('a.tag::text').extract(),
                'item' : response.css('html::text').extract_first()
            }
            yield item
        # Follow pagination link
        # next_page_url = response.css('li.next > a::attr(href)').extract_first()
        # if next_page_url:
        #     next_page_url = response.urljoin(next_page_url)
        #     yield scrapy.Request(url=next_page_url, callback=self.parse)

    # def parse_details(self, response):
    #     #     yield {
    #     #         'name': response.css('h3.author-title::text').extract_first(),
    #     #         'birth_date': response.css('span.author-born-date::text').extract_first(),
    #     #     }
