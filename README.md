# Logs Analysis Project

This is the first project for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) program. 

A [PostgreSQL](https://www.postgresql.org/) database of an imaginary news website is provided with the following 3 tables: 
- Articles
- Authors
- Log

Students are assigned to write three seperate advanced SQL queries and execute them in Python using [Psycopg](http://initd.org/psycopg/) as a PostgreSQL adapter.

## To run project

1. Clone this repo.  
2. Download and unzip the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
3. Download and install [VirtualBox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/) to create a virtual Linux environment.  
4. Download and install PostgreSQL: https://www.postgresql.org/download/
5. Download and install Psycopg: http://initd.org/psycopg/download/
6. Go inside the `vagrant` folder, then type `vagrant up` followed by `vagrant ssh` in your command line
7. The file downloaded is called `newsdata.sql`. Put this file into the `vagrant` directory
8. To load the data, type `psql -d news -f newsdata.sql` inside the `vagrant` directory
8. To test your own SQL statements, type `psql news`
9. Run newsdb.py by typing `python newsdb.py` or `python3 newsdb.py` if using Python3 in your command line.  

## Views

2 views are created in the execution of the 3rd query using the `create view` statement:
-errorcalc
-percentages

`create view errorcalc as
select date(time), count(*) as total,count(*) filter
(where status != '200 OK') as errors
from log group by date`

`create view percentages as
select date, (100 * (errors/total::numeric)) as perc
from errorcalc`

## Dependencies

- [PostgreSQL](https://www.postgresql.org/)
- [Psycopg](http://initd.org/psycopg/)
- [VirtualBox](https://www.virtualbox.org/)
- [Vagrant](https://www.vagrantup.com/)

