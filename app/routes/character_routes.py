from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.schemas.character import CharacterCreate, Character, CharacterResponse
from app.services.character_service import CharacterService
from typing import List

router = APIRouter()

@router.get("/character/getAll", response_model=List[CharacterResponse])
def get_all_characters(db: Session = Depends(get_db)):
    """
    Returns all registered characters.
    """
    return CharacterService.get_all_characters(db)

@router.get("/character/get/{character_id}", response_model=Character)
def get_character(character_id: int, db: Session = Depends(get_db)):
    """
    Returns a specific character by ID.
    """
    return CharacterService.get_character_by_id(db, character_id)

@router.post("/character/add", response_model=Character)
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    """
    Creates a new character.
    """
    return CharacterService.create_character(db, character)

@router.delete("/character/delete/{character_id}")
def delete_character(character_id: int, db: Session = Depends(get_db)):
    """
    Deletes a character by ID.
    """
    return CharacterService.delete_character(db, character_id) 