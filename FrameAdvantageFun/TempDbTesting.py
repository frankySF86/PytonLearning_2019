import sqlite3

with sqlite3.connect(":memory:") as connection:
    print(type(connection))
    dbcursor = connection.cursor()
    dbcursor.execute("CREATE TABLE mytesttable(fighterName nvachar(15), fighterage int)")
    fighter_values=(("Ryu",35),("Chun Li",21),("Cammy",24))
    dbcursor.executemany("INSERT INTO mytesttable VALUES (?, ?)",fighter_values)
    records = dbcursor.execute("SELECT * FROM mytesttable").fetchall()
    print(type(records))

for fighter in records:
    print(fighter[0] + " " + str(fighter[1]))

