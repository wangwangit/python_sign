# 各种签到脚本
### 联通营业厅签到脚本 unicom_sign.py 可以点个star再走嘛!!!
* 替换手机号,密码,appId即可
* 默认配置了TG推送,需要替换自己的tgBot秘钥
* appId获取最方便的方法就是手机文件管理器，找到路径为 Unicom/appid 的文件打开复制。
* 出现No module named "Crypto" 解决办法:https://www.cnblogs.com/fawaikuangtu123/p/9761943.html
* 新增Github Action签到方式,地址https://github.com/asa1253/HiCnUnicom

### GLaDOS网站签到脚本 glados_sign.py
* 网站地址注册GLaDOS(注册地址在 https://github.com/glados-network/GLaDOS 实时更新), 并输入邀请码:HZCYH-YG3DE-K39MO-VCAPX 激活
* 若不想走我的邀请链接,直接百度也可搜索到.另外edu邮箱可以获得一年免费额度  
* 默认配置了TG推送,需要替换自己的tgBot秘钥
* 填写网站glados的cookie即可
* 推荐定时任务 30 10 * * *  ,即每天10.30签到.

### 腾讯视频签到脚本 tx_sign.py
* 腾讯视频好莱坞会员V力值签到，支持两次签到：一次正常签到，一次手机签到。
* 其余四项任务只支持任务完成后,自动领取V力值.
* 电脑打开浏览器访问v.qq.com，打开控制台(F12)、切换到Network，找到 https://access.video.qq.com/user/auth_refresh 的接口，把Request URL:后的地址都复制一下，填写到脚本的auth_refresh_url中，如：
* 复制Request Header中的cookie，填写到脚本的Cookie配置中

### CSDN自动评论脚本 csdn_sign.py
* 可以自动对CSDN热门文章进行评论,提升CSDN等级
* Cookie请通过F12获取
* 个人ID,个人名称均可在CSDN个人中心获取

![image](https://user-images.githubusercontent.com/22621145/122183411-cc7fcb00-cebd-11eb-907f-32043dd611fb.png)
