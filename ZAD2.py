import requests
import json


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, url, file_path):
        for i in file_path:
            params = {"path": i}
            headers = {"Authorization": "OAuth " + self.token}
            responce = requests.get(url, headers=headers, params=params)
            if 200 <= responce.status_code < 300:
                print('Text: ', responce.text)
                print('Json: ', responce.json)
                data = responce.json()
                message = data["href"]
            with open(i, "rb") as x:
                requests.post(message, files={"file": x})
                print(responce.status_code)


path_to_file = "https://cloud-api.yandex.net/v1/disk/resources/upload"

tok = # токен яндекс диска

with open('names.txt', 'r', encoding='UTF-8') as file:
    f = file.read().splitlines()



uploader = YaUploader(tok)
result = uploader.upload(path_to_file, f)
