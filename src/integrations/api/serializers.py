from rest_framework import serializers

from ..models import Order, Product, OrderSpeedaf, ProductsSpeedaf


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class SpeedafOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderSpeedaf
        fields = '__all__'


class SpeedafProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsSpeedaf
        fields = '__all__'
