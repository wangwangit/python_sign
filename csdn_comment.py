import json
import random
import time
from urllib import parse
import requests
from bs4 import BeautifulSoup
from requests import post

# CSDN相关配置
# cookie
csdn_cookies = 'xxxxxxx'
# csdn的个人ID
user_id = 'xxxxx'
# csdn的个人名称
user_name = 'xxxxx'

# TG配置
TG_TOKEN = 'xxx'  # TG机器人的TOKEN
CHAT_ID = 'xxx'  # 推送消息的CHAT_ID

# 新版Server酱配置
server_key = 'xxxx'


# 新版Server酱推送
def send_server(title, content):
    server_content = {'text': title, 'desp': content}
    server_url = "https://sctapi.ftqq.com/%s.send" % server_key
    resp = requests.post(server_url, params=server_content)
    print('新版Server酱推送状态码为: %s' % resp.status_code)


# Telegram推送
def tgPush(telegram_message):
    params = (
        ('chat_id', CHAT_ID),
        ('text', telegram_message),
        ('parse_mode', "Markdown"),  # 可选Html或Markdown
        ('disable_web_page_preview', "yes")
    )
    telegram_url = "https://api.telegram.org/bot" + TG_TOKEN + "/sendMessage"
    post(telegram_url, params=params)


# 获取随机的请求头
def get_header():
    agents = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]
    return random.choice(agents)


# 随机请求头
random_header = {'User-Agent': get_header()}


# 获取随机的代理ip
def get_ip():
    # 代理ip爬取地址
    ip_url = 'http://ip.yqie.com/proxyhttps/'
    ip_result = requests.get(ip_url, headers=random_header)
    soup = BeautifulSoup(ip_result.text, 'html.parser')
    td_all = soup.find_all('td')
    ip_all = td_all[1:-2:6]
    ip_port = td_all[2:-3:6]
    ip_type = td_all[4:-5:6]
    index = random.randint(0, len(ip_all))
    ip = ip_all[index].text
    port = ip_port[index].text
    ip_type = ip_type[index].text
    proxy = ip_type.lower() + '://' + ip + ':' + port
    print("代理ip为: " + proxy)
    proxies = {ip_type.lower(): proxy}
    return proxies


# 文章爬取地址
request_url = 'https://blog.csdn.net/api/articles?type=more&category=java&shown_offset=0'
# 评论回复地址
submit_url = 'https://blog.csdn.net/phoenix/web/v1/comment/submit'
# 评论获取地址
comment_url = 'https://blog.csdn.net/phoenix/web/v1/comment/list/'
# 个人文章获取地址
reply_url = 'https://blog.csdn.net/community/home-api/v1/get-business-list?page=1&size=100&businessType=blog&orderby' \
            '=&noMore=false&username=' + user_id

# 评论
texts = ['膜拜大佬,哈哈哈', '写的很棒啊，让我加深了印象', '感谢分享，文章干货满满', '大佬666，看了之后受益很大', '认真看完了，浅显易懂，学习到了。', '写的好，原创不易，必须支持一下!',
         '好文，值得点赞', '好文！希望博主以后多多分享哈！', '码字不易，欢迎回访!', '活到老学到老，支持原创', '优秀优秀，必须给个大大的赞', '大佬的文章让我受益颇多', '大佬出品，必属精品',
         '写的不错，顶个贴，点个赞，嘿嘿！', '很棒呀，学习啦，谢谢分享！', '大佬的文章让我受益匪浅,感谢博主！', '放弃不难，但坚持一定很酷！',
         '看完大佬的文章，我的心情竟是久久不能平静。正如老子所云：大音希声，大象无形。我现在终于明白我缺乏的是什么了。']


# CSDN评论文章
def comment():
    size = 10
    resp_msg = ''
    # 反爬设置
    requests.session().keep_alive = False  # 关闭多余链接
    requests.session().proxies = get_ip()  # 配置代理
    # 获取CSDN文章列表
    response = requests.get(request_url, headers=random_header)
    loads = json.loads(response.text)
    if 'false' == loads.get('status'):
        resp_msg = '获取文章列表失败'
        send(send_type, 'CSDN评论异常', resp_msg)
    else:
        i = 1
        for article in loads.get('articles'):
            if i > size:
                break
            # 文章ID
            article_id = article.get('id')
            # 文章名字
            article_title = article.get('title')
            # 文章url
            article_url = article.get('url')
            # 获取评论
            get_comment_url = comment_url + article_id + '?page=1&size=100&commentId='
            comment_resp = requests.get(get_comment_url, headers=random_header)
            comment_json = json.loads(comment_resp.text)
            comment_list = comment_json.get('data').get('list')
            name_list = []
            for com in comment_list:
                nick_name = com.get('info').get('nickName')
                name_list.append(nick_name)
            if user_name in name_list:
                continue
            else:
                params = {'content': random.choice(texts), 'commentId': '', 'articleId': article['id']}
                resp = requests.post(submit_url, params=params, headers=random_header,
                                     cookies={'Cookie': csdn_cookies})
                if 200 == resp.status_code:
                    msg = str(
                        i) + '⃣️ ' + '<a href=' + '"' + article_url + '"' + '>' + article_title + '------评论成功' + '</a> \n\n '
                    resp_msg += msg
                    print(msg)
                    i += 1
                    time.sleep(random.uniform(random.random() * 2, random.random() * 20))
                else:
                    continue
        return resp_msg


if __name__ == '__main__':
    message = comment()
    send_server('CSDN评论通知', message)
