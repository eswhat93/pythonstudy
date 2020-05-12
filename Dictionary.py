from copy import copy

a= {"name" : "LEe", "age":"28"}


#for K in a.keys():
 #   print(K) 

list(a.keys()) #key 리스트만들기
a.values() #value 리스트만들기
a.items() #key value 쌍 얻기
a.clear # 쌍 다 지우기
a.get('name') #key 로 value 얻기
a.get('nam','age') #해당값 없으면 default값 가져오기
'name' in a #True / False


#집합자료형
s1 = set([1,2,3])
s2 = list(set("Tesst")) #변수에 담으려면 리스트형이나 튜플로 변형
s2.sort()
#s1&s2 #교집합
#s1 | s2 #합집합
#s1 - s2 #차집합

s3 = set([1,2,3])
s3.add(5)
s3.remove(5)

s4 = copy(s3)
print(s4 is s3) #false


#변수만들기

a=b=1
a=3
b=5
a, b = b,a