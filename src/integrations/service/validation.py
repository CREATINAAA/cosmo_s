from pydantic import BaseModel, Field, AliasPath


class OrderValidator(BaseModel):
    order_id: int = Field(validation_alias=AliasPath("number"), default="")
    customer_name: str = Field(validation_alias=AliasPath("customerName"), default="")
    customer_phone: str = Field(validation_alias=AliasPath("customerPhone"), default="")
    city: str = Field(validation_alias=AliasPath("city"), default="")
    address: str = Field(validation_alias=AliasPath("address"), default="")
    delivery_date: str = Field(validation_alias=AliasPath("deliveryDate"), default="")
    comment: str = Field(validation_alias=AliasPath("comment"), default="")
    summ: int = Field(validation_alias=AliasPath("summ"), default=0)
    currency: str = Field(validation_alias=AliasPath("currency"), default="")
    districts: str = Field(validation_alias=AliasPath("districts"), default="")


class ProductValidator(BaseModel):
    product_id: int = Field(validation_alias=AliasPath("goodID"), default=0)
    qty: int = Field(validation_alias=AliasPath("quantity"), default=0)


class SpeedafOrderValidator(BaseModel):
    custom_order_no: str = Field(validation_alias=AliasPath("number"), default="")
    # platform_source: str = 
    # parcel_type
    # delivery_type
    # transport_type
    # ship_type
    # pay_method
    # accept_name
    # accept_mobile
    # accept_address
    # accept_country_code
    # accept_province_name
    # accept_city_name
    # accept_district_name
    # send_name
    # send_address
    # send_mobile
    # send_country_code
    # send_province_name
    # send_city_name
    # send_district_name
    # parcel_weight
    # piece
    # goods_qty
    # tax_method
    # pick_up_aging


class SpeedafProductValidator(BaseModel):
    goods_name: str = Field(validation_alias=AliasPath("name"), default="")
    goods_qty: str = Field(validation_alias=AliasPath("quantity"), default="")
    goods_value: float = Field(validation_alias=AliasPath("price"), default="")
    bl_insure: int = Field(validation_alias=AliasPath("price"), default="")
