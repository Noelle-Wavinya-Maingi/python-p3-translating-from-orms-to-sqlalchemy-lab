from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///:memory')


def create_table(base, engine):
    base.metadata.create_all(engine)


def save(session, dog):
    session.add(dog)
    session.commit()


def get_all(session):
    all_dogs = session.query(Dog).all()
    return all_dogs


def find_by_name(session, name):
    dog = session.query(Dog).filter(Dog.name == name).first()
    return dog


def find_by_id(session, id):
    dog_id = session.query(Dog).filter(Dog.id == id).first()
    return dog_id


def find_by_name_and_breed(session, name, breed):
    dogs = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return dogs


def update_breed(session, dog, breed):
    session.query(Dog).update({Dog.breed: breed})