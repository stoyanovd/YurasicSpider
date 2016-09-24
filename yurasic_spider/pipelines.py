# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

#authors_file = '/home/dima/PycharmProjects/yurasic_spider/authors.txt'
authors_file = 'C:\\Users\\stoya\\work\\spider\\authors.txt'


class YurasicSpiderPipeline(object):
    def __init__(self):
        self.cur_authors = set()

    def process_item(self, item, spider):
        a = item['author']
        if a not in self.cur_authors:
            self.cur_authors.add(a)
            with open(authors_file, 'a') as f:
                f.write(a + os.linesep)
        return item
