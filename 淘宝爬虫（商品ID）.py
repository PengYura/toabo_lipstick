from bs4 import BeautifulSoup
import requests
import warnings
import re
from datetime import datetime
import json
import pandas as pd
import random
import time
from datetime import datetime
#from selenium import webdriver


# 每次爬取时cookies都需要重新粘贴使用。
# 网址就是大网页网址（修改s={}）
# 修改文件名称

headers = {
    'User-Agent': '',
    'Referer':'https://www.taobao.com/',
    'Connection':'keep-alive'}
url = 'https://s.taobao.com/search?q=%E5%8F%A3%E7%BA%A2&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&s={}'

cookies={'cookie':''}

price=[]
name=[]
address=[]
count=[]
title=[]
id_=[]
detail_url=[]
sale=[]
ji=1

for i in range(51,51):
    value=44*i
    url_range=url.format(value)
    res=requests.get(url_range,headers=headers,cookies=cookies,timeout=10)
    res.encoding='utf-8'
    # 正则从网址中提取信息
    print('正在爬取第'+str(ji)+'页')
    data=re.findall('g_page_config =(.*?)g_srp_loadCss',res.text,re.S)[0].strip()[:-1]
    content=json.loads(data,encoding='utf-8')
    list_=content['mods']['itemlist']['data']['auctions']
    for item in list_:
        name.append(item['nick'])
        price.append(item['view_price'])
        address.append(item['item_loc'])
        count.append(item['view_sales'].replace('人收货',''))
        title.append(item['raw_title'])
        id_.append(item['nid']) #nid
        detail_url.append(item['detail_url'])
    ji+=1
    time.sleep(random.random()*100+3)
    
print('爬取完成')
result={'店铺名称':name,'商品标题':title,'价格':price,'地址':address,'商品编号':id_,'收货人数':count,'详情页网址':detail_url}
#result={'店铺名称':name[:177],'商品标题':title[:177],'价格':price[:177],'地址':address[:177],'商品编号':id_[:177],'收货人数':count[:177],'详情页网址':detail_url[:177]}
results=pd.DataFrame(result)
results.info()
results.to_excel('口红ID.xlsx')

