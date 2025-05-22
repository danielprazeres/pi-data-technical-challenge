from sqlalchemy.orm import Session
from app.models.character import Character
from app.schemas.character import CharacterCreate
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

class CharacterService:
    @staticmethod
    def get_all_characters(db: Session):
        return db.query(Character).all()

    @staticmethod
    def get_character_by_id(db: Session, character_id: int):
        character = db.query(Character).filter(Character.id == character_id).first()
        if not character:
            raise HTTPException(status_code=400, detail="Character not found")
        return character

    @staticmethod
    def create_character(db: Session, character: CharacterCreate):
        new_character = Character(**character.dict())
        db.add(new_character)
        try:
            db.commit()
            db.refresh(new_character)
            return new_character
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Character with this ID already exists")

    @staticmethod
    def delete_character(db: Session, character_id: int):
        character = db.query(Character).filter(Character.id == character_id).first()
        if not character:
            raise HTTPException(status_code=400, detail="Character not found")
        db.delete(character)
        db.commit()
        return {"message": "Character successfully deleted"} 