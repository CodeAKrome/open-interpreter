from security import safe_requests


class Browser:
    def __init__(self, computer):
        self.computer = computer

    def search(self, query):
        response = safe_requests.get(f'{self.computer.api_base.strip("/")}/browser/search', params={"q": query}
        )
        return response.json()["result"]
