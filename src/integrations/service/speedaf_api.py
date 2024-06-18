from ..facades.speedaf import speedaf_api

def create_order(data):
    speedaf_api.post(data, "order/createOrder")

create_order({

    "acceptAddress": "",

    "acceptCitizenId": "78456478965",

    "acceptCityCode": "",

    "acceptCityName": "",

    "acceptCompanyName": "",

    "acceptCountryCode": "NG",

    "acceptCountryName": "Nigiera",

    "acceptDistrictCode": "",

    "acceptDistrictName": "",

    "acceptEmail": "123@Test.com",

    "acceptMobile": "17789222226",

    "acceptName": "",

    "acceptPhone": "999999",

    "acceptPostCode": "",

    "acceptProvinceCode": "",

    "acceptProvinceName": "",

    "acceptStreetName ": "",

    "codFee": 100,

    "currencyType": "NGN",

    "customOrderNo": "",

    "customerCode": "",

    "changeLable": 0,

    "deliveryType": "DE01",

    "goodsQTY": 1,

    "goodsWeight": 0,

    "insurePrice": 0,

    "isAllowOpen": 0,

    "itemList": [

        {

            "battery": 0,

            "blInsure": 0,

            "currencyType": "NGN",

            "dutyMoney": 0,

            "goodsHigh": 0,

            "goodsLength": 100,

            "goodsMaterial": "",

            "goodsName": "English goodsName",

            "goodsNameDialect": "",

            "goodsQTY": 2,

            "goodsRemark": "",

            "goodsRule": "",

            "goodsType": "IT02",

            "goodsUnitPrice": 100,

            "goodsValue": 100,

            "goodsVolume": 1.52,

            "goodsWeight": 100,

            "goodsWidth": 100,

            "hsCode": "",

            "makeCountry": "CN",

            "salePath": "",

            "sku": "sku001",

            "unit": "box"

        }

    ],

    "packetCenterCode": "",

    "parcelCurrencyType": "NGN",

    "parcelHigh": 100,

    "parcelLength": 100,

    "parcelType": "PT01",

    "parcelVolume": 1.52,

    "parcelWeight": 100,

    "parcelWidth": 100,

    "parcelValue": 10,

    "payMethod": "PA01",

    "pickupBatch": "",

    "pickUpAging": 0,

    "pickupCity": "",

    "pickupCountry": "",

    "pickupDetailAddress": "",

    "pickupDistrict": "",

    "pickupName": "",

    "pickupPhone": "",

    "pickupProvince": "",

    "pickupType": 0,

    "piece": 1,

    "platformSource": "csp",

    "prePickUpTime": "2022-04-12 10:00:00",

    "productService": "",

    "remark": "",

    "sendAddress": "",

    "sendCityCode": "",

    "sendCityName": "",

    "sendCompanyName": "",

    "sendCountryCode": "CN",

    "sendCountryName": "China",

    "sendDistrictCode": "",

    "sendDistrictName": "",

    "sendMail": "",

    "sendMobile": "",

    "sendName": "",

    "sendPhone": "",

    "sendPostCode": "",

    "sendProvinceCode": "",

    "sendProvinceName": "",

    "shipType": "ST01",

    "shippingFee": 0,

    "smallCode": "",

    "threeSectionsCode": "",

    "transportType": "TT02",

    "taxMethod": "DDP",

    "warehouseCode": "GZ01"

})
