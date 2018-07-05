# -*- coding:utf-8 -*-

import requests
from urllib import request
from bs4 import BeautifulSoup

class DetailCrawler(object):
    def __init__(self,postID):
        self.url = 'https://www.lagou.com/jobs/{}.html'.format(postID)
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'WEBTJ-ID=20180704101725-1646314800fe80-07b49f6733c3e3-3c365402-1440000-16463148010b53; user_trace_token=20180704101734-69d89c66-7f30-11e8-bde7-525400f775ce; LGUID=20180704101734-69d8a036-7f30-11e8-bde7-525400f775ce; X_HTTP_TOKEN=772ae384576f84bdb7219f06aa997931; LG_LOGIN_USER_ID=d7a03e43a6df91e72ea41007cbf0b98874269e6666a8a585; TG-TRACK-CODE=search_code; SEARCH_ID=46e26d2df1a0424f8ea08f8cb4c4d520; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=ABAAABAAAIAACBI16970F5E0E2E0C2A43EF42CC1CD6C94D; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F4394984.html; _putrc=9F3547C565AC2E4D; login=true; unick=%E6%9F%B4%E4%B8%96%E7%90%A6; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=55; gate_login_token=2e2e020cf900967406897fe4424bbb9ff48f67afbf1cca9f; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530670645; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530685465; _gid=GA1.2.860888104.1530670646; _ga=GA1.2.1017355783.1530670645; LGSID=20180704142433-ea7e66fe-7f52-11e8-be05-525400f775ce; LGRID=20180704142434-eb53ecf4-7f52-11e8-be05-525400f775ce',
            'Host': 'www.lagou.com',
            'Referer': self.url,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
        }

    def detail_crawl(self):
        response = requests.post(self.url,headers=self.header)
        soup = BeautifulSoup(response.content)
        advantage = soup.select('.job-advantage')[0].get_text()
        job_bt = soup.select('.job_bt')[0].get_text()
        #work_label = soup.select('div.work_addr')
        #print(work_label)
        work_addr = soup.select('div.work_addr')[0].get_text(strip=True).strip("查看地图")
        #print(work_addr)
        return {'advantage':advantage,'job_bt':job_bt,'work_addr':work_addr,'position_url':self.url}

if __name__ == '__main__':
    despider = DetailCrawler('4394984')
    despider.detail_crawl()