from app.database.base import SessionLocal, engine
from app.models.character import Character
from sqlalchemy.exc import IntegrityError

# Insert sample data
characters = [
    Character(id=1, name="Daniel Prazeres", height=178, mass=72, hair_color="brown", skin_color="light", eye_color="green", birth_year=1996),
    Character(id=2, name="Bruna Battazza", height=165, mass=58, hair_color="black", skin_color="fair", eye_color="brown", birth_year=1997),
    Character(id=3, name="Arya", height=60, mass=23, hair_color="white", skin_color="gray", eye_color="blue", birth_year=2021),
    Character(id=4, name="Obi-Wan Kenobi", height=182, mass=77, hair_color="auburn", skin_color="light", eye_color="blue-gray", birth_year=1975),
    Character(id=5, name="Leia Organa", height=150, mass=49, hair_color="brown", skin_color="light", eye_color="brown", birth_year=1977),
]

def seed_db():
    db = SessionLocal()
    for char in characters:
        try:
            db.add(char)
            db.commit()
            print(f"✅ Added {char.name}")
        except IntegrityError:
            db.rollback()
            print(f"⚠️  Character with id {char.id} already exists.")
    db.close()

if __name__ == "__main__":
    seed_db()