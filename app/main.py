from fastapi import FastAPI
from typing import List
from etl import run_etl_process
from sqlalchemy.orm import Session
import uvicorn
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
import models, schemas

SQLALCHEMY_DATABASE_URL = "postgresql://newuser:newpassword@db/newdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.on_event("startup")
async def startup_event():
    run_etl_process()
    return {"message": "ETL process started."}

@app.get("/run_etl")
def run_etl():
    run_etl_process()
    return {"message": "ETL process completed."}

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

@app.get("/experiments", response_model=List[schemas.UserExperiment])
async def read_experiments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    experiments = db.query(models.UserExperiment).offset(skip).limit(limit).all()
    print(experiments)
    return experiments

@app.get("/compounds", response_model=List[schemas.Compound])
async def read_compounds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    compounds = db.query(models.Compound).offset(skip).limit(limit).all()
    return compounds

@app.get("/experiments/{experiment_id}", response_model=schemas.UserExperiment)
def read_user_experiment(experiment_id: int, db: Session = Depends(get_db)):
    db_user_experiment = db.query(models.UserExperiment).filter(models.UserExperiment.experiment_id == experiment_id).first()
    if db_user_experiment is None:
        raise HTTPException(status_code=404, detail="User experiment not found")
    return db_user_experiment

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    run_etl_process()