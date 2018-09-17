# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WawjspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # 地址、楼层、朝向、装修、楼型、供暖、出租方式、看房时间、商圈、地铁、租金、户型、面积、支付方式
    shangquan = scrapy.Field()
    zhifufangshi = scrapy.Field()
    mianji = scrapy.Field()
    address = scrapy.Field()
    gongnuan = scrapy.Field()
    chaoxiang = scrapy.Field()
    louceng = scrapy.Field()
    zhuangxiu = scrapy.Field()
    louxing = scrapy.Field()
    chuzufangshi = scrapy.Field()
    kanfangshijian = scrapy.Field()
    ditie = scrapy.Field()
    zujin = scrapy.Field()
    huxing = scrapy.Field()
    href = scrapy.Field()