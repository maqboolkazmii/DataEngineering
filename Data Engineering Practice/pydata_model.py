import psycopg2
#import psycopg2.extras # dicnatory form


hostname = 'localhost'
database = 'pydatabase'
username = 'postgres'
pwd = 'qwerty'
port_id = 5432
conn = None
cur = None


try:
    #build conection
    # here we also used with, benefit  is cur closed when query execute,and commit done auto 
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    cur = conn.cursor()
    #cur = conn.cursor(psycopg2.extras.DictCursor) # give data in dicationary from

#droping table
    cur.execute('DROP TABLE IF EXISTS employee')

# Creating Table
    query = ''' CREATE TABLE IF NOT EXISTS employee(
                        id int PRIMARY KEY,
                        name varchar(50) NOT NULL,
                        salary int,
                        dept_id varchar(30))'''
    cur.execute(query)

# inserting values
    insert_query = 'INSERT INTO employee (id, name, salary, dept_id) VALUES(%s, %s, %s, %s)'

    # insert_value =(1, 'Ali', 20000, 'D1') on evalue
    # if multiple value wecan give it in a tuple list
    insert_values =[(1, 'Ali', 20000, 'D1'),(2, 'saleem', 27000, 'D1'), (3, 'muhmmad', 56000, 'D2'), (4, 'M.Ali', 19000, 'D3')]
    

#update values
    update_qurey = 'UPDATE employee SET salary = salary + (salary*0.5)'
    cur.execute(update_qurey)

#delete 
    delete_query ='DELETE FROM employee WHERE name =%s'
    delete_record =('Ali')
    cur.execute(delete_query, delete_record)
# inserting tuples from data into database 
    for record in insert_values:
        cur.execute(insert_query, record)

# showing tables in terminal
    cur.execute('SELECT * FROM employee')
    for record in cur.fetchall():
        #print(record)    #print all record
        print(record[1], record[2]) # to print specific column

        #print(record['name'], record['salary']) # to print specific column by name , data in dic from
    
    #commit update the data in databse
    conn.commit()

except Exception as error:
    print(error)

finally:
    #must close conection and cursor
    if cur is not None:
        cur.close()
    if conn is not None:
         conn.close()