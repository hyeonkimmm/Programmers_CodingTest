--https://programmers.co.kr/learn/courses/30/lessons/59410
-- 코드를 입력하세요
SELECT ANIMAL_TYPE, IFNULL(NAME,'No name')AS NAME, SEX_UPON_INTAKE FROM ANIMAL_INS 
/*
IFNULL 사용법 IFNULL(A,B) NULL이면 B NULL이 아니면 A
*/
