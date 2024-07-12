from pydantic import BaseModel



class Enquiry(BaseModel):
    enquiry_name:str
    mobile_number:str
    course:str
    description:str