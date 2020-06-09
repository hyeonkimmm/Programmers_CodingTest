--https://programmers.co.kr/learn/courses/30/lessons/59040
-- 코드를 입력하세요
SELECT ANIMAL_TYPE , COUNT(ANIMAL_TYPE) AS count FROM 
(SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_TYPE asc LIMIT 1000000)AS RESULT GROUP BY RESULT.ANIMAL_TYPE

/*
이 문제는 상당히 간단해 보였으나 풀어보니까 계속 틀렸다고 나와서 화가 많이 났다.
문제:
동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이가 개보다 먼저 조회해주세요.
고양이는 2마리, 개는 1마리 들어왔습니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.
ANIMAL_TYPE	  count
Cat	            2
Dog             1
이런식으로 나오면 되는거라 간단하게
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count FROM ANIMAL_INS GROUP BY ANIMAL_TYPE
이렇게 풀면 될 줄 알았는데
나도 정확하게는 모르지만 GROUP BY 특성상 데이터베이스 맨위에 조회되는 칼럼 기준으로 GROUP BY 되는 것 같다 예를들어 Dog 가 먼저 조회되면
Cat이 먼저 들어온게 아니기 때문에 문제가 생기는 듯
그래서 찾아보니깐 ORDER BY를 사용하면 된다는데 GROUP BY가 ORDER BY 보다 먼저 값이 먹혀서 또 안된다고함 --> 서브쿼리 사용하라고함
그래서 서브쿼리 사용해서
SELECT ANIMAL_TYPE , COUNT(ANIMAL_TYPE) AS count FROM 
(SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_TYPE asc)as x GROUP BY x.ANIMAL_TYPE
뭐 이런식으로 했더니 또 안된다!!!
찾아보니까 서브쿼리에서 ORDER BY 값이 안먹힘 뭐 ORDER BY 이후에 다시 뭔 값을 기준으로 한다고 했다나 뭐라나..
쓰다보니까 일기가 됐는데 결국에 MY SQL 에선 LIMIT 값을 주게 되면 잘 먹힌다고 함.. Oracle에선 모름

요약
1. 간단할 줄 알았는데 Cat 값을 정렬해야 풀림
2. ORDER BY 보다 GROUP BY가 먼저이기 떄문에 서브쿼리를 사용
3. 서브쿼리 내에서 ORDER BY 가 실행되더라도 적용이 안됨
4. MY SQL에서 LIMIT 설정시 적용 가능. Oracle에서는 모르겠음
*/
