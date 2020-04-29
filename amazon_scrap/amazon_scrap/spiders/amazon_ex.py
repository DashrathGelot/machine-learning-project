# -*- coding: utf-8 -*-
import scrapy
from .. items import AmazonScrapItem

class AmazonExSpider(scrapy.Spider):
    name = 'amazon_ex'
    start_urls = ['https://www.amazon.com/s?rh=n%3A283155%2Cn%3A%212334088011%2Cn%3A%212334119011%2Cn%3A6960520011&page=2&qid=1570953277&ref=lp_6960520011_pg_2']
    page_num=3

    def parse(self, response):
        item=AmazonScrapItem()
        book_name=response.css('.a-color-base.a-text-normal::text').extract()
        book_price=response.css('.a-spacing-top-small .a-price:nth-child(1) span').css('::text').extract()
        book_author=response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        book_img=response.css('.s-image::attr(src)').extract()
        item['book_name']=book_name
        item['book_price']=book_price
        item['book_author']=book_author
        item['book_img']=book_img
        yield item
        next_page='https://www.amazon.com/s?rh=n%3A283155%2Cn%3A%212334088011%2Cn%3A%212334119011%2Cn%3A6960520011&page='+str(AmazonExSpider.page_num)+'&qid=1570953277&ref=lp_6960520011_pg_2'
        if AmazonExSpider.page_num<=24:
            AmazonExSpider.page_num+=1
            yield response.follow(next_page,callback=self.parse)
        
