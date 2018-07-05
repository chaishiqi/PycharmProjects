# -*- coding:utf-8 -*-

import random
import requests
import time
import pymysql
from demo.crawler.agent import agents
from demo.crawler.detail_crawler import DetailCrawler


class Crawl(object):
    def __init__(self):
        self.main_url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0'
        self.header = {
            'Host': 'www.lagou.com',
            'User-Agent': random.choice(agents),
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4?labelWords=sug&fromSearch=true&suginput=yunwei',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Anit-Forge-Token': 'None',
            'X-Anit-Forge-Code': '0',
            'Content-Length': '37',
            'Cookie': 'WEBTJ-ID=20180704101725-1646314800fe80-07b49f6733c3e3-3c365402-1440000-16463148010b53; _gat=1; user_trace_token=20180704101734-69d89c66-7f30-11e8-bde7-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rsv_spt%3D1%26rsv_iqid%3D0x9f87c0270000e37e%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_sug3%3D4%26rsv_sug1%3D4%26rsv_sug7%3D100; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; LGUID=20180704101734-69d8a036-7f30-11e8-bde7-525400f775ce; X_HTTP_TOKEN=772ae384576f84bdb7219f06aa997931; LG_LOGIN_USER_ID=d7a03e43a6df91e72ea41007cbf0b98874269e6666a8a585; _putrc=9F3547C565AC2E4D; JSESSIONID=ABAAABAAAIAACBI16970F5E0E2E0C2A43EF42CC1CD6C94D; login=true; unick=%E6%9F%B4%E4%B8%96%E7%90%A6; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=55; gate_login_token=410738e005d8a34f15176da71e4f5d74a23895ff1e7edb27; _gid=GA1.2.860888104.1530670646; _ga=GA1.2.1017355783.1530670645; LGSID=20180704101734-69d89ea5-7f30-11e8-bde7-525400f775ce; LGRID=20180704101825-87f3bf86-7f30-11e8-bde8-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530670645; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530670696; TG-TRACK-CODE=search_code; SEARCH_ID=8db67a9ae0214d519c77b561fbd611f6; index_location_city=%E5%8C%97%E4%BA%AC',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
    def insertMysql(self,datalist):
        try:
            conn = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                passwd='111111',
                db='lagou',
                charset='utf8'
            )
            cursor = conn.cursor()
            effect_row = cursor.executemany("insert into yunwei("
                                            "positionId,position_url,positionName,companyShortName,"
                                            "companyFullName,createTime,salary,"
                                            "job_bt,advantage,workYear,"
                                            "district,linestaion,education,"
                                            "industryField,companySize,work_addr) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",datalist)
            print('成功插入%d条' %effect_row)
        except Exception as e:
            print(e)
        finally:
            conn.commit()
            cursor.close()
            conn.close()

    def crawler(self,page):
        self.page = page
        if(self.page == 1):
            first = 'true'
        else:
            first = 'false'
        form = {'first':first,'kd':u'运维','pn':str(page)}
        time.sleep(random.randint(2,5))
        html = requests.post(self.main_url,data=form,headers=self.header)
        result = html.json()
        position_list = result['content']['positionResult']['result']
        datalist= []
        for position in position_list:
            linestaion = position['linestaion']     #地铁沿线
            companyShortName = position['companyShortName']     #公司简称
            positionId = str(position['positionId'])   #职位ID
            companyFullName = position['companyFullName']       #公司全称
            createTime = position['createTime']     #发布时间
            workYear = position['workYear']     #工作年限
            district = position['district']     #地区
            positionName = position['positionName']     #职位名
            salary = position['salary']     #薪资
            industryField = position['industryField']   #所属领域
            companySize = position['companySize']       #公司规模
            education = position['education']       #学历
            decrawl = DetailCrawler(positionId)
            time.sleep(random.randint(2, 5))
            dedict = decrawl.detail_crawl()
            work_addr =  dedict['work_addr']    #工作地址
            advantage = dedict['advantage']     #优势
            job_bt = dedict['job_bt']           #工作职责
            position_url = dedict['position_url']   #招聘页
            datalist.append((positionId,position_url,positionName,companyShortName,companyFullName,createTime,salary,job_bt,advantage,workYear,district,linestaion,education,industryField,companySize,work_addr))
        self.insertMysql(datalist)

if __name__ == '__main__':
    craw = Crawl()
    for page in range(1,31):
        print('正在爬第 %d 页 >>>>' %page)
        craw.crawler(page)