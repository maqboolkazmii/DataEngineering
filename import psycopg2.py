import psycopg2
#import psycopg2.extras  # for dictionary form

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = 'qwerty'
port_id = 5432
conn = None
cur = None

try:
    # Build connection
    # here we also used with, benefit  is cur closed when query execute,and commit done auto 
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )

    cur = conn.cursor(psycopg2.extras.DictCursor)  # give data in dictionary form

    # Dropping table
    cur.execute('DROP TABLE IF EXISTS employee')

    # Creating Table
    query = '''CREATE TABLE IF NOT EXISTS employee(
                        id int PRIMARY KEY,
                        name varchar(50) NOT NULL,
                        salary int,
                        dept_id varchar(30))'''
    cur.execute(query)

    # Inserting values
    insert_query = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'

    insert_values = [
        (1, 'Ali', 20000, 'D1'),
        (2, 'saleem', 27000, 'D1'),
        (3, 'muhmmad', 56000, 'D2'),
        (4, 'M.Ali', 19000, 'D3')
    ]

    # Inserting tuples from data into the database
    cur.executemany(insert_query, insert_values)

    # Showing tables in terminal
    cur.execute('SELECT * FROM employee')
    for record in cur.fetchall():
        print(record['name'], record['salary'])  # to print specific column by name, data in dict form

    # Commit updates the data in the database
    conn.commit()

except Exception as error:
    print(error)

finally:
    # Must close connection and cursor
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
