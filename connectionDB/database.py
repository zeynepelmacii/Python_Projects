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
create_script = ''' CREATE TABLE IF NOT EXISTS books (
                        isbn BIGINT primary key UNIQUE NOT NULL,
                        name VARCHAR ( 50 ) NOT NULL,
                        writer VARCHAR ( 50 )  NOT NULL,
                        publisher VARCHAR ( 50 )  NOT NULL,
                        page INTEGER NOT NULL,
                        price INTEGER NOT NULL,
                        score DECIMAL NOT NULL);'''
cur.execute(create_script)


#insert values
def insert(isbn,name,writer,publisher,page,price,score):
    insert_script='insert into books (isbn,name,writer,publisher,page,price,score) values(%s,%s,%s,%s,%s,%s,%s)'
    insert_values=[isbn,name,writer,publisher,page,price,score]
    cur.execute(insert_script,insert_values)



def update(isbn,name,writer,publisher,page,price,score):
    update_script = 'update books set name=%s,writer=%s,publisher=%s,page=%s,price=%s,score=%s where isbn=%s'
    updated_values = [name,writer,publisher,page,price,score,isbn]
    cur.execute(update_script,updated_values)



def delete(isbn):
    delete_script= 'delete from books where isbn=%s'
    cur.execute(delete_script,[isbn])



def select():
    select_script = 'select * from books'
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




