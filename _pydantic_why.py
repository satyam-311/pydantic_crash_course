from pydantic import BaseModel
from typing import List,Dict
class Patient(BaseModel):
    name:str
    age:int
    weight:float
    allergies:List
    contact_details:Dict[str,str]
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('inserted')
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')
patient_info={'name':'suresh','age':30,'weight':76.89,'allergies':['pollen','dust'],'contact_details':{'email':'sa@gmail.com','phn_no':'70xxxxxx9'}}
patient1=Patient(**patient_info)
update_patient_data(patient1)
    