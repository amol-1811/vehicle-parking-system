from re import U
import mysql.connector
import mysql.connector
from mysql.connector import errorcode
from db_credentials import config


def connect():
     try:
          connection = mysql.connector.connect(**config)
          print("Connected to Database..")
          return connection

     except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
               print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
               print("Database does not exist")
          else:
               print(err)