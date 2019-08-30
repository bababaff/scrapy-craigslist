# -*- coding: utf-8 -*-
import scrapy


def get_userbody(response, value):
    return response.xpath('//span[text()="compensation: "]/b/text()').get()


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

            yield scrapy.Request(link, callback=self.parse_listing, meta={
                'date': date,
                'title': title,
                'link': link
            })

        next_page_url = response.xpath(
            '//*[@class="button next"]/@href').get()  # /search/egr?s=120

        # https://losangeles.craigslist.org/search/egr?s=120
        abs_next_page_url = response.urljoin(next_page_url)

        if next_page_url:
            yield scrapy.Request(abs_next_page_url, callback=self.parse)

    def parse_listing(self, response):
        date = response.meta['date']
        title = response.meta['title']
        link = response.meta['link']
        compensation = response.xpath(
            '//*[@class="attrgroup"]/span[1]/b/text()').get()
        employment_type = response.xpath(
            '//*[@class="attrgroup"]/span[2]/b/text()').get()
        images = response.xpath("//*[@id='thumbs']//@src").getall()

        images = [image.replace('50x50c', '600x450') for image in images]
        description = "".join(response.xpath(
            '//*[@id="postingbody"]/text()').getall()).strip()

        yield {
            'date': date,
            'title': title,
            'link': link,
            'compensation': compensation,
            'employment_type': employment_type,
            'images': images,
            'description': description
        }
