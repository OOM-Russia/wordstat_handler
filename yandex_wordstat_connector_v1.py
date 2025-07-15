import requests
from dotenv import dotenv_values
from typing import Optional, List, Dict, Any


class YandexWordstatConnector:
    BASE_URL = "https://api.wordstat.yandex.net"

    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "Content-Type": "application/json;charset=utf-8",
            "Authorization": f"Bearer {self.token}",
        }

    def get_top_requests(
        self,
        phrase: str,
        regions: Optional[List[int]] = None,
        devices: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/v1/topRequests"
        payload = {"phrase": phrase}

        if regions:
            payload["regions"] = regions
        if devices:
            payload["devices"] = devices

        response = requests.post(url, headers=self.headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"ошибка при получении топов: {response.status_code} {response.text}"
            )

    def get_dynamics(
        self,
        phrase: str,
        period: str,
        from_date: str,
        to_date: Optional[str] = None,
        regions: Optional[List[int]] = None,
        devices: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/v1/dynamics"
        payload = {"phrase": phrase, "period": period, "fromDate": from_date}

        if to_date:
            payload["toDate"] = to_date
        if regions:
            payload["regions"] = regions
        if devices:
            payload["devices"] = devices

        response = requests.post(url, headers=self.headers, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"ошибка при получении динамики: {response.status_code} {response.text}"
            )


if __name__ == "__main__":
    config = dotenv_values(".env")
    TOKEN = config["YANDEX_WORDSTAT_TOKEN"]

    client = YandexWordstatConnector(TOKEN)

    # тест запроса топа
    top_data = client.get_top_requests(
        phrase="купить телефон", regions=[3333], devices=["desktop"]  # Москва
    )
    print("Топы:", top_data)

    # тест запроса динамики
    dyn_data = client.get_dynamics(
        phrase="купить телефон",
        period="monthly",
        from_date="2025-05-01",
        to_date="2025-06-30",
        regions=[213],
        devices=["all"],
    )
    print("Динамика:", dyn_data)

    pass
