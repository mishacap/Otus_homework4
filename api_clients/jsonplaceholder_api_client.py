import requests


class JsonplaceholderApiClient:
    def __init__(self,
                 base_url="https://jsonplaceholder.typicode.com"):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url


    def get_all_posts(self):
        response = self.session.get(url=f"{self.base_url}/posts")
        return response



    def get_all_posts_ids(self):
        response = self.session.get(url=f"{self.base_url}/posts")
        json_response = response.json()
        if response.status_code == 200:
            all_posts_ids = [id_ ["id"] for id_ in json_response]
            return all_posts_ids
        else:
            return []


    def get_post_by_id(self, query):
        response = self.session.get(url=f"{self.base_url}/posts/{query}")
        return response




