## Itertools.cycle
>Itertools 모듈은 반복 가능한 데이터 원소들을 처리하는 데 유용한 많은 함수와 제네레이터가 포함되어 있다.
while문을이용해 반복하면서 데이터 원소들을 처리할수는 있지만 itertools 모듈을 이용하면 간단하게 구현이 가능하다.


cycle(iterable)
iterable에서 요소를 반환하고 각각의 복사본을 저장하는 반복자를 만든다.

반복 가능한 요소가 모두 소모되면 저장된 사본에서 요소를 리턴한다.

반복 가능한 요소가 모두 소모될때까지 무한정 반복한다.

예를들어 list1 = [ 1 , 2 , 3 , 4 ] , list2 = [ ‘a’ , ’b’ , ’c’ , ’d’ , ’e’ , ’f’ , ’g’ ] 가 있다고 할때

list1, list2 를 zip을 이용해 엮으려고 하면 list1 이 list2 보다 작기때문에 다시 처음으로 돌아가서 반복을 해야한다. 

이것을 cycle 함수를 사용해 간단하게 구현을 할수 있다.
<pre>
<code>
import itertools
list1 = [1,2,3,4]
list2 = ['a','b','c','d','e','f','g']
for list1_item , list2_item in zip(itertools.cycle(list1) , list2) :    

    print((list1_item),list2_item))
    
''''
결과
''''
1 a
2 b
3 c
4 d
1 e
2 f
3 g
</pre>
</code>
