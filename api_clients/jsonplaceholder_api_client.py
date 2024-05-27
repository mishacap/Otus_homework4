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


    def create_post(self, data):
        response = self.session.post(url=f"{self.base_url}/posts",
                                     json=data)
        return response

    def update_post(self, data, query):
        response = self.session.put(url=f"{self.base_url}/posts/{query}",
                                     json=data)
        return response

    def get_all_users_ids(self):
        response = self.session.get(url=f"{self.base_url}/posts")
        json_response = response.json()
        if response.status_code == 200:
            all_users_ids = {post["userId"] for post in json_response}
            return all_users_ids
        else:
            return []

    def get_all_post_by_user(self, query):
        response = self.session.get(url=f"{self.base_url}/posts?userId={query}")
        return response








