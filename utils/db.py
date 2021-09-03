import os
import psycopg2
from dotenv import load_dotenv


def connect():
    load_dotenv()
    HOST = os.getenv('HOST')
    DATABASE = os.getenv('DATABASE')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')

    """ Connect to the PostgreSQL database server """
    try:
        # connect to the PostgreSQL server
        return psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def sql(query, values):
    load_dotenv()
    HOST = os.getenv('HOST')
    DATABASE = os.getenv('DATABASE')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')

    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD)
		
        # create a cursor
        cur = conn.cursor()
        
	    # execute a statement
        cur.execute(query, values)
        conn.commit()

	    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
