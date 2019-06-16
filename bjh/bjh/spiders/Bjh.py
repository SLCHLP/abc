# -*- coding: utf-8 -*-
import scrapy
from bjh.items import BjhItem
from copy import deepcopy



class BjhSpider(scrapy.Spider):
    name = 'Bjh'
    allowed_domains = ['bxjg.circ.gov.cn']
    start_urls = ['http://bxjg.circ.gov.cn/web/site0/tab5240/module14430/page1.htm']

    def parse(self, response):
        tr_list=response.xpath("//table[@id='ess_ctr14430_ListC_Info_LstC_Info']/tr")
        for tr in tr_list:
            item=BjhItem()
            item["href"]=tr.xpath(".//span[@id='lan1']/a/@href").extract_first()
            item["href"]="http://bxjg.circ.gov.cn"+item["href"]
            yield scrapy.Request(
                item["href"],
                callback=self.get_detail_content,
                meta={"item":deepcopy(item)}
            )
        next_url=response.xpath("//a[text()='下一页']/@href")
        if len(next_url)>0:
            next_url="http://bxjg.circ.gov.cn"+next_url.extract_first()
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
    def get_detail_content(self,response):
        item=response.meta["item"]
        item["当事人"]=response.xpath("//span[@id='zoom']//p[contains(text(),'当事人')][1]/text()")
        if len(item["当事人"])==0:
            item["当事人"]=response.xpath("//span[@id='zoom']//span[contains(text(),'当事人')][1]/text()")

        if len(item["当事人"])>0:
            item["当事人"]=item["当事人"].extract_first().split("：")[-1].strip()
        else:
            item["当事人"]=None
        yield item



