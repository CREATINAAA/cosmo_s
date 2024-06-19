from ..api.serializers import OrderSerializer, ProductSerializer, SpeedafOrderSerializer, SpeedafProductSerializer


def save_order(validated_order, validated_products_items, order_model, product_model):
    serializer = order_model(data=validated_order)
    print(serializer)
    if not serializer.is_valid():
        return -1
    serializer.save()
    order_id = int(serializer.data.get('order_id'))
    for product in validated_products_items:
        data = product
        data['order'] = order_id
        for key, value in data.items():
            if key != 'name':
                data[key] = int(value)
        new_data = {'product_id': data['goodID'], 'qty': data['quantity'], 'order': int(data['order'])}
        serializers_product = product_model(data=new_data)
        if not serializers_product.is_valid():
            return -1
        serializers_product.save()
    return order_id


# def save_speedaf_order(validated_order, validated_products_items):
#     serializer = SpeedafOrderSerializer(data=validated_order)
#     print(serializer)
#     if not serializer.is_valid():
#         return -1
#     serializer.save()
#     order_id = int(serializer.data.get('order_id'))
#     for product in validated_products_items:
#         data = product
#         data['order'] = order_id
#         for key, value in data.items():
#             if key != 'name':
#                 data[key] = int(value)
#         new_data = {'product_id': data['goodID'], 'qty': data['quantity'], 'order': int(data['order'])}
#         serializers_product = SpeedafProductSerializer(data=new_data)
#         if not serializers_product.is_valid():
#             return -1
#         serializers_product.save()
#     return order_id
