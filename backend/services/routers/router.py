from fastapi import APIRouter,Depends
from schemas.schemas import Enquiry,Admission
from sqlalchemy.orm import session as dbsession
from databases.database import get_db
import models.table_model as models

ss_computer_router = APIRouter()



@ss_computer_router.post('/enquiry/create',tags=["Enquiry"])
def create_enquiry(details:Enquiry,db:dbsession=Depends(get_db)):
    try:
        details_dict = details.dict()
        new_row = models.EnquiryEntity(**details_dict)
        enquiry_details = db.query(models.EnquiryEntity).filter(models.EnquiryEntity.enquiry_name==details.enquiry_name,models.EnquiryEntity.description==details.description,models.EnquiryEntity.mobile_number==details.mobile_number,models.EnquiryEntity.course==details.course,models.EnquiryEntity.email_address==details.email_address)
        if (not enquiry_details.count()):
            db.add(new_row)
            db.commit()
            db.refresh(new_row)
            return{"status code":"200","message":"successfully added the enquiry details"}
        else:
            return{"status code":"401","message":"enquiry name already present","enquired details":new_row}
       
    except Exception as e:
        return{"status code":"400","message":"Enquiry created failed","Error":repr(e)}
    
@ss_computer_router.get('/enquiry/retrieve',tags=["Enquiry"])
def retrieve_enquiry(db:dbsession=Depends(get_db)):
    try:
        rows = db.query(models.EnquiryEntity.enquiry_name,models.EnquiryEntity.enquiry_name,models.EnquiryEntity.description,models.EnquiryEntity.mobile_number,models.EnquiryEntity.course,models.EnquiryEntity.email_address,models.EnquiryEntity.enquiry_id,models.EnquiryEntity.created_at)
        if (rows.count()):
            return{"status code":"200","message":"successfully retrieve all equiries","details":rows.all()}
        else:
            return{"status code":"401","message":"No existing enquiry","response body":[]}
        
    except Exception as e:
        return {"status code":"400","message":"Enquiry failed to fetch","other details":repr(e)}
    
@ss_computer_router.delete('/enquiry/delete',tags=["Enquiry"])
def delete_enquiry(details:Enquiry,db:dbsession=Depends(get_db)):
        try:
    
            
            enquiry_delete_details = db.query(models.EnquiryEntity).filter(models.EnquiryEntity.enquiry_name==details.enquiry_name,models.EnquiryEntity.mobile_number==details.mobile_number)
            if (enquiry_delete_details.count()):
                enquiry_delete_details.delete(synchronize_session=False)
                db.commit()
                
                return{"status code":"200","message":"successfully deleted the enquiry details"}
            else:
                return{"status code":"401","message":"There is no enquiry details with this name, please add the enquiry details"}
       
        except Exception as e:
            return{"status code":"400","message":"Enquiry created failed","Error":repr(e)}


@ss_computer_router.post('/admission/create',tags=['Admission'])
def create_admission(details:Admission,db:dbsession=Depends(get_db)):
    try:
        details_dict = details.dict()
        new_row = models.AdmissionEntity(**details_dict)
        admission_details = db.query(models.AdmissionEntity).filter(models.AdmissionEntity.candidate_name==details.candidate_name,models.AdmissionEntity.description==details.description,models.AdmissionEntity.mobile_number==details.mobile_number,models.AdmissionEntity.course==details.course,models.AdmissionEntity.email_address==details.email_address)
        if (not admission_details.count()):
            db.add(new_row)
            db.commit()
            db.refresh(new_row)
            return{"status code":"200","message":"successfully added the admission details"}
        else:
            return{"status code":"401","message":"admission name already present","admission details":new_row}
       
    except Exception as e:
        return{"status code":"400","message":"Admission created failed","Error":repr(e)}
    

@ss_computer_router.get('/admission/retrieve',tags=["Admission"])
def retrieve_admission(db:dbsession=Depends(get_db)):
    try:
        rows = db.query(models.AdmissionEntity.candidate_name,models.AdmissionEntity.description,models.AdmissionEntity.mobile_number,models.AdmissionEntity.course,models.AdmissionEntity.email_address,models.AdmissionEntity.admission_id,models.AdmissionEntity.created_at)
        if (rows.count()):
            return{"status code":"200","message":"successfully retrieve all admission","details":rows.all()}
        else:
            return{"status code":"401","message":"No existing admission","response body":[]}
        
    except Exception as e:
        return {"status code":"400","message":"Admission failed to fetch","other details":repr(e)}
    
@ss_computer_router.delete('/admission/delete',tags=["Admission"])
def delete_admission(details:Admission,db:dbsession=Depends(get_db)):
        try:
    
            
            enquiry_delete_details = db.query(models.AdmissionEntity).filter(models.AdmissionEntity.candidate_name==details.candidate_name,models.AdmissionEntity.mobile_number==details.mobile_number)
            if (enquiry_delete_details.count()):
                enquiry_delete_details.delete(synchronize_session=False)
                db.commit()
                
                return{"status code":"200","message":"successfully deleted the enquiry details"}
            else:
                return{"status code":"401","message":"There is no enquiry details with this name, please add the enquiry details"}
       
        except Exception as e:
            return{"status code":"400","message":"Enquiry created failed","Error":repr(e)}
