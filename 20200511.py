########알고리즘
#버블정렬 - 두 인접한 데이터를 비교해서 앞에 있는 데이터가 뒤에 있는 데이터보다 크면 자리를 바꾸는 정렬 알고리즘
#n개의 리스트가 있는경우 최대 n-1번의 로직을 적용한다
#로직을 1번 적용할때마다 가장 큰 숫자가 뒤에서부터 1개씩 결정된다

a = [1,5,6,2]

def bubble_sort(data):
    swap=0
    for num in range(len(a)):
        for index in range(len(a) - num -1):
            if a[index] > a[index + 1]:
                a[index],a[index+1] = a[index+1],a[index]
                swap +=1
        if swap == 0: break
    return data

print(bubble_sort(a))

#삽입정렬
#20200512 이지롱
a=[2,1,5,3,6]
#배우기 전 코드
def insert_sort(data):
    swap=0
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j]>data[i+1]:
                data[i+1],data[j] = data[j],data[i+1]
                swap +=1
        if swap ==0: break
    return data

#print(insert_sort(a))

#https://visualgo.net/en/sorting

#삽입정렬은 두번째 인덱스부터 시작
#해당인덱스 (key값) 앞에 있는 데이터(B)부터 비교해서 key값이 더 작으면 B를 key 뒤로 보냄(B값을 뒤 인덱스로 복사)
#이를 key값이 더 큰 데이터를 만날때까지 반복, 그리고 큰 데이터를 만난 위치 바로 뒤에 key값을 이동
###range(시작, 끝, 스텝)

#배우고나서 코드
def insert_sort2(data):
    for index in range(len(data)):
        key = data[index]
        for index2 in range(index,0,-1):
            if data[index2-1]>key :
                data[index2-1],data[index] = data[index],data[index2-1] 
            else :
                break
    return data
print(insert_sort2(a))


# 큐 (QUEUE)
# 가장 먼저 넣은 데이터를 가장 먼저 꺼낸다 FIFO = first in first out
import queue

data_queue = queue.Queue()

data_queue.put("funcoding")
data_queue.put("1")

print(data_queue.qsize())

data_queue.get()

#Last in first out
data_queue2 = queue.LifoQueue()

#key, value값 넣고 뽑기
data_queue3 = queue.PriorityQueue()

data_queue3.put((10, "korea"))
data_queue3.put((5, 1))
data_queue3.put((15, "china"))

#큐가 어디 많이쓰이나? 멀티태스킹을 위한 프로세스 스케쥴링 방식 구현 위해 (운영체제)
