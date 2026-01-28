import json
import pickle
import numpy as np
import pandas as pd
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
from typing import List
import os

app = FastAPI()

# Set up templates
templates = Jinja2Templates(directory="templates")

# Load the model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

class HouseData(BaseModel):
    data: dict

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """
    Renders the home page of the House Price Prediction app.
    """
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/predict_api")
def predict_api(house_data: HouseData):
    """
    API endpoint for making predictions using JSON input.
    Returns: JSON response with the predicted price.
    """
    data = house_data.data
    input_array = np.array(list(data.values())).reshape(1, -1)
    new_data = scalar.transform(input_array)
    output = regmodel.predict(new_data)
    return {"prediction": float(output[0])}

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request):
    """
    Web endpoint that accepts form data and renders the prediction result on the home page.
    """
    form_data = await request.form()
    data = [float(x) for x in form_data.values()]
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    output = regmodel.predict(final_input)[0]
    formatted_output = "${:,.2f}".format(output * 100000)
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "predicted_price": formatted_output
        }
    )
