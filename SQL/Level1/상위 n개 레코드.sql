--https://programmers.co.kr/learn/courses/30/lessons/59405
-- 코드를 입력하세요
SELECT NAME FROM ANIMAL_INS WHERE DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS)
/*
마땅히 생각나는게 없어서 서브쿼리로 풀었다
다른 사람 풀이
MYSQL
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1
ORACLE
SELECT * FROM (SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME) WHERE ROWNUM = 1
*/
