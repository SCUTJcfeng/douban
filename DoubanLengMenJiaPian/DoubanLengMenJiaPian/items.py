# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanlengmenjiapianItem(scrapy.Item):
    title = scrapy.Field()
    rate = scrapy.Field()
    directors = scrapy.Field()
    casts = scrapy.Field()
    id = scrapy.Field()
    url = scrapy.Field()
    cover = scrapy.Field()
    pass

class Doubanjingdian(scrapy.Item):
    title = scrapy.Field()
    rate = scrapy.Field()
    directors = scrapy.Field()
    casts = scrapy.Field()
    id = scrapy.Field()
    url = scrapy.Field()
    cover = scrapy.Field()
    pass
    '''
    "directors": [
        "王童"
    ],
    "rate": "8.9",
    "cover_x": 400,
    "star": "45",
    "title": "红柿子",
    "url": "https://movie.douban.com/subject/1303637/",
    "casts": [
        "陶述",
        "石隽",
        "张世",
        "鲁直",
        "刘若英"
    ],
    "cover": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2304629928.webp",
    "id": "1303637",
    "cover_y": 538
    '''
    pass
