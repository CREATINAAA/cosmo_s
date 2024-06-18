from ..service import db
import json
from ..service.unateus_integration import unateus_api
from ..service.validation import OrderValidator, ProductValidator


def webhook_handler(request_data: dict):
    validated_order = get_validated_order(request_data)
    validated_order_products = get_validated_order_products(request_data)
    db.save_order(validated_order, validated_order_products)
    send_order_to_unateus(request_data)


def get_validated_order(request_data: dict):
    request_data['number'] = int(request_data['number'])
    validated_deal = dict(OrderValidator.model_validate(request_data))
    return validated_deal


def get_validated_order_products(request_data: dict):
    products = [item for item in json.loads(request_data.get("products")).values()]
    return products


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
