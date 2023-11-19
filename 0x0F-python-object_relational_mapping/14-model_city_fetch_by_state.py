#!/usr/bin/python3
"""
Shw all cities, anf Order them by ID
in the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    with sessionmaker(bind=engine)() as session:
        query_result = (session.query(State.name, City.id, City.name)
                        .join(City, State.id == City.state_id)
                        .all())

        for instance in query_result:
            print(f"{instance[0]}: ({instance[1]}) {instance[2]}")

