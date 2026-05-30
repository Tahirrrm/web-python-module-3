
CREATE TABLESPACE ts_win LOCATION 'C:\PostgreSQL\data\tablespace';
SELECT *
FROM pg_tablespace
WHERE spcname = 'ts_win';

CREATE DATABASE Birds
    OWNER = postgres
    ENCODING = 'UTF8'
    TABLESPACE = ts_win;
SELECT datname FROM pg_database WHERE LOWER(datname) = 'birds';

SELECT * FROM pg_stat_activity WHERE datname = 'Birds';
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'birds'
  AND pid <> pg_backend_pid();

SELECT pid, usename, state
FROM pg_stat_activity
WHERE datname = 'birds';

ALTER DATABASE birds RENAME TO Cats;

SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'Cats'
  AND pid <> pg_backend_pid();

DROP DATABASE Cats;


CREATE TABLE vegetables_and_fruits (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(20) NOT NULL CHECK (type IN ('овощ', 'фрукт')),
    color VARCHAR(50),
    calories INTEGER NOT NULL CHECK (calories >= 0),
    description TEXT
);

INSERT INTO vegetables_and_fruits (name, type, color, calories, description)

VALUES
    ('Яблоко', 'фрукт', 'красный', 53, 'Сладкий фрукт, богат витаминами.'),
    ('Морковь', 'овощ', 'оранжевый', 40, 'Сочная морковь, источник бета‑каротина.'),
    ('Банан', 'фрукт', 'жёлтый', 92, 'Тропический фрукт, содержит калий.'),
    ('Огурец', 'овощ', 'зелёный', 16, 'Низкокалорийный овощ, идеален для салатов.'),
    ('Свёкла', 'овощ', 'тёмно‑красный', 44, 'Корнеплод с землистым вкусом, полезен для крови.');

SELECT * 
FROM vegetables_and_fruits;

SELECT * 
FROM vegetables_and_fruits
WHERE type = 'овощ';

SELECT * 
FROM vegetables_and_fruits
WHERE type = 'фрукт';

SELECT name
FROM vegetables_and_fruits;

SELECT DISTINCT color
FROM vegetables_and_fruits
WHERE color IS NOT NULL;

SELECT * 
FROM vegetables_and_fruits
WHERE type = 'фрукт'
  AND color = 'жёлтый';

SELECT * 
FROM vegetables_and_fruits
WHERE type = 'овощ'
  AND color = 'оранжевый';



SELECT *
FROM vegetables_and_fruits
WHERE type = 'овощ'
	AND calories < 40;

SELECT *
FROM vegetables_and_fruits
WHERE type = 'фрукт'
	AND calories BETWEEN 50 AND 100;

SELECT *
FROM vegetables_and_fruits
WHERE type = 'овощ'
	AND name ILIKE '%морковь';

SELECT *
FROM vegetables_and_fruits
WHERE description ILIKE '%корнеплод%';

SELECT *
FROM vegetables_and_fruits
WHERE color IN ('желтый','красный');

SELECT COUNT (*) AS vegetable_count
FROM vegetables_and_fruits
WHERE type ='овощ';

SELECT COUNT (*) AS fruit_count
FROM vegetables_and_fruits
WHERE type ='фрукт';

SELECT COUNT (*) AS count_by_color
FROM vegetables_and_fruits
WHERE color ='красный';

SELECT color, COUNT (*) AS count
FROM vegetables_and_fruits
GROUP BY color 
ORDER BY count DESC;

SELECT color, COUNT (*) AS min_count
FROM vegetables_and_fruits
GROUP BY color 
ORDER BY min_count ASC
LIMIT 1;

SELECT color, COUNT (*) AS max_count
FROM vegetables_and_fruits
GROUP BY color 
ORDER BY max_count DESC
LIMIT 1;

SELECT MIN(calories) AS min_calories
FROM  vegetables_and_fruits

SELECT MAX(calories) AS max_calories
FROM  vegetables_and_fruits

SELECT AVG(calories) AS avg_calories
FROM  vegetables_and_fruits

SELECT *
FROM vegetables_and_fruits
WHERE type = 'фрукт'
ORDER BY calories ASC
LIMIT 1;

SELECT *
FROM vegetables_and_fruits
WHERE type = 'фрукт'
ORDER BY calories DESC
LIMIT 1;




