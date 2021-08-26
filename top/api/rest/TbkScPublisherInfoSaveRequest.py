

from top.api.base import RestApi
class TbkScPublisherInfoSaveRequest(RestApi):
    def __init__(self,domain='gw.api.taobao.com',port=80):
        RestApi.__init__(self,domain, port)

        # 渠道备案 - 来源，取链接的来源
        self.relation_from = None

        # 渠道备案 - 线下场景信息，1 - 门店，2- 学校，3 - 工厂，4 - 其他
        self.offline_scene = None
        # 渠道备案 - 线上场景信息，1 - 微信群，2- QQ群，3 - 其他
        self.online_scene = None
        # 淘宝客邀请渠道或会员的邀请码
        self.inviter_code = None
        # 类型，必选 默认为1:
        self.info_type = 1
        # 媒体侧渠道备注
        self.note = None
        # 线下备案注册信息,字段包含: 电话号码(phoneNumber，必填),省(province,必填),市(city,必填),区县街道(location,必填),
        # 详细地址(detailAddress,必填),经营类型(career,线下个人必填),店铺类型(shopType,线下店铺必填),店铺名称(shopName,线下店铺必填),
        # 店铺证书类型(shopCertifyType,线下店铺选填),店铺证书编号(certifyNumber,线下店铺选填)
        self.register_info = None

    def getapiname(self):
        return 'taobao.tbk.sc.publisher.info.save'