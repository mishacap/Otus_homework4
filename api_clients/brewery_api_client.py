import requests

class BreweryApiClient:

    def __init__(self,
                 base_url="https://api.openbrewerydb.org/v1"):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url

    def get_list_of_breweries(self):
        response = self.session.get(f"{self.base_url}/breweries")