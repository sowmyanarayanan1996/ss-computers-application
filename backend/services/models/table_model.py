from sqlalchemy import Column, String,Integer, Boolean,Float,TIMESTAMP
from sqlalchemy.sql.sqltypes import TIMESTAMP
from databases.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql.expression import text

class EnquiryEntity(Base):
    __tablename__ = 'enquiry_entity'
    enquiry_id = Column(type_=UUID(as_uuid=True),default=uuid.uuid4, nullable=True)
    enquiry_name = Column(type_=String,unique=True,nullable=False,primary_key=True)
    description = Column(type_=String,nullable=False)
    mobile_number = Column(type_=String,nullable=False)
    course=Column(type_=String,nullable=False)
    email_address= Column(type_=String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class AdmissionEntity(Base):
    __tablename__ = 'admission_entity'
    admission_id = Column(type_=UUID(as_uuid=True),default=uuid.uuid4, nullable=True)
    candidate_name = Column(type_=String,unique=True,nullable=False,primary_key=True)
    description = Column(type_=String,nullable=False)
    mobile_number = Column(type_=String,nullable=False)
    course=Column(type_=String,nullable=False)
    email_address= Column(type_=String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
