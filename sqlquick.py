import pymysql
import datetime

current_date = datetime.datetime.now()

# Open database connection
db = pymysql.connect(
      host='sql.freedb.tech',
      port=3306,
      user='freedb_ben123',
   passwd='eEvaBGM4zX7J$8*',
   db='freedb_hellosql'
   )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO users2(user_id, \
   user_name, creation_date) \
   VALUES ('%s', '%s', '%d')" % \
   ('3', 'pavlik', )
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
   print"didnt insert info to db' rolling back"

# disconnect from server
db.close()