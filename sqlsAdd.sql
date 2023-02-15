INSERT INTO currentsqls VALUES ( md5('SELECT * FROM CCNTBL'), 'SELECT * FROM CCNTBL', 'pending', False, 300);
INSERT INTO currentsqls VALUES ( md5('SELECT * FROM HIPAA'), 'SELECT * FROM HIPAA', 'pending', False , 400);
INSERT INTO currentsqls VALUES ( md5('SELECT * FROM CCNTBL where CCN = "?"'), 'SELECT * FROM CCNTBL where CCN = "?"', 'pending', False , 300);
INSERT INTO currentsqls VALUES ( md5('SELECT name, description FROM products WHERE category = "Gifts"'), 'SELECT name, description FROM products WHERE category = "Gifts"', 'pending', False , 300);
INSERT INTO currentsqls VALUES ( md5('SELECT name, description FROM products WHERE category = "Gifts" UNION SELECT username, password FROM users--'), 'SELECT name, description FROM products WHERE category = "Gifts" UNION SELECT username, password FROM users--', 'pending', False, 300);
