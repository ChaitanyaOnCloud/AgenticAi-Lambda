import os
import requests
import string

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

class WeatherTool:
    def get_weather(self, city="Mumbai"):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url).json()
        if response.get("main"):
            return f"Weather in {city}: {response['main']['temp']}°C, {response['weather'][0]['description']}"
        return f"Weather info not available for {city}."

class CryptoTool:
    def get_crypto_price(self, coin="bitcoin"):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        response = requests.get(url).json()
        if coin in response:
            return f"{coin.capitalize()} price: ${response[coin]['usd']}"
        return f"Crypto info not available for {coin}."


def lambda_handler(event, context):
    query = event.get("query", "").lower()
    if not query:
        return {"result": "No query provided."}

    # Determine intent
    if "weather" in query:
        intent = "weather"
    elif "bitcoin" in query or "crypto" in query or "ethereum" in query:
        intent = "crypto"
    else:
        intent = "unknown"

    # Tools
    weather_tool = WeatherTool()
    crypto_tool = CryptoTool()

    if intent == "weather":
        # city extraction after 'in'
        words = query.translate(str.maketrans('', '', string.punctuation)).split()
        city = "Mumbai"
        if "in" in [w.lower() for w in words]:
            idx = [w.lower() for w in words].index("in")
            city_words = words[idx+1:]
            if city_words:
                city = " ".join(city_words)
        result = weather_tool.get_weather(city)

    elif intent == "crypto":
        coin = "bitcoin"
        words = query.translate(str.maketrans('', '', string.punctuation)).split()
        for w in words:
            if w.lower() in ["bitcoin", "crypto", "ethereum"]:
                coin = w.lower()
                break
        result = crypto_tool.get_crypto_price(coin)

    else:
        result = "Sorry, I don't understand the query."

    return {"result": result}

