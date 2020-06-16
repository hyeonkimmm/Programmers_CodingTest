#https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    answer = 0
    current_weight = weight
    dis = [0]*len(truck_weights)
    a,i=0,0
    while True:
        for t in range(i,a):#제일 앞 트럭 부터 대기트럭 전까지
            dis[t]+=1 # 최신 트럭부터 제일 뒤 트럭 거리 증가
            if dis[t]==bridge_length: # 만약 도착했으면
                current_weight+=truck_weights[t] #무게 반납
                i=t+1
        if a<len(truck_weights):        
            if current_weight - truck_weights[a]>=0: 
                #대기 트럭 무게비교
                current_weight -= truck_weights[a] #현재 무게 최신화
                a+=1      # 대기 트럭 번호 최신화
        elif dis[a-1]==bridge_length: #마지막 트럭 건넜으면
            answer+=1
            break
        answer+=1 # 시간 증가
    return answer
bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length,weight,truck_weights))
'''
뭔가 비효율적이면서 효율적인거같다.. 솔직히 잘 모르겠다
'''
