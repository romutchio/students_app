from pydantic import BaseModel, validator


class Student(BaseModel):
    id: int
    full_name: str
    rating: int
    age: int
    photo_link: str
    speciality: str
    group: str
    sex: str
    fav_colour: str
    
    @validator('full_name')
    def validate_full_name(cls, v):
        if len(v.split()) < 3:
            raise ValueError('full_name should contain first, middle and last names')
        return v

    @validator('age')
    def validate_age(cls, v):
        if v <= 0:
            raise ValueError("Age must be a positive integer")
        elif v < 15:
            raise ValueError("Constructed student is too young")
        return v

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
