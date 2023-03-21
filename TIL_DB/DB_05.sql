

-- 문제 1

CREATE TABLE posts (
	postld INT AUTO_INCREMENT,
    tilte VARCHAR(50) NOT NULL,
    content VARCHAR(200) NOT NULL,
    PRIMARY KEY (postld)
);
    
-- 문제 2

ALTER TABLE
	posts
ADD
	(writer VARCHAR(100) NOT NULL,
    created_at DATE);
    
ALTER TABLE
	posts
MODIFY
	writer VARCHAR(100);   
    
    
-- 문제 3   
   
ALTER TABLE
	posts
MODIFY
	content TEXT;
    
-- 문제 4

ALTER TABLE
	posts
DROP COLUMN
	writer;
    
-- 문제 5

DROP TABLE posts;

-- 문제 6

CREATE TABLE posts(
    postld INT AUTO_INCREMENT,
    tilte VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    writer VARCHAR(20) NOT NULL,
    created_at DATE,
    PRIMARY KEY (postld)
);
    
-- 문제 7

DROP TABLE posts;
    
SHOW COLUMNS FROM posts;