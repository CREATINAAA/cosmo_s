from ..service import db
import json
from .speedaf_api import send_order_to_speedaf
from .unateus_integration import send_order_to_unateus
from ..service.validation import OrderValidator, ProductValidator, SpeedafProductValidator, SpeedafOrderValidator
from ..api.serializers import OrderSerializer, ProductSerializer, SpeedafOrderSerializer, SpeedafProductSerializer


def webhook_handler(request_data: dict, warehouse: str):
    if warehouse == "unateus":
        validated_order = get_validated_order(request_data)
        validated_order_products = get_validated_order_products(request_data)
        db.save_order(validated_order, validated_order_products, OrderSerializer, ProductSerializer)
        send_order_to_unateus(request_data)
    else:
        validated_order = get_validated_order_speedaf(request_data)
        validated_order_products = get_validated_order_products_speedaf(request_data)
        db.save_order(validated_order, validated_order_products, SpeedafOrderSerializer, SpeedafProductSerializer)
        send_order_to_speedaf(request_data)


def get_validated_order(request_data: dict, ):
    request_data['number'] = int(request_data['number'])
    validated_deal = dict(OrderValidator.model_validate(request_data))
    return validated_deal


def get_validated_order_products(request_data: dict):
    products = [item for item in json.loads(request_data.get("products")).values()]
    return products

def get_validated_order_speedaf(request_data: dict):
    validated_order = SpeedafOrderValidator.model_validate(request_data)
    return validated_order

def get_validated_order_products_speedaf(request_data: dict):
    pass
    