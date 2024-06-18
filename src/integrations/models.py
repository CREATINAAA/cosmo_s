from django.db import models


class Order(models.Model):
    order_id = models.IntegerField(blank=True, unique=True)
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    delivery_date = models.DateTimeField()
    comment = models.TextField()
    summ = models.IntegerField()
    currency = models.CharField(blank=True, null=True)
    districts = models.CharField(blank=True, null=True)


class Product(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, to_field='order_id')
    product_id = models.IntegerField()
    qty = models.IntegerField()


class OrderSpeedaf(models.Model):
    custom_order_no = models.CharField(max_length=255, unique=True)
    customer_code = models.CharField(max_length=255)
    platform_source = models.CharField(max_length=255)
    parcel_type = models.CharField(max_length=255)
    delivery_type = models.CharField(max_length=255)
    transport_type = models.CharField(max_length=255)
    ship_type = models.CharField(max_length=255)
    pay_method = models.CharField(max_length=255)
    accept_name = models.CharField(max_length=255)
    accept_mobile = models.CharField(max_length=255)
    accept_address = models.CharField(max_length=255)
    accept_country_code = models.CharField(max_length=255)
    accept_province_name = models.CharField(max_length=255)
    accept_city_name = models.CharField(max_length=255)
    accept_district_name = models.CharField(max_length=255)
    send_name = models.CharField(max_length=255)
    send_address = models.CharField(max_length=255)
    send_mobile = models.CharField(max_length=255)
    send_country_code = models.CharField(max_length=255)
    send_province_name = models.CharField(max_length=255)
    send_city_name = models.CharField(max_length=255)
    send_district_name = models.CharField(max_length=255)
    parcel_weight = models.DecimalField(max_digits=10, decimal_places=2)
    piece = models.IntegerField()
    goods_qty = models.IntegerField()
    tax_method = models.CharField(max_length=255)
    pick_up_aging = models.IntegerField()


class ProductsSpeedaf(models.Model):
    order = models.ForeignKey(to=OrderSpeedaf, on_delete=models.CASCADE, to_field='custom_order_no')
    sku = models.CharField(max_length=255)
    goods_name = models.CharField(max_length=255)
    goods_name_dialect = models.CharField(max_length=255)
    goods_qty = models.IntegerField()
    goods_value = models.DecimalField(max_digits=10, decimal_places=2)
    goods_type = models.CharField(max_length=255)
    bl_insure = models.IntegerField()
    battery = models.IntegerField()
