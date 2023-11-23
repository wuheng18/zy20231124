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
        return "中国文化"
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
        	"庄子":"庄子",
		    "论语":"论语",
		    "博通":"博通",
		    "丹道":"丹道",
			"九宫八卦":"九宫八卦",			
			"河图洛书":"河图洛书",
			"道德经":"道德经",
			"奇门遁甲":"奇门遁甲",
			"大六壬":"大六壬",
			"梅花易数":"梅花易数",
			"易经":"易经",
			"黄帝内经":"黄帝内经",
			"山海经":"山海经",
			"南华经":"南华经",
			"冲虚经":"冲虚经",
			"文始真经":"文始真经"
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
        raw_cookie_line = "buvid3=CFF74DA7-E79E-4B53-BB96-FC74AB8CD2F3184997infoc; LIVE_BUVID=AUTO4216125328906835; rpdid=|(umRum~uY~R0J'uYukYukkkY; balh_is_closed=; balh_server_inner=__custom__; PVID=4; video_page_version=v_old_home; i-wanna-go-back=-1; CURRENT_BLACKGAP=0; blackside_state=0; fingerprint=8965144a609d60190bd051578c610d72; buvid_fp_plain=undefined; CURRENT_QUALITY=120; hit-dyn-v2=1; nostalgia_conf=-1; buvid_fp=CFF74DA7-E79E-4B53-BB96-FC74AB8CD2F3184997infoc; CURRENT_FNVAL=4048; DedeUserID=85342; DedeUserID__ckMd5=f070401c4c699c83; b_ut=5; hit-new-style-dyn=0; buv