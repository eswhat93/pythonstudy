# 선택정렬 
# 코딩 테스트를 준비하고.... 구조도준비하고....웹도 만들어봐야하느디 킄ㅋ킄킄크ㅡㅡ크크크ㅡ크ㅡ크크ㅡ크ㅡ카ㅡㅏㅢ아리ㅏ

#데이터가 두개일때 동작하는 선책정렬 알고리즘

#배우기전
data = [2,5,1,3,8,7]
 
def sel(dataList): 
    for i in range(len(dataList)-1):
        index = dataList.index(min(dataList[i:]))
        dataList[i],dataList[index] = min(dataList[i:]), dataList[i]
        print(dataList)
    return data

#print(sel(data))

#배우고나서
#데이터가 두개일때, 세개일때, 네개일때 짜면서 보완
#값대입해보고 알고리즘 구현 시작
#for stand in range(len(dataList) -1)로 반복
#lowest = stand 로 놓고
#for num in range(stand, len(dataList)) stand 이후부터 반복
    #내부 반복문 안에서 dataList[lowest] > dataList[num] 이면 lowest = num
#dataList[num],dataList[lowest]=dataList[lowest],dataList[num]

data2 = [2,5,1,3,8,7]
#print("#############")
def selection_sort(data_list):
    for stand in range(len(data_list) - 1):
        lowest = stand
        for num in range(stand, len(data_list)):
            if data_list[lowest] > data_list[num]:
                lowest = num
        data_list[stand], data_list[lowest] = data_list[lowest], data_list[stand]
        print (data_list)
    return data_list

#print(selection_sort(data2))

#재귀용법
#함수 안에서 동일한 함수를 호출하는 형태/ 여러알고리즘 작성시 사용된다고함
#2! = 1X2
#3! = 1X2X3
#규칙 = > n! = n X (n-1)!
#함수(n)은 n>1 이면 return nX함수(n-1)
#함수(n)은 n=1이면 return n


def factorial(n):
    if n > 1 :
        return n * factorial(n-1)
    else :
        return n

#for num in range(10):
#    print(factorial(num))

#재귀 용법을 활용한 프로그래밍 연습
def multiple(data):
    if data <=1:
        return data
    return data * multiple(data-1)

#print(multiple(10))

#숫자가 들어있는 리스트/ 리스트의 합리턴하는 함수 만들기
import random
data = random.sample(range(100),10)
print(data)
def total(d):
    first = 1
    for i in range(len(d)-1):
        first = first + d[i]
        print(d[i])
    return first

#print(total(data))

#20200515
#재귀함수 이용해서 리스트의 합 구하기
def total2(data):
    if len(data)==1 :
        return data[0]
    return data[0] + total2(data[1:])

print(total2([3,4,5,6]))

#회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 이야기헙니다. 
#회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드세요
#슬라이싱은 a[start : end : step]

#20200518
string = "MOTOM"

#배우기전
def pal(data):
    cnt = 0
    for i in range((len(data)-1)):
        if data[i] == data[len(data)-i-1]:
            print(data[i], " = ", data[len(data)-i-1])
        else:
            print("dsd")
            break
    return "회문"

print(pal(string))

#배운후
def recursive(data):
    if len(data) <=1 :
        return True

    if data[0] == data[-1]:
        #print(data[1:-1])
        return recursive(data[1:-1])

    else:
        return False

print(recursive(string))


#정수 n 
#배우기전
def t(n):
    print(n)
    if n<=1:
        return 1
    if n%2 == 0 :
        n = n/2
    else :
        n = (3*n) + 1
    t(n)
    return n

#t(int(input()))

#배운후
def func(data):
    print(data)
    if data == 1 :
        return

    if data%2 == 0:
        return func(int(data / 2))
    else:
        return func(3*data +1)
#func(int(input()))

