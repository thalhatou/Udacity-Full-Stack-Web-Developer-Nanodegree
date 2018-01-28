#! /usr/bin/env python3

# Log data analysis assigmen is part of the Udacity's Full Stack Nanodegree program

# Import modules
import psycopg2
from datetime import datetime

# Connect to the PostgreSQL database. Returns a database connection 
def connect(database_name="news"):
    try:
        # Connect to the news database
        db = psycopg2.connect("dbname={}".format(database_name))
        # Create cursor
        cursor = db.cursor()
        return db, cursor
    # If not possible to connect to the database
    except:
        print ("Unable to connect to the database")


# Return query results for given query
def get_results(query):
    # Connect to the  database
    db, cursor = connect()
    # Cursor runs queries and fetches results
    cursor.execute(query)
    return cursor.fetchall()
    # Close database
    db.close()

# Function prints result of the query



# Query 1: What are the most popular three articles of all time?
query1_question = ("What are the most popular three articles of all time?")

query1 = '''select title,count(*) as num from articles,log where
log.path=CONCAT('/article/',articles.slug) AND log.status like '%200%' group by articles.title order by
num DESC limit 3;'''


# Query 2:  Who are the most popular article authors of all time?
query2_question = ("Who are the most popular article authors of all time?")

# Query 3: On which days did more than 1% of requests lead to errors
query2_question = ("Who are the most popular article authors of all time?")


