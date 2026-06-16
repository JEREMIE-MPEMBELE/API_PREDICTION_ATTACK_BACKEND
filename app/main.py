from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
import numpy as np
import joblib
import os
from .schemas import DataInput, PredictionOutPut

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",   
        "http://127.0.0.1:5500",   
        "http://127.0.0.1:3000",   
        "http://127.0.0.1:8000",   
        
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')
model = joblib.load(model_path)

@app.get("/")
def home():
    return {"message": "BIENVENUE DANS L'API DE PREDICTION D'ATTAQUE DE CYBERSECURITE"}

@app.post("/predict", response_model=PredictionOutPut)
def prediction(data: DataInput):
    features = np.array([[
        data.network_packet_size,
        data.login_attempts,
        data.session_duration,
        data.ip_reputation_score,
        data.failed_logins
    ]])
    
    classe = model.predict(features)[0]
    score = model.predict_proba(features).max()
    
    return PredictionOutPut(classe=classe, score=score)