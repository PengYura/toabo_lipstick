#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 15:35:26 2018

@author: yura
"""
import requests
import re
from bs4 import BeautifulSoup
import json
import pandas as pd
import time

#修改输入、输出文件名称

sale=[]
df=pd.read_excel('口红ID.xlsx')
df=df[600:]
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer':'https://www.taobao.com/',
    'Connection':'keep-alive'}
cookies={'cookie':''}


url='https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/?jsv=2.5.0&appKey=12574478&t=1545890324697&sign=b3019d1cfa9fca53e96c2dce375af631&api=mtop.taobao.detail.getdetail&v=6.0&ttid=2018%40taobao_iphone_9.9.9&utdid=123123123123123&isSec=0&ecode=0&AntiFlood=true&AntiCreep=true&H5Request=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data=%7B%22itemNumId%22%3A%22{a}%22%2C%22exParams%22%3A%22%7B%5C%22id%5C%22%3A%5C%22{b}%5C%22%2C%5C%22abtest%5C%22%3A%5C%2214%5C%22%2C%5C%22rn%5C%22%3A%5C%2288c67406326ce50a3b7c45a84fd373f8%5C%22%2C%5C%22sid%5C%22%3A%5C%221358529dab8ea682d11893feec138136%5C%22%7D%22%2C%22detail_v%22%3A%223.1.1%22%2C%22ttid%22%3A%222018%40taobao_iphone_9.9.9%22%2C%22utdid%22%3A%22123123123123123%22%7D'

#url='https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/?jsv=2.5.0&appKey=12574478&t=1545097454728&sign=7a334fe28be77a280b6039cf82f9ec5a&api=mtop.taobao.detail.getdetail&v=6.0&ttid=2018%40taobao_iphone_9.9.9&utdid=123123123123123&isSec=0&ecode=0&AntiFlood=true&AntiCreep=true&H5Request=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data=%7B%22itemNumId%22%3A%22{}%22%2C%22exParams%22%3A%22%7B%5C%22id%5C%22%3A%5C%22{}%5C%22%2C%5C%22abtest%5C%22%3A%5C%2215%5C%22%2C%5C%22rn%5C%22%3A%5C%22fce108850a452024b097fba77551c041%5C%22%2C%5C%22sid%5C%22%3A%5C%2210bedb1db0e75ee9d5060821336dde24%5C%22%7D%22%2C%22detail_v%22%3A%223.1.1%22%2C%22ttid%22%3A%222018%40taobao_iphone_9.9.9%22%2C%22utdid%22%3A%22123123123123123%22%7D'

k=0
for id in df['商品编号']:
    k=k+1
    print('正在爬取第{}个产品：{}'.format(k,id),)
    time.sleep(1)
    full_url=url.format(a=id,b=id)    
    res=requests.get(full_url,timeout=20)
    res.encoding='utf-8'
    html=res.text
    data=re.findall(".*sellCount(.*)vagueSellCount.*",html)
    if(len(data)):
        sale.append(data[0][5:-5])
    else:
        sale.append('未找到')
    


df['销量']=sale
df.to_excel('口红allinfo.xlsx')


