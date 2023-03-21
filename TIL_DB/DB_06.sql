set sql_safe_updates=0;

DROP TABLE users;

-- 문제 1

CREATE TABLE users(
	userId INT AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    city VARCHAR(100),
    country VARCHAR(100),
    email VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(userId)
);


-- 문제 2

INSERT INTO
	users (first_name, last_name, birthday, city, country, email)
VALUES
	('Beemo', 'Jeong', '1000-01-01', ' ', ' ', 'beemo@hphk.kr'),
    ('Jieun', 'Lee', '1993-05-16', 'Seoul', 'Korea', ' '),
    ('Dami', 'Kim', '1995-04-09', 'Seoul', 'korea', ' '),
    ('Kwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea', ' ');

SELECT * FROM users;

-- 문제 3

INSERT INTO
	users (first_name, last_name, birthday, city, country, email)
VALUES
	('koko', 'Park', '1997-09-16', 'Nonsan', 'Korea', ' ');
    
SELECT * FROM users;

-- 문제 4

UPDATE
	users
SET
	first_name = 'Jeong Ill',
    last_name = 'Lee',
    birthday = '1997-02-23',
    city = 'Jeonju',
    country = 'Korea',
    email = 'gone_789@naver.com'
WHERE
	userId = 2;
    
SELECT * FROM users;

-- 문제 5

UPDATE
	users
SET
	country = replace(country , NULL, 'Korea');


    
SELECT * FROM users;

-- 문제 6

DELETE FROM
	users
WHERE
	userId = 1;
SELECT * FROM users;  
  
-- 문제 7

DELETE FROM
	users
WHERE
	first_name = 'Kwangsoo' AND
	last_name = 'Lee';
     
SELECT * FROM users;

-- 문제 8

DELETE FROM
	users
ORDER BY
	created_at
LIMIT 1;
     


SELECT * FROM users;