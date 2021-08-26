'''
Created by auto_sdk on 2016.05.24
'''
from top.api.base import RestApi
class AlibabaAliqinFcTtsNumSinglecallRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.called_num = None
		self.called_show_num = None
		self.extend = None
		self.tts_code = None
		self.tts_param = None

	def getapiname(self):
		return 'alibaba.aliqin.fc.tts.num.singlecall'
