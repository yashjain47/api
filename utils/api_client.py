import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.header = {
            'Content_Type': 'application/json'
        }


    def get_request(self,endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url,headers=self.header)
        return response


    def post_request(self,endpoint,data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url,headers=self.header,json=data)
        return response


    def put_request(self,endpoint,data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.put(url,headers=self.header,json=data)
        return response


    def delete_request(self,endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.delete(url,headers=self.header)
        return response