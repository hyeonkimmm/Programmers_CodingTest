#https://programmers.co.kr/learn/courses/30/lessons/49993
import copy
def solution(skill, skill_trees):
    a=copy.deepcopy(skill)
    answer = 0
    for i in skill_trees:
        for j in i:
            if j in a:#주요 스킬트리값이 리스트에 있을 때
                if 0==a.index(j):#순서대로 찍는지
                    a=a[1:]# 다음순서로 초기화
                    if j ==i[-1]:#주요 스킬이 마지막일때
                        answer+=1
                        a=copy.deepcopy(skill)
                else: # 순서를 어겼을 때
                    a=copy.deepcopy(skill)
                    break
            elif j ==i[-1]: #주요 스킬이 아니고 마지막일때
                answer+=1
                a=copy.deepcopy(skill)
                continue
            else: #주요 스킬도 아니고 마지막도 아닐 때
                continue
    return answer
'''
내가봐도 너무 복잡하다 풀려고 하다보니 파이썬은 깊은 복사 얕은 복사가 있다는 것을 알게 되었다
뭔가 딱 스택/큐 느낌으로 푸는건 알겠는데 어떻게 구현할지 애매했던 것 같다
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
굳이 깊은복사 그렇게 할 필요 없이 pop이랑 비교해서 아니면 바로 break 하면 된다. 어차피 주요 스킬 아니면 pop하지도 않고
pop 하더라도 skill 문자열에는 전혀 지장이 안가는..(주소값을 안 건드는 것 같다)
다시 초기화 할 경우에는 pop을 사용하면 되겠다
for else 구문도 배움
for 가 다 끝났는지 찾기 애매할 때가 많은데 저렇게 하면 되는듯
'''
