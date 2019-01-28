# Log_Analysis_1_Udacity

By Prasanna Raj Mallipudi

### Project Overview

For this project, I was tasked to create a reporting tool that prints out reports (in plain text) based on the data in a database.
This reporting tool is a Python program using the `psycopg2` module to connect to the database.

### Assignment

The reporting tool needed to answer the following questions::
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### How to Run the Code
This section will describe the SQL views I created for the code to function properly and how to run the program.

### Required SQL Views
This program uses SQL views.

------> views.sql

first run the and execute views.

*For Assignment 1:*
`CREATE VIEW articles_view AS SELECT title,author,count(title) AS views
FROM articles,log WHERE log.path LIKE concat('%',articles.slug) GROUP BY articles.title,articles.author ORDER BY views DESC limit 3;`

*For Assignment 2:*
`CREATE VIEW authors_view AS SELECT name,sum(articles_view.views) AS total
FROM articles_view,authors WHERE authors.id=articles_view.author
GROUP BY authors.name ORDER BY total DESC limit 3;`

*For Assignment 3:*
`CREATE VIEW log_view AS SELECT totals_view.date as date,((100.00*errors)/(total_errors)) AS percentage_errors FROM errors_view natural join totals_view
WHERE errors_view.date=totals_view.date GROUP BY totals_view.date,percentage_errors order by percentage_errors desc;`

`CREATE VIEW errors_view AS SELECT date(time),count(*) as errors FROM log WHERE log.status like concat('404 NOT FOUND') GROUP BY date(time) ORDER BY errors desc;`

`CREATE VIEW totals_view AS SELECT date(time),count(status) AS total_errors FROM log GROUP BY date(time) ORDER BY total_errors desc;`

### Running the Program

*These instructions assume you have the Udacity-provided Virtual machine and Udacity-provided database*
or
Crete your own Virtual OS

##First, you'll need to create the views listed above:
1. Within the VM, navigate to `cd /vagrant`
2. Run `psql`
3. Connect to the database `\c news`
4. Enter the views listed above
   psql -d news -f views.sql
5. Exit `psql`

##With those view created, run the `LogAn.py` file:
1. Place the `LogAn.py` file within the same directory as the VM and SQL file provided by Udacity.
2. If you haven't already, launch the VM:
	a. `vagrant up` -- only required once
	b. `vagrant ssh` -- required each and every time
3. Within the VM, navigate to `cd /vagrant`
4. Goto Project folder `PJ3`
5. Execute the file `python LogAn.py`

### Output::---

Heepe Connected..!

The most popular three articles::
Candidate is jerk, alleges rival -- 338647

Bears love berries, alleges bear -- 253801

Bad things gone, say good people -- 170098

The most popular article authors::
Rudolf von Treppenwitz -- 338647

Ursula La Multa -- 253801

Anonymous Contributor -- 170098

On which day did more than 1%  of errors found::
2016-07-17 -- 2.3%
