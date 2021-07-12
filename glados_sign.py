import json
import requests
from requests import post

# TG配置
TG_TOKEN = 'xxx'  # TG机器人的TOKEN
CHAT_ID = 'xxx'  # 推送消息的CHAT_ID
# glados网站的cookie
Cookie = 'xxxxxxxxxxx'

# 新版Server酱配置
server_key = 'xxxxxxxxxx'

# 企业微信配置
corpid = 'xxx'     # 上面提到的你的企业ID
corpsecret = 'xxx'     # 上图的Secret
agentid = xxx  # 填写你的企业ID，不加引号，是个整型常数,就是上图的AgentId

# 企业微信推送
def wxPush(message):
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


if __name__ == '__main__':
    checkinUrl = 'https://glados.rocks/api/user/checkin'
    resp = requests.post(checkinUrl, data={'token': 'glados_network'}, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37'},
                         cookies={
                             'Cookie': Cookie})
    message = 'GLaDOS梯子签到 : \n\n' + json.loads(resp.text).get('message')
    print(message)
    # Server酱通知
    send_server('Glados签到通知', message)
    # Telegram通知
    # tgPush(message)
