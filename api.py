import json
import pickle
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class model_input(BaseModel): 
  Pregnancies: int
  Glucose: int
  BloodPressure: int
  SkinThickness: int
  Insulin: int
  BMI: float
  DiabetesPedigreeFunction: float
  Age: int

# Loading the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

@app.post('/predict')
def diabetes_predd(inputs: model_input):
  input_data = inputs.json()
  input_data = json.loads(input_data)

  preg = input_data['Pregnancies']
  glucose = input_data['Glucose']
  bp = input_data['BloodPressure']
  st = input_data['SkinThickness']
  insulin = input_data['Insulin']
  bmi = input_data['BMI']
  dpf = input_data['DiabetesPedigreeFunction']
  age = input_data['Age']

  input_list = [preg, glucose, bp, st, insulin, bmi, dpf, age]
  prediction = diabetes_model.predict([input_list])

  if prediction[0] == 0:
    result = 'Non-Diabetic'
  else:
    result = 'Diabetic'
  
  return result