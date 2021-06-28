import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import requests
from bs4 import BeautifulSoup

# 发送者邮件
sender = 'xxxx@qq.com'
# 邮件内容
content = '我最帅'
# 邮件标题
title = '我最帅'
# 在邮箱网站申请授权码，不是自己的登录密码
secret = 'xxx'


def send(receiver):
    smtpObj = smtplib.SMTP('smtp.qq.com', 25)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(sender, secret)
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = Header(title, 'utf-8')
    smtpObj.sendmail(sender, receiver, message.as_string())
    smtpObj.quit()


# 读取文件,获取收件人,每行填写一个邮箱!
def readMail():
    resp = ''
    with open('mail.txt', 'r') as f:
        receiverList = f.read().splitlines()
    for receiver in receiverList:
        resp += receiver + ','
    return resp[0:-1]


if __name__ == '__main__':
    send(readMail())
