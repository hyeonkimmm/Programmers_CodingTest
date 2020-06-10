#https://programmers.co.kr/learn/courses/30/lessons/12901
def solution(a, b):
    Day_Week=['FRI','SAT','SUN','MON','TUE','WED','THU']
    Day_Month=[31,29,31,30,31,30,31,31,30,31,30,31]
    num = sum(day_Month[:a-1])+b-1
    answer = Day_Week[num%7]
    return answer
'''
다른 사람 코드
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]
나랑 아예 똑같은데 코드를 충분히 줄여서 할 수 있다
import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]
datetime 함수 활용한게 좋아보인당
.split()활용해서 직접 초기화할때도 좀 더 편해보여서 다음엔 참고해야겠다.

'''
