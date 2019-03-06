#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 09:42:18 2019

@author: yura
"""
from bs4 import BeautifulSoup
import requests
import warnings
import re
from datetime import datetime
import json
import pandas as pd
import random
import time

name=[]
content=[]
comment_date=[]
reply=[]
append_comment=[]
x=1

#更改User-Agent、cookies、url里面的id、保存的文件名
headers = {
    'User-Agent': '',
    'Connection':'keep-alive',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9'}
cookies={'cookie':''}
url=''



for i in range(100):
    print('正在爬取第'+str(i+1)+'页')
    detail_url=url.format(i)
    res=requests.get(detail_url,headers=headers,cookies=cookies)
    data=re.findall(r'{.*}',res.text)[0]
#    data=res.text[13:-1]
    data=json.loads(data)
#    print(data)
#    data=json.loads(data)
    for item in data['rateDetail']['rateList']:
        name.append(item['displayUserNick'])
        content.append(item['rateContent'])
        comment_date.append(item['rateDate'])
        reply.append(item['reply'])
        x+=1
        #判断是否有追评
        if(item['appendComment']):
            append_comment.append(item['appendComment']['content'])
        else:
            append_comment.append('')
            
    print('第'+str(i+1)+'页爬取完成')
    time.sleep(random.random()*30)
result={'名字':name,'评价日期':comment_date,'评价':content,'追评':append_comment,'回复':reply}
results=pd.DataFrame(result)
results.info()
results.to_excel('产品名字_评价.xlsx')
