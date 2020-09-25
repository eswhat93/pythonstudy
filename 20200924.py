#해시 - 임의값을 고정 길이로 변환하는 것
# 해쉬테이블-키값의 연산에 의해 직접 접근이 가능한 데이터 구ㅜ조
# 해싱함수 - key에 대해 산술연ㄴ산을 이용해 데이터 위치를 찾을 수 있는 함수

id_name = {1 : 'Dave', 2 : 'David', 3 : 'Anthony'}

# id_name.items()
# dict_items([(1, 'Dave'), (2, 'David'), (3, 'Anthony')])

name_id = {key*10 for key,val in id_name.items()}
#print(name_id)


def str_data():
    data = "hi Dave"
    for item in data:
        yield item


char = iter(str_data())
print(next(char))
print(next(char))

my_list = [1, 2, 3, 4, 5]

my_list_iterator = iter(my_list) # iterator 객체를 만듬
print(next(my_list_iterator)) #next 로 한개씩 뽑을수 있음
