#jupyter

import queue

#배열
# 파이썬에서는 리스트 타입이 배열 기능을 제공하고 있음
# 배열의 장점은? 빠른 접근 가능 / 단점은? 
# 

#9,8,7 순서로 
data = ['asdasfa','sfef','sdawtyy','dfsge']

#s의 빈도수 구하기
count=0
for i in data:
    for j in i:
        if j=='s':
            count +=1


#FIFO
data_queue = queue.Queue()

data_queue.put('a')

print(data_queue.qsize())

data_queue.get()
print(data_queue.qsize())


data_queue2 = queue.LifoQueue()


#우선순위 번호를 같이 넣는다
data_queue3 = queue.PriorityQueue()


data_queue3.put((10,"korea"))
data_queue3.put((1,"a"))
#data_queue3.put("d4d")

print(data_queue3.get())


#멀티태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용함(운영체제 참조)
# 큐의 경우에는 장단점 딱히 없음

#리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현

queue_list = list()


def enqueue(data):
    queue_list.append(data)


def dequeue(data):
    data = queue_list[0]
    del queue_list.get[0]
    return data

for index in range(10):
    enqueue(index)

print(len(queue_list))


#stack
def recursive(data):
    if data<0:
        print("end")
    else:
        print(data)
        recursive(data-1)
        print("returned",data)


recursive(4)

