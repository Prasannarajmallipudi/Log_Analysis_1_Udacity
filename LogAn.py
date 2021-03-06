#!/usr/bin/env python

import psycopg2
import time
# con=psycopg2.connect (database="news")
try:
    # connecting the data base using postgresql
    con = psycopg2.connect(database="news")
    print("Heepe Connected..!")
    curr = con.cursor()
except Exception as ex:
    print("Ooh error :(", ex)
# top 3 Articles


def articles_view():
    curr.execute("select title,views from articles_view limit 3;")
    arti = curr.fetchall()
    print("The most popular three articles::")
    for art_v in arti:
        print art_v[0], "---", art_v[1]

# top most  Authors


def authors_view():
    Av = '''SELECT name,sum(articles_view.views) AS views
    FROM authors_view,articles_view
    WHERE authors_view.title = articles_view.title
    GROUP BY name ORDER BY views desc limit 4;'''
    curr.execute(Av)
    arti = curr.fetchall()
    print("The most popular article authors::")
    for art_v in arti:
        print art_v[0], "--", art_v[1]


# Error Log display


def log_view():
    curr.execute("select * from log_view where percentage_errors > 1 ;")
    arti = curr.fetchall()
    print("On which day did more than 1%  of errors found::")
    for log in arti:
        print log[0], "--", '%0.1f%%' % (log[1])

articles_view()
authors_view()
log_view()
curr.close()
con.close()
