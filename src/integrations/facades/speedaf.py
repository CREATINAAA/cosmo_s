import base64
import hashlib
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from time import time
import requests
import json


class SpeedafAPI:
    def __init__(self, app_code, secret_key) -> None: 
        self.app_code = app_code
        self.secret_key = secret_key
        self.BASE_URL = 'https://apis.speedaf.com/open-api/express/'
    
    def post(self, data, end_point):
            # Функция для получения текущего времени в миллисекундах
        def get_current_timestamp():
            return str(int(time() * 1000))

        # Функция для создания MD5 подписи
        def create_md5_signature(timestamp, secret_key, data):
            signature_str = timestamp + secret_key + data
            return hashlib.md5(signature_str.encode('utf-8')).hexdigest()

        # Функция для шифрования данных
        def des_encrypt(data, secret_key):
            des_iv = bytes([0x12, 0x34, 0x56, 0x78, 0x90, 0xAB, 0xCD, 0xEF])
            cipher = DES.new(secret_key.encode('utf-8'), DES.MODE_CBC, des_iv)
            padded_data = pad(data.encode('utf-8'), DES.block_size)
            encrypted_data = cipher.encrypt(padded_data)
            return base64.b64encode(encrypted_data).decode('utf-8')

        # Функция для дешифрования данных
        def des_decrypt(encrypted_data, secret_key):
            des_iv = bytes([0x12, 0x34, 0x56, 0x78, 0x90, 0xAB, 0xCD, 0xEF])
            cipher = DES.new(secret_key.encode('utf-8'), DES.MODE_CBC, des_iv)
            decoded_encrypted_data = base64.b64decode(encrypted_data)
            decrypted_data = unpad(cipher.decrypt(decoded_encrypted_data), DES.block_size)
            return decrypted_data.decode('utf-8')
        data = json.dumps(data)
        timestamp = get_current_timestamp()
        signature = create_md5_signature(timestamp, self.secret_key, data)

        # Подготовка тела запроса
        body = json.dumps({
            "data": data,
            "sign": signature
        })

        # Шифрование тела запроса
        encrypted_body = des_encrypt(body, self.secret_key)

        # Формирование окончательного URL с параметрами
        final_url = f'{self.BASE_URL}{end_point}?timestamp={timestamp}&appCode={self.app_code}'

        # Отправка POST запроса
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(final_url, headers=headers, data=encrypted_body)

        # Обработка ответа
        if response.status_code == 200:
            response_data = response.json()
            if response_data['success']:
                decrypted_data = des_decrypt(response_data['data'], self.secret_key)
                print('Расшифрованный ответ:', decrypted_data)
            else:
                print('Ошибка в ответе:', response_data['error']['message'])
        else:
            print('Ошибка запроса:', response.status_code, response.text)

speedaf_api = SpeedafAPI("NG000674", "rIEpSjxc")
