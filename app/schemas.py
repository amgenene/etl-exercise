from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    signup_date: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True


class CompoundBase(BaseModel):
    compound_name: str
    compound_structure: str


class CompoundCreate(CompoundBase):
    pass


class Compound(CompoundBase):
    compound_id: int
    class Config:
        orm_mode = True


class UserExperimentBase(BaseModel):
    user_id :int
    experiment_compound_ids: str
    experiment_run_time: int


class UserExperimentCreate(UserExperimentBase):
    pass


class UserExperiment(UserExperimentBase):
    experiment_id: int
    class Config:
        orm_mode = True
