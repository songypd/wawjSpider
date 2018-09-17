# -*- coding: utf-8 -*-
from random import random, Random

import scrapy
import time

from wawjSpider.wawjSpider.items import WawjspiderItem


class WawjspiderSpider(scrapy.Spider):
    name = "wawjspider"
    allowed_domains = ["bj.5i5j.com"]
    start_urls = ['https://bj.5i5j.com/zufang/']
    # xpath_prefix = "//div[@class='content fr']//div[@class='housesty']"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Cookie: PHPSESSID=15phvcdfim5ff787odfmi76g4l; domain=bj; _ga=GA1.2.1018343336.1536907326; _gid=GA1.2.234806853.1536907326; _gat=1; yfx_c_g_u_id_10000001=_ck18091414420611648380775748216; yfx_f_l_v_t_10000001=f_t_1536907326157__r_t_1536907326157__v_t_1536907326157__r_c_0; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1536907326; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1536907326; _Jo0OQK=23623A1325A6741334B0425AA51BB518FC586F8DA04376F974619F98608BCEE15674F69915D1D62C4FF8CBC654ED7794D0FA0F44E6F335892C516CC81121CCAB7FEC57212F12283777C98FB9E3C853EFEE298FB9E3C853EFEE215D8BEE34E43E5C0GJ1Z1VQ==
        'Host': 'bj.5i5j.com',
        'Referer': 'https://bj.5i5j.com/zufang/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    cookies = {
        'PHPSESSID': 'bpdslvl834e97rof43uhihrc99',
        'domain': 'bj',
        '_ga': 'GA1.2.1204791589.1536903105',
        '_gid': 'GA1.2.1204791589.1536903105',
        '_gat': '1',
        'yfx_c_g_u_id_10000001': '_ck18091413313910310716032146123',
        'yfx_f_l_v_t_10000001': 'f_t_1536903098968__r_t_1536903098968__v_t_1536918259614__r_c_0',
        'Hm_lvt_94ed3d23572054a86ed341d64b267ec6': '1536918274',
        'Hm_lpvt_94ed3d23572054a86ed341d64b267ec6': '1536918274',
        '_Jo0OQK': '77301EA7744A21CDC57ACBF9F9CF07F01909080134216BE972D7E4D63053210E2E12C2B73838F381E7F5932F1818604149CD335489EBCF16C59C1B99FFDAB7AC593C57212F12283777C840763663251ADEB840763663251ADEB90E4E57C5FB61AC6A593CD374DB85252GJ1Z1Jw==',
        # 'zufang_BROWSES': '41471181%2C41470029%2C41466716%2C41465151%2C41473911%2C41452876%2C41216704%2C41476214'
    }

    # xpath_prefix = "//div[@class='content fr']//div[@class='housesty']"

    def parse(self, response):
        return [scrapy.Request(url='https://bj.5i5j.com/zufang/', cookies=self.cookies,
                               callback=self.start_qe)]
        # self.start_qe(self,response)
    def start_qe(self, response):
        # time.sleep(3)
        detail_hrefs = response.xpath(
            "//div[@class='list-con-box']//div[@class='listCon']//h3[@class='listTit']//@href").extract()
        for i_item in detail_hrefs:
            # print(i_item)
            yield scrapy.Request(url="https://bj.5i5j.com" + i_item, callback=self.nextpar)
        next_page = response.xpath("/html/body/div[4]/div[1]/div[3]/div[2]/a[1]//@href").extract()
        count =0
        if next_page:
            next_page = next_page[0]
            print(str(next_page) + "--------------------------")
            time.sleep(2)
            if count % 9 ==0:
                time.sleep(5)
            count +=1
            yield scrapy.Request(url="https://bj.5i5j.com" + next_page, callback=self.start_qe)

    def nextpar(self, res):
        item = WawjspiderItem()
        try:
            item["louceng"] = res.xpath("/html/body/div[3]/div[2]/div[2]/div[2]/ul/li[2]/text()").extract()[0]
        except:
            item["louceng"] =00
        try:
            item["chaoxiang"] = res.xpath("/html/body/div[3]/div[2]/div[2]/div[2]/ul/li[3]/text()").extract()[0]
        except:
            item["chaoxiang"] = 00
        try:
            item["zhuangxiu"] = res.xpath("/html/body/div[3]/div[2]/div[2]/div[2]/ul/li[4]/text()").extract()[0]
        except:
            item["zhuangxiu"] =00
        try:
            item["louxing"] = res.xpath("/html/body/div[3]/div[2]/div[2]/div[2]/ul/li[5]/text()").extract()[0]
        except:
            item["louxing"] =00
        try:
            item["gongnuan"] = res.xpath("/html/body/div[3]/div[2]/div[2]/div[2]/ul/li[6]/text()").extract()[0]
        except:
            item["gongnuan"] =00
        try:
            item["chuzufangshi"] = res.xpath("/html/body/div[3]/div[2]/div[2]/div[2]/ul/li[7]/text()").extract()[0]
        except:
            item["chuzufangshi"] =00
        try:
            item["kanfangshijian"] = res.xpath("/html/body/div[3]/div[2]/div[2]/div[2]/ul/li[8]/text()").extract()[0]
        except:
            item["kanfangshijian"] = 00
        try:
            item["shangquan"] = res.xpath("/html/body/div[3]/div[2]/div[2]/div[2]/ul/li[9]/text()").extract()[0]
        except:
            item["shangquan"] =00
        try:
            item["ditie"] = res.xpath("/html/body/div[3]/div[2]/div[2]/div[2]/ul/li[10]/text()").extract()[0]
        except:
            item["ditie"] = 00
        try:
            item["address"] = res.xpath("/html/body/div[3]/div[2]/div[2]/div[2]/ul/li[1]/a/text()").extract()[0]
        except:
            item["address"] = 00
        try:
            item["zujin"] = res.xpath("/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div/p[1]/text()").extract()[0]
        except:
            item["zujin"] = 00
            return
        try:
            item["huxing"] = res.xpath("/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div/p[1]/text()").extract()[0]
        except:
            item["huxing"] = 00
        try:
            item["mianji"] = res.xpath("/html/body/div[3]/div[2]/div[2]/div[1]/div[3]/div/p[1]/text()").extract()[0]
        except:
            item["mianji"] = 00
        try:
            item["zhifufangshi"] = res.xpath("/html/body/div[3]/div[2]/div[2]/div[1]/div[4]/div/p[1]/text()").extract()[0]
        except:
            item["zhifufangshi"] = 00

        item["href"] = res.url
        print(item["zujin"] + item["huxing"] + item["mianji"] + item["zhifufangshi"] + item["address"])
        yield item
