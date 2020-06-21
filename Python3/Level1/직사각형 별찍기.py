#https://programmers.co.kr/learn/courses/30/lessons/12969
a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print('*'*a)
'''
다른 사람의 풀이
print(('*'*a+"\n")*b)
'''
