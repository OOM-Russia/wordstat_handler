import requests
from dotenv import dotenv_values
from typing import Optional, List, Dict, Any
import time


class YandexWordstatConnector:
    def __init__(self, token: str):
        self.base_url = "https://api.wordstat.yandex.net"
        self.token = token
        self.headers = {
            "Content-Type": "application/json;charset=utf-8",
            "Authorization": f"Bearer {self.token}",
        }

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:

        # реализовать метод _make_request и затем использовать его в get_regions, get_top_requests и get_dynamics

        pass

    def get_regions(self) -> List[int]:
        pass

    def get_top_requests(
        self,
        phrase: str,
        regions: Optional[List[int]] = None,
        devices: Optional[List[str]] = None,
    ) -> Dict[str, Any]:

        pass

    def get_dynamics(
        self,
        phrase: str,
        period: str,
        from_date: str,
        to_date: Optional[str] = None,
        regions: Optional[List[int]] = None,
        devices: Optional[List[str]] = None,
    ) -> Dict[str, Any]:

        pass

    def get_dynamics_batch(
        self,
        phrases: List[str],
        period: str,
        from_date: str,
        to_date: Optional[str] = None,
        regions: Optional[List[int]] = None,
        devices: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        pass


if __name__ == "__main__":
    config = dotenv_values(".env")
    TOKEN = config["YANDEX_WORDSTAT_TOKEN"]
    client = YandexWordstatConnector(token=TOKEN)

    pass
