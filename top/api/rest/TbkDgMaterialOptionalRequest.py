'''
Created by auto_sdk on 2021.08.09
'''
from top.api.base import RestApi
class TbkDgMaterialOptionalRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.cat = None
		self.city_code = None
		self.device_encrypt = None
		self.device_type = None
		self.device_value = None
		self.end_ka_tk_rate = None
		self.end_price = None
		self.end_tk_rate = None
		self.get_topn_rate = None
		self.has_coupon = None
		self.include_good_rate = None
		self.include_pay_rate_30 = None
		self.include_rfd_rate = None
		self.ip = None
		self.is_overseas = None
		self.is_tmall = None
		self.itemloc = None
		self.latitude = None
		self.lock_rate_end_time = None
		self.lock_rate_start_time = None
		self.longitude = None
		self.material_id = None
		self.need_free_shipment = None
		self.need_prepay = None
		self.npx_level = None
		self.page_no = None
		self.page_result_key = None
		self.page_size = None
		self.platform = None
		self.q = None
		self.relation_id = None
		self.seller_ids = None
		self.sort = None
		self.special_id = None
		self.start_dsr = None
		self.start_ka_tk_rate = None
		self.start_price = None
		self.start_tk_rate = None
		self.ucrowd_id = None
		self.ucrowd_rank_items = None

	def getapiname(self):
		return 'taobao.tbk.dg.material.optional'
