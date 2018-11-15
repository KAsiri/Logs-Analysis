#!/usr/bin/env python
# # Logs-Analysis project

import psycopg2

# function to open the connection, run the request , close the connection


def query_db(request):
    try:
        conn = psycopg2.connect(database="news")
    except:
        print ("Unable to connect to the database")
    cursor = conn.cursor()
    cursor.execute(request)
    results = cursor.fetchall()
    conn.close()
    return results


# query 1 :
#  What are the most popular three articles of all time?
query1 = """Select articles.title, count(*) as counter
            from log, articles
            where log.status='200 OK'
            and articles.slug = substr(log.path, 10)
            group by articles.title
            order by counter desc
            limit 3;"""

rows = query_db(query1)
print ("\n\t" + "What are the most popular three articles of all time?" + "\n")

for row in rows:
    print(" \"{}\" -- {} views".format(row[0], row[1]))


# query 2:
#  Who are the most popular article authors of all time?
query2 = """Select authors.name, count(*) as counter
            from log, articles, authors
            where log.status='200 OK'
            and authors.id = articles.author
            and articles.slug = substr(log.path, 10)
            group by authors.name
            order by counter desc;"""

rows = query_db(query2)
print ("\n\t"+"Who are the most popular article authors of all time?"+"\n")

for row in rows:
    print(" {} -- {} views".format(row[0], row[1]))

# query 3 :
#  On which days did more than 1% of requests lead to errors?
query3 = """Select time, FaliedPercentage
            from CalPercentage
            where FaliedPercentage > 1;"""

rows = query_db(query3)
print("\n\t"+"On which days did more than 1% of requests lead to errors?"+"\n")

for row in rows:
    print("""  {0:%B %d,%Y} -- {1:.2f}% errors\n""".format(row[0], row[1]))
