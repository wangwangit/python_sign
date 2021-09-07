import configparser
import re
from decimal import Decimal
from top import appinfo
from top.api.rest.TbkCouponGetRequest import TbkCouponGetRequest
from top.api.rest.TbkDgMaterialOptionalRequest import TbkDgMaterialOptionalRequest
from top.api.rest.TbkTpwdCreateRequest import TbkTpwdCreateRequest


# 查找商品详细信息
def TbkDgMaterialOptional(title):
    req = TbkDgMaterialOptionalRequest()
    req.set_app_info(appinfo(app_key, app_password))
    req.adzone_id = app_id
    req.platform = 2
    req.q = title
    try:
        resp = req.getResponse()
        return resp
    except Exception as e:
        print(e)


# 查找商品的有无淘宝客对应的优惠券
def TbkCouponGet(item_id, activity_id):
    req = TbkCouponGetRequest()
    req.set_app_info(appinfo(app_key, app_password))
    req.item_id = int(item_id)
    req.activity_id = str(activity_id)
    try:
        resp = req.getResponse()
        return resp
    except Exception as e:
        print(e)


# 有淘宝客对应优惠券的商品生成短链接
def TbkTpwdCreate(title, url):
    req = TbkTpwdCreateRequest()
    req.set_app_info(appinfo(app_key, app_password))
    req.text = title
    req.url = url
    try:
        resp = req.getResponse()
        return resp
    except Exception as e:
        print(e)


def getTb(sp):
    # 给出要查询的商品名字
    response = TbkDgMaterialOptional(sp)
    map_data = response['tbk_dg_material_optional_response']['result_list']['map_data'][0]
    if map_data.get('coupon_share_url') is None:
        return '没有发现优惠券'
    else:
        # 得到商品的名称
        title = map_data.get('title')
        # 得到商品的id
        itemid = map_data.get('item_id')
        # 得到优惠券的id
        activityid = map_data.get('coupon_id')
        share_url = "https:" + map_data.get('coupon_share_url')

        priceresponse = TbkCouponGet(itemid, activityid)
        price = priceresponse['tbk_coupon_get_response']['data']
        # 商品的优惠券额度
        discount = price.get('coupon_amount')
        # 商品的原始价格
        onsale = price.get('coupon_start_fee')
        # 优惠后的价格
        difference = str(float(Decimal(onsale) - Decimal(discount)))

        Shortlink = TbkTpwdCreate(title, share_url)
        # 得到短链接
        link = Shortlink['tbk_tpwd_create_response']['data']['model']
        linkterm = re.compile(r'(.*?)【.*')
        truelink = re.findall(linkterm, link)
        message = title + "\n【在售价】" + onsale + "\n【券后价】" + difference + "\n" + link
        return message


if __name__ == '__main__':

    while True:
        config = configparser.ConfigParser()
        config.read("config.ini")
        app_id = config.get('TB', 'app_id')
        app_key = config.get('TB', 'app_key')
        app_password = config.get('TB', 'app_password')
        content = input("请输入商品名称：")
        print(getTb(content) + '\n')
