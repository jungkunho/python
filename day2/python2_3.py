#for 변수 in 리스트(튜플 or 문자열):
#    수행문1

a = [1, 2, 3]

for i in a:
    print(i)
#i는 list의 구성요소
# 아래의 경우는 dictionary를 의미함   
list =[{"name":"가"}, {"name":"나"}, {"name":"다"}]
for i in list:
        print(list[i]["name"])
        
list2 =[{"name":"홍길동", "score":40}, {"name":"황진희", "score":60}]
for i in list2:
        print(list[i]["name"] +"의 점수는 " + str(i["score"]))
        
index = 1
list3 =[{"name":"홍길동", "score":40}, {"name":"황진희", "score":60}]
for i in list3:
        print(list[index]["번째"] +"의 점수는 " + str(i["score"]))
        index -index + 1
#50점 이상인 사람은 합격 출력하기
        index = 1
for i in list

