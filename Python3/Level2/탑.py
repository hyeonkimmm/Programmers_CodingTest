#https://programmers.co.kr/learn/courses/30/lessons/42588
def solution(heights):
    answer = []
    heights = list(reversed(heights))
    for i,v in enumerate(heights):
        for a,val in enumerate(heights[i+1:]):
            if v>=max(heights[i+1:]):
                answer.append(0)
                break
            elif v<val:
                index = len(heights)-i-a-1
                answer.append(index)
                break
    answer.append(0)
    return list(reversed(answer))
'''
일단 억지로 풀긴 했는데 좀 비효율적인것 같긴하다
다른 사람의 풀이
def solution(h):
    ans = [0] * len(h)
    for i in range(len(h)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if h[i] < h[j]:
                ans[i] = j+1
                break
    return ans
    
def solution(heights): # -> O(N) 풀이
    stack = []
    stack.append(0)
    max_pos = 1
    max_val = heights[0]

    for i in range(1,len(heights)):
        if heights[i] >= max_val:
            stack.append(0)
            max_pos = i+1
            max_val = heights[i]
        if heights[i] < max_val:
            stack.append(max_pos)
        if heights[i] < heights[i-1]:
            max_pos = i
            max_val = heights[i-1]
            stack.pop()
            stack.append(max_pos)

    return stack
알게 된 점
1. reversed 사용하면 객체자체가 리스트가 아님
2. range는 생각보다 엄청 유용하다(굳이 reversed 안써도 될 때가 많음)
  range(start,stop,bacth)
  start -> 여기부터 시작
  stop -> 여기 앞까지
  batch -> 이만큼
  ex) range(3 , -1 , -1)
    3부터 -1 앞까지 -1만큼
    3 , 2 , 1 ,0 이런식으로 실행 됨
'''
