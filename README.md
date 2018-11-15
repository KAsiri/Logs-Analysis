
## Logs Analysis Project
a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Project Requirements:-
- Project follows good SQL coding practices: Each question should be answered with a single database query.  
- The code is error free and conforms to the PEP8 style recommendations.
- The code presents its output in clearly formatted plain text.
- The Code should show results answer three Questions:
    * What are the most popular three articles of all time?
    * Who are the most popular article authors of all time?
    * On which days did more than 1% of requests lead to errors? 

## Setup Requirements:-
- Python  (https://www.python.org)
- Psycopg2 v2.7.5  (http://initd.org/psycopg/download/)
- PostgreSQL v9.5.14  (https://www.postgresql.org/download/)
- Vagrant v2.2.0  (https://www.vagrantup.com/downloads.html) 
- VirtualBox v5.1.38  (https://www.vagrantup.com/downloads.html)

## Instructions:-
- Create empty folder that will be project main folder for example (Logs-Analysis) here will be your python file.
- Download "Vagrantfile" (https://goo.gl/wLBxDA) and place it inside recently created folder.
- Run "vagrant up" command inside folder using any CLI (cmd,pwoershell,bash, git bash ...etc) and wait till it finish.
- Download datafile "newsdata.sql" (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
- Unzip "newsdata.zip" and copy "newsdata.sql" to our project folder.
- Run "vagrant ssh" inside project folder.
- Cd to vagrant using command "cd /vagrant". 
- Fill database from "newsdata.sql" file using this command "psql -d news -f newsdata.sql".
- Now VM machine and database with data is ready.

## Tips:-
- You can connect and use "news" database by this command "psql -d news" (make sure you run this command in vagrant VM).
- After you connect to database "news" you can run this command "\dt" to see all tables.
- You can see table detail by this command "\d log" "log" is the table name.
- While you connected to "news" database you can preform queries.
- You can see sample data from table by using this sql query "SELECT * FROM log LIMIT 5;" (do not forget ';' at the end of query) to execute it.
- To close connection with "news" database and return to vagrant VM use press "Ctrl+Z".

## Views used
#### statusView
````sql
CREATE VIEW statusView AS
SELECT time ::date,
       status
FROM log;
````

#### Falied
````sql
CREATE VIEW Falied AS
SELECT time,
       count(*) AS counter
FROM statusView
WHERE status = '404 NOT FOUND'
GROUP BY time;
````

#### statusAll
````sql
CREATE VIEW statusAll AS
SELECT time,
       count(*) AS counter
FROM statusView
GROUP BY time;
````

#### CalPercentage
````sql
CREATE VIEW CalPercentage AS
SELECT statusAll.time,
       statusAll.counter AS counterAll,
       Falied.counter AS counterFailed,
       Falied.counter::double precision/statusAll.counter::double precision * 100 AS FaliedPercentage
FROM statusAll,
     Falied
WHERE statusAll.time = Falied.time;
````
