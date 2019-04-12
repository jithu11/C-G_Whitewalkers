import pymysql as MySQLdb

# Open database connection
db = MySQLdb.connect("127.0.0.1","root","jithin@12","Bank_Application")
#db = MySQLdb.connect(host='localhost',user='root',passwd='')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.

cursor.execute('''INSERT INTO BankDetail values ('3000', 'joe', '1900-07-03')''')
cursor.execute('''SELECT * FROM BankDetail''')

# Fetch a single row using fetchone() method.
data = cursor.fetchall()

#print the data
print (data)

#commit the changes to db
db.commit()

# disconnect from server
db.close()