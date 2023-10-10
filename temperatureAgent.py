from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
from datetime import datetime
import json
import requests

URL = "https://api.open-meteo.com/v1/forecast?"
# no API key needed
MY_DATA = {"latitude": 12.800962392747023, "longitude": 80.22415148590215, "hour": 12} #To be adjusted as per website data

#Requesting for data in a specified format.
class RequestWeather(Model):
    latitude: float
    longitude: float
    hour: int

#returning the result in `Weather` format.
class Weather(Model):
    hour: int
    degrees: float
    text: str

#Weather API call to get data specific to the user need
def get_data(ctx, latitude, longitude) -> dict or None:
    """
    Function to get the data from the open meteo API

    :param ctx: Context
    :param latitude: float
    :param longitude: float
    :return: dict of weather data or None
    """
    url = (
        URL
        + f"latitude={latitude}&longitude={longitude}"
        + "&hourly=temperature_2m&forecast_days=1"
    )
    current_date = datetime.utcnow().date().isoformat()
    cached_data = ctx.storage.get("last_request")
    if cached_data:
        data = json.loads(cached_data)
        if data["date"] == current_date and data["url"] == url:
            return data["response"]

    response = requests.get(url=url, timeout=5)
    if response.status_code == 200:
        data = response.json()
        ctx.storage.set("last_request",
            json.dumps({"date": current_date, "url": url, "response": data})
        )
        return data
    return None


temperatureAgent = Agent(name="temperatureAgent", 
                         seed="temperatureAgent secret seed phrase",
                         port=8002,
                         endpoint=["http://127.0.0.1:8002/submit"]
                         )

fund_agent_if_low(temperatureAgent.wallet.address())
min = 28
print(temperatureAgent.address)
#Temperature Check logic




#Agent activities:
@temperatureAgent.on_event("startup")
async def intoduce(ctx: Context):
    ctx.logger.info("Collecting Data for temperature")

@temperatureAgent.on_message(model=RequestWeather, replies=Weather)
async def handle_request(ctx: Context, sender: str, msg: RequestWeather):
    """This function handles the request from other agents"""
    data = get_data(ctx, msg.latitude, msg.longitude)
    if data:
        temp = data["hourly"]["temperature_2m"][msg.hour]
        ctx.logger.info(f"Sending weather data to {sender[-10:]}...")
        await ctx.send(
            sender,
            Weather(
                hour=msg.hour,
                degrees=temp,
                text=f"Your local temperature at {msg.hour} is {temp}°C.",
            ),
        )
    else:
        ctx.logger.info("Couldn't get data")
        await ctx.send(sender, Weather(hour=msg.hour, degrees=0, text="Couldn't get data"))


if __name__ == "__main__":
    temperatureAgent.run()