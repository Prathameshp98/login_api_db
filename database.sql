CREATE TABLE databases(user_name varchar,password varchar);

select * from databases;
  
SELECT user_name FROM databases WHERE user_name = 'unknown'; 

SELECT password FROM databases WHERE user_name = 'prathamesh' AND password='f3b7e5d3eb074cde5b76e26bc0fb5776';

DELETE FROM databases WHERE user_name='unknown';