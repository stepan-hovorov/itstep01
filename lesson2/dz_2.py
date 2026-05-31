import requests


class CurrencyConverter:
    def __init__(self):
        self.usd_rate = self.get_usd_rate()

    def get_usd_rate(self):
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

        response = requests.get(url)
        data = response.json()

        for currency in data:
            if currency["cc"] == "USD":
                return currency["rate"]

        return None

    def uah_to_usd(self, amount_uah):
        return amount_uah / self.usd_rate


converter = CurrencyConverter()

print(f"Поточний курс USD: {converter.usd_rate} грн")

amount = float(input("Введіть суму в гривнях: "))

usd = converter.uah_to_usd(amount)

print(f"{amount} грн = {usd:.2f} USD")