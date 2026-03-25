import requests


class Moldea:
    def __init__(self, base_url: str = "https://httpbin.org") -> None:
        self.base_url = base_url.rstrip("/")

    def get(self) -> dict:
        response = requests.get(f"{self.base_url}/get", timeout=10)
        response.raise_for_status()
        return response.json()