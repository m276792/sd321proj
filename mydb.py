import MySQLdb

def dbConnect():
    return MySQLdb.connect(
        host='localhost',
        user='root',
        password='password',
        database='mydatabase'
    )