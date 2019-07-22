### Newspaper logs analysis project
==============================


This is an internal reporting tool that produces answers by printing them out in the plain text in the Terminal. The tool produces answers to the following three questions based on the data in the database:

**Question 1:**   
What are the most popular three articles of all time?

**Question 2:**   
Who are the most popular articles authors of all time?

**Question 3:**   
On which days did more than 1% of requests lead to errors?

This tool is a Python program that uses the psycopg2 module to connect to the database.

-----


### How To Install Report Tool:
##### Prepare the software and data
To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

##### The virtual machine
This project makes use of the same Linux-based virtual machine (VM). You will need to install virtual box and vagrant to run this project.


#### Download database
Database was provide by Udacity and available to download here: [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

##### Download or Clone the file into your local machine
To build the reporting tool, you'll need to load the site's data into your local database.


To load the data, cd into the vagrant directory and use the command `psql -d news -f newsdata.sql`.
Here's what this command does:


#### Inside The database
The database includes three tables:

- The authors table includes information about the authors of articles.
- The articles table includes the articles themselves.
- The log table includes one entry for each time a user has accessed the site.  

------


#### PSQL Views Created for Report
Question 2:
```
#article views
CREATE VIEW articles_view AS
	select title, COUNT(log.id) as view
	from articles, log where articles.slug = (replace(path, '/article/', ''))
	GROUP BY articles.title;

#author
CREATE VIEW article_authors AS
	SELECT title, name
	FROM articles, authors
	WHERE articles.author = authors.id;
```

Question 3:
```
#error log
CREATE VIEW error_log AS
	select cast(time as date),
	COUNT(status) as Error_Count from log
	where status like '404%'
	GROUP BY cast(time as date);

#all log
CREATE VIEW logcount
	AS select cast(time as date),
	COUNT(status) as logcount from log
	group by cast(time as date);
```

-----

#### Final Output Result
Check out output.txt file for result.
