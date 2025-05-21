from sqlalchemy.orm import Session
from app.models.character import Character
from app.schemas.character import CharacterCreate
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
        db_character = Character(**character.model_dump())
        existing_character = db.query(Character).filter(Character.id == db_character.id).first()
        if existing_character:
            raise HTTPException(status_code=400, detail="Character already exists")
        db.add(db_character)
        db.commit()
        db.refresh(db_character)
        return db_character

    @staticmethod
    def delete_character(db: Session, character_id: int):
        character = db.query(Character).filter(Character.id == character_id).first()
        if not character:
            raise HTTPException(status_code=400, detail="Character not found")
        db.delete(character)
        db.commit()
        return {"message": "Character successfully deleted"} 