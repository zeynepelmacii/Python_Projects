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
		name VARCHAR ( 50 ) NOT NULL,
		surname VARCHAR ( 50 ) UNIQUE NOT NULL,
		age int NOT NULL,
		phone_number BIGINT NOT NULL);'''
cur.execute(create_script)


#insert values
def insert(name,surname,age,phone_number):
    insert_script='insert into participants(name,surname,age,phone_number) values(%s,%s,%s,%s)'
    insert_values=[name,surname,age,phone_number]
    cur.execute(insert_script,insert_values)



def update(name,surname,age,phone_number,id):
    update_script = 'update participants set name=%s,surname=%s,age=%s,phone_number=%s where id=%s'
    updated_values = [name,surname,age,phone_number,id]
    cur.execute(update_script,updated_values)



def delete(id):
    delete_script= 'delete from participants  where id=%s'
    cur.execute(delete_script, [id])



def select():
    select_script = 'select * from participants'
    cur.execute(select_script)
    records = cur.fetchall()
    conn.commit()
    return records


def select_condition(name):
    select_script = "select * from participants where upper (name) like upper (%s)"
    condition = ['%'+name+'%']
    cur.execute(select_script,condition)
    records = cur.fetchall()
    conn.commit()
    return records




