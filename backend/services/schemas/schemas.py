from pydantic import BaseModel



class Enquiry(BaseModel):
    enquiry_name:str
    mobile_number:str
    course:str
    email_address:str
    description:str


class Admission(BaseModel):
    candidate_name:str
    mobile_number:str
    course:str
    email_address:str
    description:str

