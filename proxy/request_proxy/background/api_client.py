import requests

class ApiClient:

    ENDPOINTS = {
        "apiGetConfig": "/api/config/get",
        "apiPostReport": "/api/intercept/report",
    }

    def __init__(self, url):
        self.url = url

    def get_config(self):
        return requests.get(self.url + self.ENDPOINTS["apiGetConfig"]).json()["data"]

    def post_report(self, report: dict):
        return requests.post(self.url + self.ENDPOINTS["apiPostReport"], json=report, headers={"Content-Type": "application/json"})
