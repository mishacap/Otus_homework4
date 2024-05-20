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
