# pip install fastapi, uvicorn, pydantic

from fastapi import FastAPI
import json 

app = FastAPI()
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
        
    return data

@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get("/about")
def about():
    return {'message':'A fully functional API to mange your patient records'}

@app.get('/view')
def view():
    data = load_data()
    
    return data

# a endpoint from which user can look at a speciifc patient profile.

@app.get('/patient/{patient_id}')
def view_patient(patient_id : str):
    data = load_data() #load all the data
    if patient_id in data:
        return data[patient_id]
    
    return {'error' : 'patient_not_found'} # in curly braces we need to do key value pair