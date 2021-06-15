import json
import requests
from requests import post

# TG配置
TG_TOKEN = 'xxx'  # TG机器人的TOKEN
CHAT_ID = 'xxx'  # 推送消息的CHAT_ID
# glados网站的cookie
Cookie = 'xxxxxxxxxxx'


def tgPush(message):
    telegram_message = message  # 需要推送的信息
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
    # 需要签到请删除下面的#号.对齐上面.
    # tgPush(message)
