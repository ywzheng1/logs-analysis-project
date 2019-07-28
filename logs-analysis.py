#! /usr/bin/env python3

import psycopg2

DBNAME = "news"

query1 = """SELECT *
            FROM articles_view
            LIMIT 3"""

query2 = """SELECT name, sum(articles_view.view) as view
            FROM article_authors, articles_view
            WHERE articles_view.title = article_authors.title
            GROUP BY name ORDER BY view DESC;"""

query3 = """SELECT round(cast((error_count/logcount::float)*100 as numeric) ,2)
            as Error_Percent, error_log.time
            FROM logcount, error_log
            WHERE logcount.time = error_log.time
            and round(cast((error_count/logcount::float)*100 as numeric) ,2) > 1.0;"""


# 1. What are the most popular three articles of all time? Which articles have been accessed the most?
# Present this information as a sorted list with the most popular article at the top.
def most_popular_articles(query):
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    print("\nMost popular article authors of all time are: ")
    for item in result:
        print(str(item[0]) + " - " + str(item[1]) + " views")


# 2. Who are the most popular article authors of all time?
# That is, when you sum up all of the articles each author has written, which authors get the most page views?
# Present this as a sorted list with the most popular author at the top.
def most_popular_author(query):
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    print("\nMost popular article authors of all time are: ")
    for item in result:
        print(str(item[0]) + " - " + str(item[1]) + " views")


# 3. On which days did more than 1% of requests lead to errors?
# The log table includes a column status that indicates the HTTP status code
# that the news site sent to the user's browser.
def error_calculate(query):
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    print("\nDays have more than 1% of bad requests: ")
    for item in result:
        print(str(item[0]) + "%" + " - " + str(item[1]))


most_popular_articles(query1)
most_popular_author(query2)
error_calculate(query3)
