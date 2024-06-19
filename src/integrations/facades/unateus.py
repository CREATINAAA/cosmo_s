import requests

from config import settings


class UnateusApi:
    BASE_URL = "https://api.unateus.com/api/v1/"

    def __init__(self, api_key: str):
        self.params = {
            "apiKey": api_key,
        }

    def create_order(self, data: dict):
        return requests.post(self.BASE_URL + "createOrder", params=self.params, json=data)

    def update_order(self, data: dict):
        return requests.post(self.BASE_URL + "updateOrder", params=self.params, json=data)

    def get_list_orders(self, data: dict):
        return requests.post(self.BASE_URL + "listOrders", params=self.params, json=data)

    def get_products(self):
        return requests.get(self.BASE_URL + "products", params=self.params)


unateus_api = UnateusApi(api_key=settings.API_KEY_UNATEUS)