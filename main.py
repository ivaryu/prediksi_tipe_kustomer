from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

app = FastAPI()
# Fungsi untuk mengganti nama kolom agar sesuai dengan yang diharapkan oleh model
def rename_columns(df):
    df.columns = [col.replace(' ', '_').replace('%', 'percent') for col in df.columns]
    return df

# Membaca model yang telah dilatih (model.pkl) dan scaler (scaler.pkl)
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

class MemberData(BaseModel):
    City: int
    Gender: int
    Product_line: int
    Unit_price: float
    Total: float
    Payment: int
    cogs: float
    Jam: int


def preprocess_data(data: MemberData):
    input_data = [
        data.City,
        data.Gender,
        data.Product_line,
        data.Unit_price,
        data.Total,
        data.Payment,
        data.cogs,
        data.Jam,
    ]

    input_data = np.array(input_data).reshape(1, -1)
    
    # Skalakan data
    scaled_data = scaler.transform(input_data)
    
    return scaled_data

@app.post("/predict")
def predict(data: MemberData):
    # Preprocessing data input
    processed_data = preprocess_data(data)
    
    # Prediksi menggunakan model
    prediction = model.predict(processed_data)
    
    # Kembalikan hasil prediksi
    return {"prediction": int(prediction[0])}
