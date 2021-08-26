'''
Created by auto_sdk on 2016.05.24
'''
from top.api.base import RestApi
class AlibabaAliqinFcSmsNumSendRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.extend = None
		self.rec_num = None
		self.sms_free_sign_name = None
		self.sms_param = None
		self.sms_template_code = None
		self.sms_type = None

	def getapiname(self):
		return 'alibaba.aliqin.fc.sms.num.send'
