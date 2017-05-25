# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Cl1024Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cl_title = scrapy.Field()
    cl_url = scrapy.Field()
    cl_bankuai = scrapy.Field()
    posted = scrapy.Field()
    torrent_url = scrapy.Field()
    torrent_downloaded = scrapy.Field()
    torrent_download_urls = scrapy.Field()

