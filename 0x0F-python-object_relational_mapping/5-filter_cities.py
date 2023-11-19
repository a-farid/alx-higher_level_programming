#!/usr/bin/python3
"""  lists all cities from a name from the database named hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    qr = ("""SELECT cities.name FROM cities
           INNER JOIN states ON cities.state_id = states.id
           where states.name = %s""")
    cur.execute(qr, (sys.argv[4],))
    rows = cur.fetchall()
    city_names = ', '.join(city[0] for city in rows)
    print(city_names)
    cur.close()
    db.close()
