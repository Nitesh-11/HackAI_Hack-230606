from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
# from typing_extensions import NDArray
import warnings
import pickle 
import numpy as np

# #loading weight files
with warnings.catch_warnings():
  warnings.filterwarnings("ignore", category=UserWarning)
  model = pickle.load(open("model4.pkl", "rb"))

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

#getter for data
def get_data(inputs: data):
   inputs = np.array(inputs, dtype=object)
   return inputs

#returns a list with values
def get_predictions(input):
   return model.predict(input)

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
    input = np.array(response.values, dtype=object)
    # print(input)
    output = model.predict(input)
    output = float(output[0])
    # print(output)
    # print(type(output))
    await ctx.send(sender, Weather(hour=0, degrees=output, text=f"Output for th egiven input is {output}"))

if __name__ == "__main__":
   modelAgent.run()

