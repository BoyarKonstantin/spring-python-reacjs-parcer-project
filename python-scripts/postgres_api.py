import pandas as pd 
import csv
import psycopg2

try:
    conn = psycopg2.connect("dbname='parcerDB' user='postgres' host='localhost' password='postgres' connect_timeout=1 ")
except:
    print("Connection failed")
    
        
cursor = conn.cursor()

class ParcerPostgresAPI():

    def post_items(self, items):

        try:

            sql_delete_quety = """
                DELETE FROM parcer_model
            """
            cursor.execute(sql_delete_quety)
            sql_insert_query = """
                            INSERT INTO parcer_model (id,
                            model_name, 
                            price, 
                            available, 
                            model_link,  
                            shop_name, 
                            date, 
                            dumping_status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
            """
            result = cursor.executemany(sql_insert_query, items)
            conn.commit()

            print(cursor.rowcount, "Record inserted successfully into mobile table")

        except (Exception, psycopg2.Error) as error:

            print("Failed inserting record into mobile table {}".format(error))
        finally:
            # closing database connection.
            if conn:
                cursor.close()
                conn.close()
                print("PostgreSQL connection is closed")

    def get_items(self):

        try:
            sql_get_query = """
                SELECT * FROM parcer_model
            """
            cursor.execute(sql_get_query)
            mobile_records = cursor.fetchall()
            return mobile_records     
        except (Exception, psycopg2.Error) as error:
            print("Failed inserting record into mobile table {}".format(error))
        
        finally:
            # closing database connection.
            if conn:
                cursor.close()
                conn.close()
                print("PostgreSQL connection is closed")