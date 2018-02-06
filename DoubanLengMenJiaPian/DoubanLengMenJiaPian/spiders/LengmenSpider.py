import scrapy
import json
from urllib import parse
from DoubanLengMenJiaPian.items import DoubanlengmenjiapianItem
from DoubanLengMenJiaPian.items import Doubanjingdian

class LengMenSpider(scrapy.Spider):
    name = 'LengMen'
    tags = parse.urlencode({'tags':'冷门佳片'})
    page = 400
    start_urls=["https://movie.douban.com/j/new_search_subjects?sort=S&range=0,10&%s&start=0" % tags]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        jbody = json.loads(response.body)
        item = Doubanjingdian()
        movieList = jbody['data']
        for movie in movieList:
            item['directors'] = movie['directors']
            item['rate'] = movie['rate']
            item['title'] = movie['title']
            item['url'] = movie['url']
            item['casts'] = movie['casts']
            item['cover'] = movie['cover']
            item['id'] = movie['id']
            yield item

        self.page += 400
        next_url = "https://movie.douban.com/j/new_search_subjects?sort=S&range=0,10&%s&start=%d" % (self.tags,self.page)
        yield scrapy.Request(url=next_url)



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