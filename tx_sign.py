import requests
from requests import post

# 腾讯Cookie,
tx_cookie = 'pgv_pvid=6036319171; _ga=GA1.2.1783440562.1617659868; RK=P2xsmkwOWy; ptcz=962a7a1e67ac2406aab3efc0e7ba23345d7fc91ec4ad99ce16b74cf155b9a28d; tvfe_boss_uuid=fa43a63a3a0c6417; pac_uid=0_c3e468bf96299; o_cookie=1249217495; _gcl_au=1.1.1756066116.1624533069; video_guid=04a5728ac01f5a27; video_platform=2; pgv_info=ssid=s1955050180; _qpsvr_localtk=0.11117530483114613; ptui_loginuin=1249217495; main_login=qq; vqq_access_token=49A7132D22745AA0B41DA1D2B95294D2; vqq_appid=101483052; vqq_openid=5C5817CC0F6C93EB19E63E9B261113B2; vqq_vuserid=248126996; vqq_vusession=n_AsIVjAQADnMa8cxkNpQw..; vqq_refresh_token=45BEE4021749E2ECBC59FD5C67732ADD; login_time_init=2021-7-12 9:17:57; uid=79130810; vqq_next_refresh_time=6592; vqq_login_time_init=1626052686; login_time_last=2021-7-12 9:18:5; vversion_name=8.3.95.0; video_bucketid=4; video_omgid=test_jinfuwu_omgid'
auth_refresh_url = 'https://access.video.qq.com/user/auth_refresh?vappid=11059694&vsecret=fdf61a6be0aad57132bc5cdf78ac30145b6cd2c1470b0cfe&type=qq&g_tk=&g_vstk=406154242&g_actk=982078386&callback=jQuery19107263100220876779_1626052698163&_=1626052698164'

# TG配置
TG_TOKEN = 'xxx'  # TG机器人的TOKEN
CHAT_ID = 'xxx'  # 推送消息的CHAT_ID

# 新版Server酱配置
server_key = 'xxxxxx'

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


# 腾讯视频签到
def tx_sign():
    url1 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2'
    url2 = 'https://v.qq.com/x/bu/mobile_checkin'
    url3 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=1'  # 观看60分钟
    url4 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=7'  # 下载
    url5 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=6'  # 赠送
    url6 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=3'  # 弹幕
    login_headers = {
        'Referer': 'https://v.qq.com',
        'Cookie': tx_cookie
    }
    login = requests.get(auth_refresh_url, headers=login_headers)
    resp_cookie = requests.utils.dict_from_cookiejar(login.cookies)
    if not resp_cookie:
        tgPush('腾讯视频V力值签到通知\n\n' + '获取Cookie失败，Cookie失效')
    arr = tx_cookie.split('; ')
    sign_cookie = ''
    for str in arr:
        if 'vqq_vusession' in str:
            continue
        else:
            sign_cookie += (str + '; ')
    sign_cookie += ('vqq_vusession=' + resp_cookie['vqq_vusession'] + ';')
    sign_headers = {
        'Cookie': sign_cookie,
        'Referer': 'https://m.v.qq.com'
    }
    send_message = ''
    sign1 = response_handle(url1, sign_headers)
    send_message += '链接1' + sign1 + '\n'
    # sign2 = response_handle(url2, sign_headers)
    send_message += '链接2' + '任务未完成' + '\n'
    sign3 = response_handle(url3, sign_headers)
    send_message += '链接3' + sign3 + '\n'
    sign4 = response_handle(url4, sign_headers)
    send_message += '链接4' + sign4 + '\n'
    sign5 = response_handle(url5, sign_headers)
    send_message += '链接5' + sign5 + '\n'
    sign6 = response_handle(url6, sign_headers)
    send_message += '链接6' + sign6 + '\n'
    mes = '腾讯视频V力值签到通知\n\n' + send_message
    return mes


# 处理腾讯视频返回结果
def response_handle(url, sign_headers):
    resp_str = requests.get(url, headers=sign_headers).text
    if '-777903' in resp_str:
        return "已获取过V力值"
    elif '-777902' in resp_str:
        return "任务未完成"
    elif 'OK' in resp_str:
        return "成功，获得V力值：" + resp_str[42:-14]
    else:
        return "执行出错"


if __name__ == '__main__':
    message = tx_sign()
    send_server('腾讯视频签到通知', message)
