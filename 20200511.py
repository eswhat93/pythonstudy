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
a=[2,1]
def insert_sort(data):
    swap=0
    for i in len(data)-1:
        for j in len(data)-1: