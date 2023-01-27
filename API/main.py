from fastapi import FastAPI
from model import predict
from pydantic import BaseModel

class Textin(BaseModel):
    age : int
    sex : str
    children : int
    smoker : str
    region : str
    grade : str

class Prediction(BaseModel):
    charges : float

app = FastAPI()

@app.post("/predict", response_model=Prediction)
async def root_predict(payload : Textin):
    value = [x for x in payload.__dict__.values()]
    to_return = predict(value)
    return {"charges": to_return}