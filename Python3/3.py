import re
def solution(info, query):
    answer = [0]*len(query)
    for value in info:
        part = list(value.split(' ')) # 참가자 정보 저장
        for i,v in enumerate(query):
            a = list(v.split('and'))
            for num, cond in enumerate(part):
                if num ==4:
                    # 숫자 제외하고 삭제
                    score = re.sub('[^0-9]',"",v)
                    if int(cond) >= int(score): # 만약 이상이면
                        answer[i]+=1
                # 마지막이 아니면
                else:
                    # -일때 아니면 same일때
                    if cond in a[num] or '-' in a[num]:
                        continue
                    else:
                        break
    return answer
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query =["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))
