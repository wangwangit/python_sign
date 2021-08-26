
from top.api.base import RestApi
class TbkOrderDetailsGetRequest(RestApi):
    def __init__(self,domain='gw.api.taobao.com',port=80):
        RestApi.__init__(self,domain, port)
        # 查询时间类型，1：按照订单淘客创建时间查询，2:按照订单淘客付款时间查询，3:按照订单淘客结算时间查询
        self.query_type = None
        # 位点，除第一页之外，都需要传递；前端原样返回。
        self.position_index = None
        # 页大小，默认20，1~100
        self.page_size = None
        # 推广者角色类型,2:二方，3:三方，不传，表示所有角色
        self.member_type = None
        # 淘客订单状态，12-付款，13-关闭，14-确认收货，3-结算成功;不传，表示所有状态
        self.tk_status = None
        # 订单查询结束时间，订单开始时间至订单结束时间，中间时间段日常要求不超过3个小时，
        # 但如618、双11、年货节等大促期间预估时间段不可超过20分钟，超过会提示错误，调用时请务必注意时间段的选择，以保证亲能正常调用！
        self.end_time = None
        # 订单查询开始时间
        self.start_time = None
        # 跳转类型，当向前或者向后翻页必须提供,-1: 向前翻页,1：向后翻页
        self.jump_type = None
        # 第几页，默认1，1~100
        self.page_no = None
        # 场景订单场景类型，1:常规订单，2:渠道订单，3:会员运营订单，默认为1
        self.order_scence = None

    def getapiname(self):
        return 'taobao.tbk.order.details.get'