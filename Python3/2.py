import itertools
from collections import Counter
def solution(orders, course):
    answer = []
    a=[]
    #알파벳 순으로 정렬
    for i,v in enumerate(orders):
        orders[i]=''.join(sorted(v))
    for index,num in enumerate(course):
        for i,v in enumerate(orders):
            a += list(itertools.combinations(orders[i],num))
        # 카운터로 세주고 딕셔너리로 변환
        b = dict(Counter(a))
        # 최대 value를 가지고있는 dict저장
        max_dic ={}
        # 최대 value
        try:
            max_num = max(b.values())
            if max_num == 1:
                max_num = 0
        except:
            pass
        #최대 키 제외하고 새로운 dict에 추가
        for i,v in b.items():
            if max_num==v:
                max_dic[i]=v
        # 최대 키들 result에 추가
        result = list(max_dic.keys())
        # 키들 answer에 추가
        for i in result:
            answer.append(''.join(i))
        # a 초기화
        a =[]
    return sorted(answer)
