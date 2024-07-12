from fastapi import FastAPI
from routers.router import ss_computer_router
from databases.database import Base,postgres_engine

Base.metadata.create_all(bind = postgres_engine)

app = FastAPI(title="ss computers website")




app.include_router(ss_computer_router)







if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app",reload=True,port=8061)