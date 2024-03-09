import mysql.connector

def select(conn,query):
    cursor = conn.cursor()
    cursor.execute(query)
    results = []
    for row in cursor.fetchall():
        results.append(row)
    cursor.close()
    return results
def execute(conn,query):  # update, delete, and insert
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
def show(rows):
    for row in rows:
        print(row)

try:
    conn = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cricket")
except mysql.connector.Error as err:
    print("Cannot connect.")
    exit()

print("Select a record")
rows = select(conn,"select * from ticket_details where Ticket_id = 'tid1'")
show(rows)
print("Now insert a record")
execute(conn,"insert into ticket_details values ('tid5','2nd floor',3,72000)")
rows = select(conn,"select * from ticket_details")
show(rows)
