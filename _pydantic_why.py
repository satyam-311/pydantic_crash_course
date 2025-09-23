"""from pydantic import BaseModel
from typing import List,Dict,Optional
class Patient(BaseModel):
    name:str
    age:int
    weight:float
    allergies:Optional[List[str]]=None
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
patient_info={'name':'suresh','age':30,'weight':76.89,'contact_details':{'email':'sa@gmail.com','phn_no':'70xxxxxx9'}}
patient1=Patient(**patient_info)
update_patient_data(patient1)
    """
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.email)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', 'age': 30, 'weight': 75.2,'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)