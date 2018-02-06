# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import scrapy

class DoubanlengmenjiapianPipeline(object):
    db = pymysql.connect(host = '127.0.0.1',user='root',password='root',database='movies',charset='utf8')
    count_error = 0
    def process_item(self, item, spider):
        if spider.name == 'LengMen':
            directors = ','.join(item['directors'])
            rate = item['rate']
            title = item['title']
            url = item['url']
            casts = ','.join(item['casts'])
            cover = item['cover']
            id = item['id']
            data = (title,rate,directors,casts,id,url,cover)
            sql = "insert into doubanlengmenjiapian (title,rate,directors,casts,id,url,cover) values ('%s','%s','%s','%s','%s','%s','%s')" % data
            with self.db.cursor() as cursor:
                cursor.execute(sql)
                self.db.commit()
                print("电影：" +item['title'] + "：已添加进数据库")
        return item

class DoubanJingdianPipeline(object):
    db = pymysql.connect(host = '127.0.0.1',user='root',password='root',database='movies',charset='utf8')
    count_error = 0
    def process_item(self, item, spider):
        if spider.name == 'Jingdian':
            directors = ','.join(item['directors'])
            rate = item['rate']
            title = item['title']
            url = item['url']
            casts = ','.join(item['casts'])
            cover = item['cover']
            id = item['id']
            data = (title,rate,directors,casts,id,url,cover)
            sql = "insert into doubanchengzhang (title,rate,directors,casts,id,url,cover) values ('%s','%s','%s','%s','%s','%s','%s')" % data
            with self.db.cursor() as cursor:
                cursor.execute(sql)
                self.db.commit()
                print("电影：" +item['title'] + "：已添加进数据库")
        return item