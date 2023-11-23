#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import json
import time
import base64

class Spider(Spider):  # 元类 默认的元类 type
    def getName(self):
        return "初中"
    def init(self,extend=""):
        print("============{0}============".format(extend))
        pass
    def isVideoFormat(self,url):
        pass
    def manualVideoCheck(self):
        pass
    def homeContent(self,filter):
        result = {}
        cateManual = {
            "7年级地理":"7年级地理",
       "7年级生物":"7年级生物",
       "7年级物理":"7年级物理",
       "7年级化学":"7年级化学",
       "8年级语文":"8年级语文",
       "8年级数学":"8年级数学",
       "8年级英语":"8年级英语",
       "8年级历史":"8年级历史",
       "8年级地理":"8年级地理",
       "8年级生物":"8年级生物",   
       "8年级物理":"8年级物理",
       "8年级化学":"8年级化学",
       "9年级语文":"9年级语文",
       "9年级数学":"9年级数学",
       "9年级英语":"9年级英语",
       "9年级历史":"9年级历史",
       "9年级地理":"9年级地理",
       "9年级生物":"9年级生物",
       "9年级物理":"9年级物理",
       "9年级化学":"9年级化学"
        }
        classes = []
        for k in cateManual:
            classes.append({
                'type_name':k,
                'type_id':cateManual[k]
            })
        result['class'] = classes
        if(filter):
            result['filters'] = self.config['filter']
        return result
    def homeVideoContent(self):
        result = {
            'list':[]
        }
        return result
    cookies = ''
    def getCookie(self):
        import requests
        import http.cookies
        # 这里填cookie
        raw_cookie_line ="buvid3=8B57D3BA-607A-1E85-018A-E8C430023CED42659infoc; b_lsid=BEB8EE7F_18742FF8C2E; bsource=search_baidu; _uuid=DE810E367-B52C-AF6E-A612-EDF4C31567F358591infoc; b_nut=100; buvid_fp=711a632b5c876fa8bbcf668c1efba551; SESSDATA=7624af93%2C1696008331%2C862c8%2A42; bili_jct=141a47