# 완전탐색, 재귀, 2진탐색, BFS, 순열




#k= input().split()
#v= input().split()
#print(dict(k,v))

a = [38, 21, 53, 62, 19]

#print(a.__getitem__(1))


#a = input()
#b = input()
#print(a[1::2]+b[0::2])



#딕셔너리 만들기
#딕셔너리 = {}
#딕셔너리 = dict()
#딕셔너리 = dict(zip([키1, 키2], [값1, 값2]))
#딕셔너리 = dict(키1=값1, 키2 = 값2)
#딕셔너리 = dict([(키1,값1), (키2, 값2)])
#딕셔너리 = dict({키1:값1, 키2,값2})
#키는 딕셔너리를 만들고나면 문자열로 바뀐다 
#딕셔너리는 해시 기법을 이용해서 데이터를 저장 키-값 형태


#a=input().split()
#b=input().split()
#c = dict(zip(a,b))
#print(c)


a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
print(map(lambda x, y: x * y, a, b))


#파이썬 이론을 떼고 파이썬으로 알고리즘을 풀면서 기초를 익히고 바로 프로젝트 들어가고
# 강의도 사서 들으면서 프로젝트 해보고 프론트 쪽도 공부만ㄹ힝ㄴ멍리ㅏㅓㄴ; 러시발
import itertools

def solutions(numbers):
    numbers = [str(i) for i in numbers]
    answer=list(map(''.join, itertools.permutations(numbers)))
    print(answer)

    answer.sort()
    answer = max(answer)    
    return answer
# 시간초과


def solution(numbers):
    numbers = list(map(str, numbers))
    
    numbers.sort(key=lambda x:x*3, reverse=True)
    print(numbers)
    # 666[0] 101010[0] 222[0] 아스키숫자로 바꿔서 비교한다고함....같으면 다음 인덱스도 비교한다고함
    return str(int(''.join(numbers)))

n=[6,10,2]
print(solution(n))


