import json
from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
import random
import streamlit as st
from typing import Union
import random
from front2 import check

#Sample MY_DATA ---- to be collected from user
MY_DATA = {"latitude": 12.800962392747023, "longitude": 80.22415148590215, "hour": 12}
MODEL_DATA = [['0700', 26.52, 71.6, 2.97, 89554]]
temperatureAgent = 'agent1qfg6mtr2lvfdjj3c8gl83pfl5e3ud25ygkfqhpvvek5u3walenawwyjr65y'
modelAgent = 'agent1qvs00xtuvuvpq02qzg20unh50jqwhyrry7ycpm3834mktnwhy3e45m7vtpp'

#Requesting for data in a specified format.
class RequestWeather(Model):
    latitude: float
    longitude: float
    hour: int

#returning the result in Weather format.
class Weather(Model):
    hour: int
    degrees: float
    text: str

#data to be sent to modelAgent
class data(Model):
   values:list

#data to be 
# class preds(Model):
#    values:str
#    text:str

flag=0

webAgent = Agent(name='webAgent',
                 seed='webAgent secret phrase',
                 port=8000,
                 endpoint=["http://127.0.0.1:8000/submit"])

fund_agent_if_low(webAgent.wallet.address())

@webAgent.on_event('startup')
def introuce_webAgent(ctx: Context):
    ctx.logger.info("Starting webAgent...")

@webAgent.on_interval(5)
async def get_weather_data(ctx: Context):
    
    """This function sends a request to the weather agent every 10 seconds"""
    ctx.logger.info("Sending request for prediction...")
    flag = random.randint(0,1)   
    await ctx.send(
        temperatureAgent,
        RequestWeather(
            latitude=MY_DATA["latitude"],
            longitude=MY_DATA["longitude"],
            hour=MY_DATA["hour"],
        ),
    )
    if flag:
        await ctx.send(modelAgent, data(values=MODEL_DATA))

@webAgent.on_message(model=Weather)
async def handle_weather_response(ctx: Context, sender: str, msg: Weather):
    
    with open('database.json','r') as f:
        data = json.load(f)

    # Access the values from the loaded JSON data
    input1 = data['input1']
    input2 = data['input2']

    print("input values", input1, input2)

    """This function handles the response from the weather agent"""
    if sender == temperatureAgent:
        val = msg.degrees
        print(val, "val from api")
        if input1< val and val<input2:

            print(f"inside if loop")
            check(1)
        else:
            print("change in range")
            check(0)
        ctx.logger.info(f"Got response from temperature_agent ({sender[-10:]}): {msg.text}")
    elif sender == modelAgent:
        ctx.logger.info(f"Got response from solar_Model agent ({sender[-10:]}): {msg.text}")
    else:
        ctx.logger.info("Waiting for the response...")

# # Set the title and a brief description
# st.title("PhotoVoltaic Power Prediction")
# st.write("Enter the minimum and maximum value of temperature")

# # Add input fields for floating-point numbers
# input1 = st.number_input("Enter the minimum value:", value=0.0, step=0.01)
# input2 = st.number_input("Enter the maximum value:", value=0.0, step=0.01)

# # Add a button to trigger a dialog box
# if st.button("Show Dialog Box"):
#     # Create a message based on the input values
#     message = f"You entered: Input 1 - {input1:.2f}, Input 2 - {input2:.2f}"

#     # Show the message in a dialog box
#     st.info(message)

# while(True):
#     introduce_webAgent(Context)


webAgent.run()