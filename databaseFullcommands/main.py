import psycopg2.extras


hostname="localhost"
database="postgres"
username="postgres"
password="zeynep123"
port_id=5432



conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=password, port=port_id)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#drop table
drop_script='drop table IF EXISTS books'


#create table
create_script = '''CREATE TABLE IF NOT EXISTS participants (
		id serial PRIMARY KEY,
		name VARCHAR ( 50 ) NOT NULL,
		surname VARCHAR ( 50 ) UNIQUE NOT NULL,
		age int NOT NULL,
		phone_number BIGINT NOT NULL);'''
cur.execute(create_script)


#insert values
def insert(name,surname,age,phone_number):
    insert_script='insert into participants(name,surname,age,phone_number) values(?,?,?,?)'
    insert_values=[name,surname,age,phone_number]
    cur.execute(insert_script,insert_values)



def update(name,surname,age,phone_number,id):
    update_script = 'update participants set name=?,surname=?,age=?,phone_number=? where id=?'
    updated_values = [name,surname,age,phone_number,id]
    cur.execute(update_script,updated_values)



def delete(id):
    delete_script= 'delete from participants  where id=?'
    cur.execute(delete_script, [id])



def select():
    select_script = 'select * from participants'
    cur.execute(select_script)
    records = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return records


#bunu yapamadın
def select_with_conditions(name):
    select_script = 'select * from books where name = %s'
    cur.execute(select_script,[name])
    records = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return records




