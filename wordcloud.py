import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import re
import jieba
import wordcloud
import matplotlib.pyplot as plt
from collections import Counter
from PIL import Image
jieba.load_userdict("new.txt") 



df=pd.read_excel('完美日记评价.xlsx')

comments=str()
for comment in df['评价']:
    comments=comments+comment



stopwords = {}.fromkeys([ line.rstrip() for line in open('stopwords.txt') ])
segs = jieba.cut(comments,cut_all=False)

final =[]
for seg in segs:
#    seg = seg.encode('gbk')、
    if seg not in stopwords:
            final.append(seg)

#print(final)
cloud_text=final       
#cloud_text="".join(final)

#print(cloud_text)
fre= Counter(cloud_text)
#print(cloud_text)
print(fre)

mask = np.array(Image.open('wmrj.jpg')) # 定义词频背景
wc = wordcloud.WordCloud(
    font_path='Hiragino Sans GB.ttc', # 设置字体格式
    mask=mask, # 设置背景图
    max_words=30, # 最多显示词数
    max_font_size=200 # 字体最大值
)

print(type(fre))
dd=pd.DataFrame({'k':fre})
dd.to_excel('完美日记高频词.xlsx')
#print(fre)

#wc=wordcloud.generate(cloud_text)
wc.generate_from_frequencies(fre) # 从字典生成词云
#wc.generate(cloud_text) 
image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
plt.imshow(wc) # 显示词云
plt.axis('off') # 关闭坐标轴
plt.show() # 显示图像
wc.to_file('完美日记_pic.png')

