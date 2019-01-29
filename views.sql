CREATE VIEW articles_view AS
SELECT title, count(log.id) as views
FROM articles, log
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
         articles.author
ORDER BY views desc limit 3;


CREATE VIEW authors_view AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;


CREATE VIEW log_view AS
 SELECT totals_view.date as date,((100.00*errors)/(total_errors))
 AS percentage_errors FROM errors_view natural join totals_view
 WHERE errors_view.date=totals_view.date GROUP BY
  totals_view.date,percentage_errors order by percentage_errors desc;



CREATE VIEW errors_view AS
SELECT date(time),count(*) as errors
FROM log WHERE log.status like concat('404 NOT FOUND')
GROUP BY date(time) ORDER BY errors desc;




CREATE VIEW totals_view AS
SELECT date(time),count(status) AS
total_errors FROM log GROUP BY date(time)
ORDER BY total_errors desc;
