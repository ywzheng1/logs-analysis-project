"""
The database includes three tables:
    - The authors table includes information about the authors of articles.
    - The articles table includes the articles themselves.
    - The log table includes one entry for each time a user has accessed the site.
"""

import psycopg2

DBNAME = "news"


# 1. What are the most popular three articles of all time? Which articles have been accessed the most?
# Present this information as a sorted list with the most popular article at the top.
def most_popular_articles():
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute("select path, COUNT(ip) from log where path != '/' group by path order by COUNT DESC limit 3;")
    result=c.fetchall()
    db.close()
    print("\nMost popular article authors of all time are: ")
    for item in result:
        print(str(item[0]) + " - " + str(item[1]) + " views")

most_popular_articles()



# 2. Who are the most popular article authors of all time?
# That is, when you sum up all of the articles each author has written, which authors get the most page views?
# Present this as a sorted list with the most popular author at the top.
def most_popular_author():
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute("select name, view from articles_view, article_authors where articles_view.title = article_authors.title ORDER BY view DESC;")
    result=c.fetchall()
    db.close()
    print("\nMost popular article authors of all time are: ")
    for item in result:
        print(str(item[0]) + " - " + str(item[1]) + " views")

most_popular_author()



# 3. On which days did more than 1% of requests lead to errors?
# The log table includes a column status that indicates the HTTP status code
# that the news site sent to the user's browser.
def error_calculate():
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute("select round(cast((error_count/logcount::float)*100 as numeric) ,2) as Error_Percent, time from log_count, error_log where log_count.date = error_log.time and round(cast((error_count/logcount::float)*100 as numeric) ,2) > 1.0;")
    result=c.fetchall()
    db.close()
    print("\nDays have more than 1% of bad requests: ")
    for item in result:
        print(str(item[0]) + "%" + " - " + str(item[1]))

error_calculate()
