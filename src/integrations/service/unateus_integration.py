import json

from ..facades.unateus import unateus_api


def send_order_to_unateus(request_data: dict):
    data = {
        "number": request_data.get("number"),
        "customerName": request_data.get("customerName"),
        "customerPhone": request_data.get("customerPhone"),
        "city": request_data.get("city"),
        "currency": request_data.get("currency"),
        "districts": request_data.get("districts"),
        "address": request_data.get("address"),
        "deliveryDate": request_data.get("deliveryDate"),
        "comment": request_data.get("comment"),
        "summ": int(request_data.get("summ")),
        "products": [
            {
                "ProductId": int(sub_dict.get('goodID')),
                "qty": int(sub_dict.get('quantity'))} for key, sub_dict in json.loads(request_data.get("products")).items()
        ]
    }

    unateus_api.create_order(data)
