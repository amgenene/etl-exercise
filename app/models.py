from sqlalchemy import Column, Integer, Sequence, String
from database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    signup_date = Column(String)


class Compound(Base):
    __tablename__ = "compounds"

    compound_id = Column(Integer, primary_key=True, index=True)
    compound_name = Column(String)
    compound_structure = Column(String)


class UserExperiment(Base):
    __tablename__ = "user_experiments"
    experiment_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    experiment_compound_ids = Column(String)
    experiment_run_time = Column(Integer)
