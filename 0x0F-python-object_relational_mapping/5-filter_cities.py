#!/usr/bin/python3
"""  lists all cities from a name from the database named hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    qr1 = ("""SELECT states.id FROM states
                WHERE states.name = %s""")
    cur.execute(qr1, (sys.argv[4],))
    stateId_result = cur.fetchone()
    if stateId_result:
        stateId = stateId_result[0]
        qr2 = ("""SELECT cities.name FROM cities
            WHERE cities.state_id = %s
            ORDER BY cities.id""")
        cur.execute(qr2, (stateId,))
        rows = cur.fetchall()
        city_names = ', '.join(city[0] for city in rows)
        print(city_names)
    else:
        print()
    cur.close()
    db.close()
