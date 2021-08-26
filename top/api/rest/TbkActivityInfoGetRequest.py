
from top.api.base import RestApi
class TbkActivityInfoGetRequest(RestApi):
    def __init__(self,domain='gw.api.taobao.com',port=80):
        RestApi.__init__(self,domain, port)

        # mm_xxx_xxx_xxx的第三位
        self.adzone_id = None
        # mm_xxx_xxx_xxx 仅三方分成场景使用
        self.sub_pid = None
        # 代理id
        self.relation_id = None
        # 官方活动物料id，由官方运营提供或从官方平台上获取
        self.activity_material_id = None
        # 自定义输入串，英文和数字组成，长度不能大于12个字符，区分不同的推广渠道
        self.union_id = None

    def getapiname(self):
        return 'taobao.tbk.activity.info.get'
