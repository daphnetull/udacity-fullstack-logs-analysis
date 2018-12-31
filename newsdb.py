#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Database code for the Logs Analysis Project

import psycopg2

DBNAME = "news"


# What are the most popular three articles of all time?
def get_top_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        select articles.title, count(*) as num
        from articles join log
        on log.path like '%' || articles.slug || '%'
        group by articles.title order by num desc limit 3
    """)
    top_articles = c.fetchall()
    print(top_articles)
    db.close()


# Who are the most popular article authors of all time?
def get_top_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        select authors.name, count(*) as num
        from articles, authors, log
        where articles.author = authors.id
        and log.path like '%' || articles.slug || '%'
        group by authors.name order by num desc
    """)
    top_authors = c.fetchall()
    print(top_authors)
    db.close()


# On which days did more than 1% of requests lead to errors?
def error_analysis():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        create view errorcalc as
        select date(time), count(*) as total,count(*) filter
        (where status != '200 OK') as errors
        from log group by date
    """)
    c.execute("""
        create view percentages as
        select date, (100 * (errors/total::numeric)) as perc
        from errorcalc
    """)
    c.execute("select date,perc from percentages where perc > 1")
    error_percentages = c.fetchall()
    print(error_percentages)
    db.close()

get_top_articles()
get_top_authors()
error_analysis()
