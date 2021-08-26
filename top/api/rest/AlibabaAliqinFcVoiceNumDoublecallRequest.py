'''
Created by auto_sdk on 2016.03.06
'''
from top.api.base import RestApi
class AlibabaAliqinFcVoiceNumDoublecallRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.called_num = None
		self.called_show_num = None
		self.caller_num = None
		self.caller_show_num = None
		self.extend = None
		self.session_time_out = None

	def getapiname(self):
		return 'alibaba.aliqin.fc.voice.num.doublecall'
