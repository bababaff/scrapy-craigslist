# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['losangeles.craigslist.org']
    start_urls = ['https://losangeles.craigslist.org/search/egr']

    def parse(self, response):
        listings = response.xpath('//li[@class="result-row"]')

        for listing in listings:
            date = listing.xpath('.//time/@datetime').get()
            title = listing.xpath(
                './/a[@class="result-title hdrlnk"]/text()').get()
            link = listing.xpath(
                './/a[@class="result-title hdrlnk"]/@href').get()

            yield {
                'date': date,
                'title': title,
                'link': link
            }
