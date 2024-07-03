import requests


class DogApiClient:

    def __init__(self,
                 base_url="https://dog.ceo/api"):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url

    def get_random_dog(self):
        response = self.session.get(url=f"{self.base_url}/breeds/image/random")

        return response

    def get_all_breeds(self):
        response = self.session.get(url=f"{self.base_url}/breeds/list/all")

        return response

    def get_all_breeds_list(self):
        response = self.session.get(url=f"{self.base_url}/breeds/list/all")
        json_response = response.json()
        if response.status_code == 200 and json_response["status"] == "success":
            breeds = json_response["message"].keys()
            return list(breeds)
        else:
            return []

    def get_dog_by_breed(self, query):
        response = self.session.get(url=f"{self.base_url}/breed/{query}/images")
        return response

    def get_all_sub_breeds(self, query):
        response = self.session.get(url=f"{self.base_url}/breed/{query}/list")
        return response

    def get_random_dog_by_breed(self, query):
        response = self.session.get(url=f"{self.base_url}/breed/{query}/images/random")
        return response
