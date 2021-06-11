# coding=utf-8
import re
from time import sleep
import datetime
import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64

from requests import post

# 此处改为自己的配置 手机号, 密码, appId
phone = 'xxx'
password = 'xxx'
pid = 'xxx'
# TG配置
TG_TOKEN = 'xxx'  # TG机器人的TOKEN
CHAT_ID = 'xxx'  # 推送消息的CHAT_ID


class UnicomSign():

    def __init__(self):
        self.UA = None
        self.VERSION = '8.0200'
        self.request = requests.Session()
        self.resp = '联通营业厅签到通知 \n\n'
        self.pid = pid

    # 加密算法
    def rsa_encrypt(self, str):
        # 公钥
        publickey = '''-----BEGIN PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDc+CZK9bBA9IU+gZUOc6
        FUGu7yO9WpTNB0PzmgFBh96Mg1WrovD1oqZ+eIF4LjvxKXGOdI79JRdve9
        NPhQo07+uqGQgE4imwNnRx7PFtCRryiIEcUoavuNtuRVoBAm6qdB0Srctg
        aqGfLgKvZHOnwTjyNqjBUxzMeQlEC2czEMSwIDAQAB
        -----END PUBLIC KEY-----'''
        rsakey = RSA.importKey(publickey)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(str.encode('utf-8')))
        return cipher_text.decode('utf-8')

    # 用户登录
    def login(self, mobile, passwd):
        self.UA = 'Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36; unicom{version:android@' + self.VERSION + ',desmobile:' + mobile + '};devicetype{deviceBrand:Xiaomi,deviceModel:MI 6};{yw_code:}'
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        headers = {
            'Host': 'm.client.10010.com',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'Cookie': 'devicedId=20be54b981ba4188a797f705d77842d6',
            'User-Agent': self.UA,
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip',
            'Content-Length': '1446'
        }
        login_url = 'https://m.client.10010.com/mobileService/login.htm'
        login_data = {
            "deviceOS": "android9",
            "mobile": self.rsa_encrypt(mobile),
            "netWay": "Wifi",
            "deviceCode": "20be54b981ba4188a797f705d77842d6",
            "isRemberPwd": 'true',
            "version": "android@" + self.VERSION,
            "deviceId": "20be54b981ba4188a797f705d77842d6",
            "password": self.rsa_encrypt(passwd),
            "keyVersion": 1,
            "provinceChanel": "general",
            "appId": self.pid,
            "deviceModel": "MI 6",
            "deviceBrand": "Xiaomi",
            "timestamp": timestamp
        }

        res1 = self.request.post(login_url, data=login_data, headers=headers)
        if res1.status_code == 200:
            print(">>>获取登录状态成功！")
            self.resp += '>>>获取登录状态成功！\n\n'

        else:
            print(">>>获取登录状态失败！")
            self.resp += '>>>获取登录状态失败！\n\n'

        sleep(3)

    # 每日签到领积分、1g流量日包
    def daysign(self):
        headers = {
            "user-agent": self.UA,
            "referer": "https://img.client.10010.com",
            "origin": "https://img.client.10010.com"
        }
        res0 = self.request.post("https://act.10010.com/SigninApp/signin/getIntegral", headers=headers)
        if res0.json()['status'] == '0000':
            print(">>>签到前积分：" + res0.json()['data']['integralTotal'])
            self.resp += ">>>签到前积分：" + res0.json()['data']['integralTotal'] + '\n\n'
        else:
            print(">>>获取积分信息失败！")
            self.resp += '获取积分信息失败' + '\n\n'

        res1 = self.request.post("https://act.10010.com/SigninApp/signin/getContinuous", headers=headers)
        sleep(3)
        if res1.json()['data']['todaySigned'] == '1':
            res2 = self.request.post("https://act.10010.com/SigninApp/signin/daySign", headers=headers)

            print('>>>签到成功！')
            self.resp += '>>>签到成功！\n\n'
        else:
            print('>>>今天已签到！')
            self.resp += '>>>今天已签到！\n\n'

        # 看视频，积分翻倍
        sleep(3)
        res3 = self.request.post("https://act.10010.com/SigninApp/signin/bannerAdPlayingLogo", headers=headers)
        if res3.json()['status'] == '0000':
            self.resp += '>>>积分翻倍成功！\n\n'
            print(">>>积分翻倍成功！")
        else:
            print(res3.json()['msg'])
            self.resp += res3.json()['msg'] + '\n\n'

        res4 = self.request.post("https://act.10010.com/SigninApp/signin/getIntegral", headers=headers)
        if res4.json()['status'] == '0000':
            print(">>>签到后积分：" + res4.json()['data']['integralTotal'])
            self.resp += ">>>签到后积分：" + res4.json()['data']['integralTotal'] + '\n\n'
        else:
            print(">>>获取积分信息失败！")
            self.resp += '>>>获取积分信息失败！\n\n'

        # 每日领取1G流量日包
        res5 = self.request.post("https://act.10010.com/SigninApp/doTask/finishVideo", headers=headers)
        res6 = self.request.post("https://act.10010.com/SigninApp/doTask/getTaskInfo", headers=headers)
        res7 = self.request.post("https://act.10010.com/SigninApp/doTask/getPrize", headers=headers)
        if res7.json()['status'] == '0000':
            print(">>>1G流量日包领取成功！")
            self.resp += '>>>1G流量日包领取成功！\n\n'
        else:
            print(">>>1G流量日包任务失败！")
            self.resp += '>>>1G流量日包任务失败！\n\n'

    # 每日任务
    def daytask(self):
        headers = {
            "user-agent": self.UA,
            "referer": "https://img.client.10010.com",
            "origin": "https://img.client.10010.com"
        }
        # 娱乐中心--每日打卡
        data1 = {
            'methodType': 'signin',
            'clientVersion': self.VERSION,
            'deviceType': 'Android',
        }
        res1 = self.request.post("https://m.client.10010.com/producGame_signin", data=data1, headers=headers)
        res1.encoding = 'utf-8'
        print(">>>每日打卡：", res1.json()['respDesc'])
        self.resp += ">>>每日打卡：" + res1.json()['respDesc'] + '\n\n'
        # 沃之树任务
        res5 = self.request.post("https://m.client.10010.com/mactivity/arbordayJson/arbor/3/0/3/grow.htm",
                                 headers=headers)
        print(">>>每日浇水：", res5.json()['msg'])
        self.resp += ">>>每日浇水：" + res5.json()['msg'] + '\n\n'
        # 签到看视频，下载APP流量奖励
        print(">>>签到看视频，下载APP流量奖励任务开始...")
        data5 = {
            'stepflag': 22
        }
        data6 = {
            'stepflag': 23
        }
        for i in range(3):
            res5 = self.request.post("https://act.10010.com/SigninApp/mySignin/addFlow", data=data5, headers=headers)
            sleep(3)
            res6 = self.request.post("https://act.10010.com/SigninApp/mySignin/addFlow", data=data6, headers=headers)
        print(">>>签到看视频，下载APP流量奖励任务完成！")
        # 金币抽奖免费3次
        res7 = self.request.post("https://m.client.10010.com/dailylottery/static/textdl/userLogin", headers=headers)
        data8 = {
            'usernumberofjsp': re.findall(r"encryptmobile=(.+?)';", res7.text)[0],
            'flag': 'convert'
        }
        for i in range(3):
            res8 = self.request.post("https://m.client.10010.com/dailylottery/static/doubleball/choujiang", data=data8,
                                     headers=headers)
            print(">>>金币抽奖：", res8.json()['RspMsg'])
            self.resp += ">>>金币抽奖：" + res8.json()['RspMsg'] + '\n\n'
            sleep(3)


# TG推送
def tgPush(telegram_message):
    params = (
        ('chat_id', CHAT_ID),
        ('text', telegram_message),
        ('parse_mode', "Html"),  # 可选Html或Markdown
        ('disable_web_page_preview', "yes")
    )
    telegram_url = "https://api.telegram.org/bot" + TG_TOKEN + "/sendMessage"
    post(telegram_url, params=params)


if __name__ == '__main__':
    user = UnicomSign()
    user.login(phone, password)  # 用户登录   这里需要更改
    user.daysign()  # 日常签到领积分，1g流量日包
    user.daytask()  # 日常任务
    tgPush(user.resp)
