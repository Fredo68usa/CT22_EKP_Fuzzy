# version 1.1 : automatic addition of SQLs being tested


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
      maxScore = 0 
      maxScoreSQL = []  
      ListmaxScoreSQL = []
      for row in self.sql_records:
          print (row[0], "  ", row[1])
          refSQL = row[1].upper()
          # print (fuzz.ratio(self.tbcSQL, row[1]), "--" ,fuzz.partial_ratio(self.tbcSQL, row[1]))
          print (fuzz.ratio(self.tbcSQL, refSQL), "--" ,fuzz.partial_ratio(self.tbcSQL, refSQL))
          current_score = fuzz.partial_ratio(self.tbcSQL, refSQL)
          print (" Max Score = ", maxScore , "Current Score = ", current_score)
          if current_score > maxScore :
              maxScore = current_score
              maxScoreSQL = []
              ListmaxScoreSQL = []
              # record the new SQL statement , md5 and statement
              maxScoreSQL.append(row[0])
              maxScoreSQL.append(row[1])
              ListmaxScoreSQL.append(maxScoreSQL)
              print (maxScoreSQL , " ---" , ListmaxScoreSQL)

          elif current_score == maxScore:
              # record the new SQL statement
              maxScoreSQL = []
              # record the new SQL statement , md5 and statement
              maxScoreSQL.append(row[0])
              maxScoreSQL.append(row[1])
              ListmaxScoreSQL.append(ListmaxScoreSQL)
          else :
              pass

      for sqlSim in ListmaxScoreSQL :
          print ("To Be Recorded")
          print (sqlSim)
          self.write_PosGres(sqlSim,maxScore)

          # print (fuzz.partial_ratio("Catherine M Gitau","Catherine Gitau"))
          # print (fuzz.token_sort_ratio("Catherine M Gitau","Catherine Gitau"))


    def write_PosGres(self,sqlSim,maxScore):
        print (" In write_PosGres" ) 
        SQL_value = self.tbcSQL
        hashSim = sqlSim[0]
        # postgres_currentSQLs_query = """ INSERT INTO currentsqls VALUES ( md5('SELECT * FROM CCNTBL2'), 'SELECT * FROM CCNTBL2', 'pending', False, 300);"""
        # postgres_currentSQLs_query = """ INSERT INTO currentsqls VALUES ( md5(%s), %s , %s,'pending', %s, %s);"""
        # self.cursor.execute(postgres_currentSQLs_query)
        # self.cursor.execute(postgres_currentSQLs_query, (SQL_value,SQL_value,hashSim,'Pending',maxScore,300,))
        postgres_currentSQLs_query = """ INSERT INTO currentsqls (hash,SQL,hashSim, status, score, frequency) VALUES (md5(%s),%s,%s,%s,%s,%s);"""
        self.cursor.execute(postgres_currentSQLs_query, (SQL_value, SQL_value, hashSim, 'Pending', maxScore, 300 ,))
        self.postgres_connect.commit()
        self.cursor.close()

    def close_PosGres(self):
        self.postgres_connect.close()
