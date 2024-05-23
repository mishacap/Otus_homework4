import requests

class BreweryApiClient:
    def __init__(self,
                 base_url="https://api.openbrewerydb.org/v1/breweries"):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url

    def get_list_of_breweries(self):
        response = self.session.get(url=f"{self.base_url}")
        return response

    def get_all_breweries_list(self):
        response = self.session.get(f"{self.base_url}")
        json_response = response.json()
        if response.status_code == 200:
            all_breweries_ids = [brewery["id"] for brewery in json_response]
            return list(all_breweries_ids)
        else:
            return []

    def get_single_brewery_by_id(self, query):
        response = self.session.get(url=f"{self.base_url}/{query}")
