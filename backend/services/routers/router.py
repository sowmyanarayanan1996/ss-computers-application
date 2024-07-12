from fastapi import APIRouter,Depends
from schemas.schemas import Enquiry
from sqlalchemy.orm import session as dbsession
from databases.database import get_db
import models.table_model as models

ss_computer_router = APIRouter()



@ss_computer_router.post('/enquiry/create')
def enquiry(details:Enquiry,db:dbsession=Depends(get_db)):
    try:
        details_dict = details.dict()
        new_row = models.EnquiryEntity(**details_dict)
        enquiry_details = db.query(models.EnquiryEntity).filter(models.EnquiryEntity.enquiry_name==details.enquiry_name,models.EnquiryEntity.description==details.description,models.EnquiryEntity.mobile_number==details.mobile_number,models.EnquiryEntity.course==details.course)
        if (not enquiry_details.count()):
            db.add(new_row)
            db.commit()
            db.refresh(new_row)
            return{"status code":"200","message":"successfully added the enquiry details"}
        else:
            return{"status code":"401","message":"enquiry name already present","other details":new_row}
       
    except Exception as e:
        return{"status code":"400","message":"Enquiry created failed","Error":repr(e)}
    
@ss_computer_router.get('/enquiry/retrieve')
def retrieve_enquiry(db:dbsession=Depends(get_db)):
    try:
        rows = db.query(models.EnquiryEntity.enquiry_name,models.EnquiryEntity.enquiry_name,models.EnquiryEntity.description,models.EnquiryEntity.mobile_number,models.EnquiryEntity.course,models.EnquiryEntity.enquiry_id,models.EnquiryEntity.created_at)
        if (rows.count()):
            return{"status code":"200","message":"successfully retrieve all project","details":rows.all()}
        else:
            return{"status code":"401","message":"No existing enquiry","response body":[]}
        
    except Exception as e:
        return {"status code":"400","message":"Enquiry failed to fetch","other details":repr(e)}