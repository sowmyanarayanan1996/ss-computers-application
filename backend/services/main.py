from fastapi import FastAPI
from routers.router import ss_computer_router
from databases.database import Base,postgres_engine
from fastapi.middleware.cors import CORSMiddleware




Base.metadata.create_all(bind = postgres_engine)

app = FastAPI(title="ss computers website")

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins =["*"],
    allow_credentials =True,
    allow_methods =["*"],
    allow_headers=["*"]
)


app.include_router(ss_computer_router)







if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app",reload=True,port=8061)