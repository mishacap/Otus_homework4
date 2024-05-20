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
        if response.status_code == 200:
            data = response.json()
            breeds_list = list(data["message"].keys())
            return breeds_list
        else:
            return []

    def get_dog_by_breed(self, breed):
        breeds_list = self.get_all_breeds_list()
        for breed in breeds_list:
            response = self.session.get(url=f"{self.base_url}/breed/{breed}/images")

        return response


