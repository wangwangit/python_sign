# 新版Server酱配置
import json

import requests

# 新版Server酱配置
server_key = 'xxxxxx'

# 企业微信配置
corpid = 'xxx'  # 上面提到的你的企业ID
corpsecret = 'xxx'  # 上图的Secret
agentid = xxx  # 填写你的企业ID，不加引号，是个整型常数,就是上图的AgentId

# 掘金Cookie
jjcookie = 'xxxx'
# 掘金check_in的地址,若默认值不可用,自行替换
check_in_url = 'https://api.juejin.cn/growth_api/v1/check_in?_02B4Z6wo00901xv6hkwAAIDCzDyrNOcq0CMb.oLAAKYjbRQVFHq9fIVQ2q9D-b8HDZihJfANUHIMY62Q-EV.g2eHNgZcITxaXiwTClDT6iWcZsgYdQEA.OxKuo5mfNhXgIkTrmI7lhNTnyKk8e'


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


if __name__ == '__main__':
    checkinUrl = check_in_url
    resp = requests.post(checkinUrl, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37'},
                         cookies={
                             'Cookie': jj_cookie})
    wxPush("掘金签到\n\n" + resp.text)
