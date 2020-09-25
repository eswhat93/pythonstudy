# 해쉬테이블 
# 1. chaining 기법 - 개방 해슁 또는 open hasing 기법중 하나: 해쉬테이블 저장공간 외의 공간을 활용하는 기법(링크드리스트)


hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
               hash_table[hash_address][index][1] = value
               return hash_table[hash_address].append([index_key, value])
            else:
                hash_table[hash_address] = [[index_key,value]] 

def read_data(data):
    hash_address = hash_function(get_key())

print(save_data(1, 2))