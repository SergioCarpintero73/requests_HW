import requests

yndex_token = 'AQAEA7qjXWpTAADLW7j6Fbv3bkKll-KdxRkF5dc'

class YaDiskUploader:
    def __init__(self, token: str):
        self.token = token

    def get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params).json()
        return response

    def upload_file(self, file_path, file_name):
        href = self.get_upload_link(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Всё прошло успешно')


if __name__ == '__main__':
    uploader = YaDiskUploader(token=yndex_token)
    uploader.upload_file('Study/Test File.txt', 'Test File.txt')