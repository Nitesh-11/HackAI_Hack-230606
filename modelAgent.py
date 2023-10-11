from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
# from typing_extensions import NDArray
import warnings
import pickle 
import numpy as np
import json
from datetime import datetime, timedelta
import requests

# #loading weight files
with warnings.catch_warnings():
  warnings.filterwarnings("ignore", category=UserWarning)
  model = pickle.load(open("model4.pkl", "rb"))


URL = "https://api.open-meteo.com/v1/forecast?"
# input = np.array([['0700', 26.52, 71.6, 2.97, 89554]], dtype=object)
# print(input)
# pred = model.predict(input)
# print(f"{pred} is the prediction")


#encapsulation of input
class data(Model):
   values:list

class preds(Model):
   values:str
   text:str

class Weather(Model):
    hour: int
    degrees: float
    text: str

# #getter for data
# def get_data(inputs: data):
#    inputs = np.array(inputs, dtype=object)
#    return inputs


def get_data(ctx, latitude=22.351, longitude=78.668) -> dict or None:
    """
    Function to get the data from the open meteo API

    :param ctx: Context
    :param latitude: float
    :param longitude: float
    :return: dict of weather data or None
    """
    url = "https://api.open-meteo.com/v1/forecast?latitude=12.800962392747023&longitude=80.22415148590215&current=temperature_2m,relativehumidity_2m,surface_pressure,windspeed_10m&start_date=2023-10-11&end_date=2023-10-11"
   #  url = (
   #      URL
   #      + f"latitude={latitude}&longitude={longitude}"+"&start={start}&end={end}" + "&current=temperature_2m,relativehumidity_2m,surface_pressure,windspeed_10m"
   #      + "&start_date={start}&end_date={start}"
        
   #  )

# Use the datetime.now() function to get the current date and time as a datetime object
    dt = datetime.now()
    hour_data = dt.strftime('%H')+'00'

    current_date = datetime.utcnow().date().isoformat()
    cached_data = ctx.storage.get("last_request")
   #  if cached_data:
   #      data = json.loads(cached_data)
   #      if data["date"] == current_date and data["url"] == url:
   #          return data["response"]

    response = requests.get(url=url, timeout=5)
    if response.status_code == 200:
        data = response.json()
        ctx.storage.set("last_request",
            json.dumps({"date": current_date, "url": url, "response": data})
        )
        return [[hour_data, data['current']['temperature_2m'],data['current']['relativehumidity_2m'],data['current']['windspeed_10m'],data['current']['surface_pressure']]]
    return None



modelAgent = Agent(name="modelAgent", 
                   seed="modelAgent secret seed phrase",
                   port=8001,
                   endpoint=["http://127.0.0.1:8001/submit"])

fund_agent_if_low(modelAgent.wallet.address())

@modelAgent.on_event("startup")
async def introduction(ctx: Context):
   ctx.logger.info(f"Address of the agent {modelAgent.address}")

@modelAgent.on_message(model=data, replies=Weather)
async def get_predictions(ctx: Context, sender: str, response: data):
    print(get_data(ctx=ctx))
    input = np.array(response.values, dtype=object)
    # print(input)
    output = model.predict(np.array(get_data(ctx=ctx), dtype=object))
    output = float(output[0])
    # print(output)
    # print(type(output))
    await ctx.send(sender, Weather(hour=0, degrees=output, text=f"Output for th egiven input is {output}"))

if __name__ == "__main__":
   modelAgent.run()

