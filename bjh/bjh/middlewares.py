# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy import signals




class RandomUserAgent:
    def process_request(self,request,spider):
        # print(spider.settings["UAS"])
        ua=random.choice(spider.settings["UAS"])
        request.headers["User-Agent"]=ua



# class CheckUserAgent:
#     def process_response(self,request,response,spider):
#
#         return response