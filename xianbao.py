import json
import time
import requests
from bs4 import BeautifulSoup

GjKey = ['红包', '攻略', '优惠', '首发', '大毛', '速度', '作业', '大水', '翼支付', '有水', '白嫖', '0元', '手慢无', '好价']


# 企业微信推送
def wxPush1(message):
    corpid = 'xxx'  # 上面提到的你的企业ID
    corpsecret = 'xxx'  # 上图的Secret
    agentid = xxx  # 填写你的企业ID，不加引号，是个整型常数,就是上图的AgentId
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?' + 'corpid=' + corpid + '&corpsecret=' + corpsecret
    req_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='
    resp = requests.get(token_url).json()
    access_token = resp['access_token']
    data = {
        "touser": "@all",
        "toparty": "@all",
        "totag": "@all",
        "msgtype": "text",
        "agentid": agentid,
        "text": {
            "content": message
        },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    data = json.dumps(data)
    req_urls = req_url + access_token
    res = requests.post(url=req_urls, data=data)
    print(res.text)


def getrikimsg():
    f = open('url.txt', 'r')
    urlList = f.read().splitlines()
    res = requests.get(url='https://www.xianbaocool.cn/category-zuankeba-jingxuan.html', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'},
                       cookies={
                           'Cookie': '__51uvsct__JGYEHCrHijT4u6x2=1; __51vcke__JGYEHCrHijT4u6x2=9ee8bff6-be8a-5261-ad46-05467e1f6e09; __51vuft__JGYEHCrHijT4u6x2=1627613625809; timezone=8; isvip=0; redswitch=0; redsign=; discruxswitch=0; discruxsign=; fanye=0; shuaswitch=0; shuajiange=0; mochu_us_notice_alert=1; PHPSESSID=dhcj0ndl27s2lktuotarq0usf5; night=0; __vtins__JGYEHCrHijT4u6x2=%7B%22sid%22%3A%20%2244b80352-780b-527f-bd78-ec0a75099a96%22%2C%20%22vd%22%3A%2021%2C%20%22stt%22%3A%20307603%2C%20%22dr%22%3A%205994%2C%20%22expires%22%3A%201627615733408%2C%20%22ct%22%3A%201627613933408%7D'})
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'html.parser')
    h2_all = soup.find_all('h2')
    flag = True
    for i in range(len(h2_all)):
        if i == 0:
            continue
        a = h2_all[i].find('a')
        url = a.get('href')
        title = a.get('title')
        if url not in urlList:
            with open("url.txt", "a") as urlTxt:
                urlTxt.write(url + '\n')
            print('标题:%s\n地址:%s' % (title, url))
            urlList.append(url)
            flag = False
            for GJ in GjKey:
                if GJ in title:
                    wxmessage = '<a href=%s>%s</a>' % (url, title)
                    wxPush1(wxmessage)
                    time.sleep(2)

    if flag:
        print('暂无更新')


if __name__ == '__main__':
    getrikimsg()
