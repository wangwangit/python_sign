import json
import locale
from time import time, localtime, strftime
import cn2an as cn2an
import cv2
import numpy as np
import requests
from PIL import ImageFont, Image, ImageDraw

# 天行数据的key
tx_key = 'xxxxx'


def img():
    # 加载背景图片
    bk_img = cv2.imread("base.jpg")
    # 设置需要显示的字体
    fontpath = "font/SIMYOU.TTF"
    font = ImageFont.truetype(fontpath, 80)
    img_pil = Image.fromarray(bk_img)
    draw = ImageDraw.Draw(img_pil)
    # 绘制文字信息
    today = int(strftime("%w"))
    if 0 == today:
        today = '星期日'
    else:
        today = '星期' + cn2an.an2cn(today)
    # 自行调整此处文字所在位置
    draw.text((430, 55), today, font=font, fill=(255, 255, 0))
    font_small = ImageFont.truetype(fontpath, 35)
    font_sentence = ImageFont.truetype(fontpath, 16)
    draw.text((750, 115), todayYear(), font=font_small, fill=(255, 255, 0))
    draw.text((110, 520), news(), font=font_small, fill=(0, 0, 0))
    font_red = ImageFont.truetype(fontpath, 40)
    draw.text((110, 1700), verse(), font=font_red, fill=(255, 255, 0))
    bk_img = np.array(img_pil)
    # 展示图片,不需要可注释
    cv2.imshow("add_text", bk_img)
    cv2.waitKey()
    cv2.imwrite("news.jpg", bk_img)


# 每日简报
def news():
    req_url = 'http://api.tianapi.com/bulletin/index?key=' + tx_key
    response = requests.get(req_url)
    loads = json.loads(response.text)
    news_list = loads.get('newslist')
    news = ''
    for index in range(len(news_list)):
        if index > 14:
            return news
        title = news_list[index].get('title')
        if len(title) > 25:
            title = title[:25] + '\n   ' + title[25:]
        news += str(index + 1) + '、' + title + '\n\n'
    return news


# 名言
def verse():
    req_url = 'http://api.tianapi.com/txapi/lzmy/index?key=' + tx_key
    response = requests.get(req_url)
    loads = json.loads(response.text)
    verse_list = loads.get('newslist')
    source = verse_list[0].get('source')
    saying = verse_list[0].get('saying')
    verse_str = '【微语】 ' + saying
    resp_verse = verse_str
    if len(verse_str) > 22:
        resp_verse = verse_str[:23] + '\n' + verse_str[23:]
    return resp_verse


# 年月日
def todayYear():
    return strftime("%Y年%m月%d日", localtime(time()))


# 精美局子
def sentence():
    req_url = 'http://api.tianapi.com/txapi/sentence/index?key=' + tx_key
    response = requests.get(req_url)
    loads = json.loads(response.text)
    verse_list = loads.get('newslist')
    content = verse_list[0].get('content')
    if len(content) > 18:
        content = content[:18] + '\n' + content[18:36] + '\n' + content[36:]
    return content


if __name__ == '__main__':
    img()
