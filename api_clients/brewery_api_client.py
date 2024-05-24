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
        response = self.session.get(url=f"{self.base_url}")
        json_response = response.json()
        if response.status_code == 200:
            all_breweries_ids = [brewery["id"] for brewery in json_response]
            return all_breweries_ids
        else:
            return []


    def get_single_brewery_by_id(self, query):
        response = self.session.get(url=f"{self.base_url}/{query}")
        if response.status_code == 200:
            return response
        else:
            return None


    def get_all_cities_list(self):
        response = self.session.get(url=f"{self.base_url}")
        json_response = response.json()
        if response.status_code == 200:
            all_cities_list = list(set([city["city"] for city in json_response]))
            return all_cities_list
        else:
            return []


    def get_breweries_by_city(self, query):
        response = self.session.get(url=f"{self.base_url}?by_city={query}")
        if response.status_code == 200:
            return response
        else:
            return None


    def get_all_breweries_types_list(self):
        response = self.session.get(url=f"{self.base_url}")
        if response.status_code == 200:
            json_response = response.json()
            all_breweries_types = list(set([brewery["brewery_type"] for brewery in json_response]))
            return all_breweries_types
        else:
            return []

    def get_breweries_by_type(self, query):
        response = self.session.get(url=f"{self.base_url}?by_type={query}")
        if response.status_code == 200:
            return response
        else:
            return None


    def get_brewery_random(self):
        response = self.session.get(url=f"{self.base_url}/random")
        if response.status_code == 200:
            return response
        else:
            return None

