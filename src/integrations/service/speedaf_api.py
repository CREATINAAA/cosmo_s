from ..facades.speedaf import speedaf_api


def get_request_body_for_create_order(data):
    return"""
    {
        "customerCode": ""
        "platformSource": ""
        "parcelType": ""
        "deliveryType": ""
        "transportType": ""
        "shipType": ""
        "payMethod": ""
        "acceptName": ""
        "acceptMobile": ""
        "acceptAddress": ""
        "acceptCountryCode": ""
        "acceptProvinceName": ""
        "acceptCityName": ""
        "acceptDistrictName": ""
        "sendName": ""
        "sendAddress": ""
        "sendMobile": ""
        "sendCountryCode": ""
        "sendProvinceName": ""
        "sendCityName": ""
        "sendDistrictName": ""
        "parcelWeight": ""
        "piece": ""
        "goodsQTY": ""
        "taxMethod": ""
        "pickUpAging": ""

        "itemList": [

            {
                "sku": ""
                "goodsName": ""
                "goodsNameDialect": ""
                "goodsQTY": ""
                "goodsValue": ""
                "goodsType": ""
                "blInsure": ""
                "battery": ""

            }

        ],
    }
    """
def send_order_to_speedaf(request):
    speedaf_api.post(get_request_body_for_create_order(request), "order/createOrder")

