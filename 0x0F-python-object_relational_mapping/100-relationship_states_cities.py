#!/usr/bin/python3
"""
Add a city in a State using relationship
in the database hbtn_0e_6_usa
"""

import sys
from model_state import Base
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    with sessionmaker(bind=engine)() as session:
        state = State(name='California')
        city = City(name='San Francisco')
        state.cities.append(city)
        session.add(state)
        session(city)
        session.commit()
