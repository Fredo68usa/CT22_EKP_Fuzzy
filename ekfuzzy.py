# def my_function():
#    print("Hello World")

# Defining our variable
# name = "Nicholas"

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import psycopg2
import socket
import sys


# Defining a class
class EKFuzzy:
    def __init__(self):
        self.course = "Course"
        self.name = "Name"
        self.myListMeta_IP = []
        self.myListMeta_Env = []
        self.myListMeta_SubEnv = []
        self.myListMeta_FQDN = []
        self.myListIPs = []
        self.cnt = 0

        #Access to PostGreSQL
        self.postgres_connect = None
        self.cursor = None
        if len(sys.argv) < 2 :
           self.tbcSQL = None
        else : 
           self.tbcSQL = sys.argv[1].upper()



    # Opening PostGreSQL
    def open_PostGres(self):

      try:
         self.postgres_connect = psycopg2.connect(user = "context22",
                                  # password = "AIM2020",
                                  # host = "127.0.0.1",
                                  port = "5432",
                                  database = "context22"
                                  )


      except (Exception, psycopg2.Error) as error :
         print("Error while connecting to PostgreSQL", error)
         print ("Hello")


    def posGresPrep(self):
        self.open_PostGres()
        self.cursor = self.postgres_connect.cursor()
        print ( self.postgres_connect.get_dsn_parameters(),"\n")
        self.cursor.execute("SELECT version();")
        record = self.cursor.fetchone()
        print("You are connected to - ", record,"\n")

        postgres_currentSQLs_query = """ SELECT * FROM currentsqls"""
        self.cursor.execute(postgres_currentSQLs_query)
        self.sql_records = self.cursor.fetchall()

    def checkFuzzy(self):
      for row in self.sql_records:
          print (row[0], "  ", row[1])
          refSQL = row[1].upper()
          # print (fuzz.ratio(self.tbcSQL, row[1]), "--" ,fuzz.partial_ratio(self.tbcSQL, row[1]))
          print (fuzz.ratio(self.tbcSQL, refSQL), "--" ,fuzz.partial_ratio(self.tbcSQL, refSQL))
          # print (fuzz.partial_ratio("Catherine M Gitau","Catherine Gitau"))
          # print (fuzz.token_sort_ratio("Catherine M Gitau","Catherine Gitau"))


