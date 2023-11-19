#!/usr/bin/python3
""" prints All the States contains letter 'a'
    from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    name = sys.argv[4]
    state = session.query(State).filter(State.name.ilike(name)).first()
    if not state:
        print("Not found")
    else:
        print(f"{state.id}")
