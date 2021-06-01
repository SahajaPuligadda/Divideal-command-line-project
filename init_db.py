import sqlite3

connection = sqlite3.connect('database.db')

with open('settlement_schema.sql') as f:
    connection.executescript(f.read())

with open('schema.sql') as f:
    connection.executescript(f.read())

with open('pots.sql') as f:
    connection.executescript(f.read())

with open('items.sql') as f:
    connection.executescript(f.read())

with open('consumer.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# lists = cur.execute("SELECT payee_name,amount,receiver_name FROM settlement").fetchall()
# print(cur.execute("SELECT * FROM participants").fetchall())
# print(cur.execute("SELECT * FROM items t JOIN consumer c ON t.id = c.item_id").fetchall())

connection.commit()
connection.close()

# print(lists)
