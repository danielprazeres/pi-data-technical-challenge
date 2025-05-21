from pydantic import BaseModel, Field, ConfigDict

class CharacterBase(BaseModel):
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int

class CharacterCreate(CharacterBase):
    pass

class Character(CharacterBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class CharacterResponse(BaseModel):
    id: int
    name: str
    height: int
    mass: int
    birth_year: int
    eye_color: str
    model_config = ConfigDict(from_attributes=True) 