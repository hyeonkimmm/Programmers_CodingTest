import re
def solution(new_id):
    # 1단계
    answer = new_id.lower()
    # 2단계
    answer = re.sub('[^a-zA-Z0-9\-\_\.]',"",answer)
    # 3단계
    answer = re.sub('\.{2,}',".",answer)
    # 4단계
    answer = re.sub('^\.|\.$',"",answer)
    # 5단계
    if not answer:answer = 'a'
    # 6단계
    if len(answer)>15:
        answer = answer[:15]
        answer = re.sub('\.$',"",answer)
    # 7단계
    while(len(answer)<3):
        answer+=answer[-1]
    return answer
