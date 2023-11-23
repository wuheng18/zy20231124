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
        return "幼儿"
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
            "儿童早教": "儿童早教",
			"儿童启蒙故事": "儿童启蒙故事",
			"儿童英语启蒙": "儿童英语启蒙",
			"儿童歌曲": "儿童歌曲",
			"儿童玩具": "儿童玩具",
			"儿童绘画": "儿童绘画",
			"睡前故事": "睡前故事",
			"儿童动画": "儿童动画",
			"儿童音乐": "儿童音乐",
			"儿童安全教育": "儿童安全教育",
			"贝瓦儿歌": "贝瓦儿歌",
			"悟空识字": "悟空识字",
			"宝宝巴士": "宝宝巴士",
			"儿歌多多": "儿歌多多",
			"学而思": "学而思"
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
        raw_cookie_line ="buvid3=8B57D3BA-607A-1E85-018A-E8C430023CED42659infoc; b_lsid=BEB8EE7F_18742FF8C2E; bsource=search_baidu; _uuid=DE810E367-B52C-AF6E-A612-EDF4C31567F358591infoc; b_nut=100; buvid_fp=711a632b5c876fa8bbcf668c1efba551; SESSDATA=7624af93%2C1696008331%2C862c8%2A42; bili_jct=141a474ef3ce8cf2fedf384e68f6625d; DedeUserID=3493271303096985; DedeUserID__ckMd5=212a836c164605b7; sid=5h4ruv6o; buvid4=978E9208-13DA-F87A-3DC0-0B8EDF46E80434329-123040301-dWliG5BMrUb70r3g583u7w%3D%3D"
        simple_cookie = http.cookies.SimpleCookie(raw_cookie_line)
        cookie_jar = requests.cookies.RequestsCookieJar()
        cookie_jar.update(simple_cookie)
        return cookie_jar
    def get_dynamic(self,pg):
        result = {}
        
        url= 'https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all?timezone_offset=-480&type=all&page={0}'.format(pg)
        
        rsp = self.fetch(url,cookies=self.getCookie())
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['items']
            for vod in vodList:
                if vod['type'] == 'DYNAMIC_TYPE_AV':
                    ivod = vod['modules']['module_dynamic']['major']['archive']
                    aid = str(ivod['aid']).strip()
                    title = ivod['title'].strip().replace("<em class=\"keyword\">","").replace("</em>","")
                    img =  ivod['cover'].strip()
                    remark = str(ivod['duration_text']).strip()
                    videos.append({
                        "vod_id":aid,
                        "vod_name":title,
                        "vod_pic":img,
                        "vod_remarks":remark
                    })
                result['list'] = videos
                result['page'] = pg
                result['pagecount'] = 9999
                result['limit'] = 90
                result['total'] = 999999
        return result

    def get_hot(self,pg):
        result = {}
        url= 'https://api.bilibili.com/x/web-interface/popular?ps=20&pn={0}'.format(pg)
        rsp = self.fetch(url,cookies=self.getCookie())
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            for vod in vodList:
                aid = str(vod['aid']).strip()
                title = vod['title'].strip().replace("<em class=\"keyword\">","").replace("</em>","")
                img =  vod['pic'].strip()
                remark = str(vod['duration']).strip()
                videos.append({
                    "vod_id":aid,
                    "vod_name":title,
                    "vod_pic":img,
                    "vod_remarks":remark
                })
            result['list'] = videos
            result['page'] = pg
            result['pagecount'] = 9999
            result['limit'] = 90
            result['total'] = 999999
        return result
    def get_rank(self):
        result = {}
        url= 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
        rsp = self.fetch(url,cookies=self.getCookie())
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            for vod in vodList:
                a