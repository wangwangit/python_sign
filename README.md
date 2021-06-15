# 各种签到脚本
### 联通营业厅签到脚本 sign.py
* 替换手机号,密码,appId即可
* 默认配置了TG推送,需要替换自己的tgBot秘钥
* appId获取最方便的方法就是手机文件管理器，找到路径为 Unicom/appid 的文件打开复制。
* 出现No module named "Crypto" 解决办法:https://www.cnblogs.com/fawaikuangtu123/p/9761943.html

### GLaDOS网站签到脚本 glados_sign.py
* 网站地址注册GLaDOS(注册地址在 https://github.com/glados-network/GLaDOS 实时更新), 并输入邀请码:HZCYH-YG3DE-K39MO-VCAPX 激活
* 若不想走我的邀请链接,直接百度也可搜索到.另外edu邮箱可以获得一年免费额度  
* 默认配置了TG推送,需要替换自己的tgBot秘钥
* 填写网站glados的cookie即可
* 推荐定时任务 30 10 * * *  ,即每天10.30签到.

