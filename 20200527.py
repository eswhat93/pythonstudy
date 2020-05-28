def solution(land):
    answer = 0
    maxl = 0
    indexl = 0
    
    for i in range(len(land)):
        if i != 0:
            land[i][indexl] = 0
            
        maxl = max(land[i])
        indexl = land[i].index(maxl)
        print(maxl)
        answer += maxl
            
    return answer

a = [[1,2,3,5],[5,6,7,8],[4,3,2,1],[0,1,0,0]]

#print(solution(a))

#

def solution(land):

    for i in range(1,len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(land[len(land)-1])

def solution2(m, n, board):
    answer = 0

    for i in range(len(board)):
        
        for k in range(len(board[i])):
            print(board[i][k])
    return answer

#print(solution2(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))#14
#6	6	[TTTANT, RRFACC, RRRFCC, TRRRAA, TTMMMF, TMMTTJ]	15


# 카카오 기출문제 비밀지도
# 지도는 한 변의 길이가 n 인 정사각형 배열, 각 칸의 공백 또는 벽# 두 종류로 이뤄져있음
# 두 배열을 합해 하나의 지도를 만든다

def ka(n,arr1,arr2):
    test=""
    answer=[]
    answer2=[]
    answer3=[]
    for k in range(len(arr1)):
        for i in range(n):
            if arr1[k]%2==0:
                test += "0" 
            else:
                test += "#"
            arr1[k] = int(arr1[k]/2)
        answer.append(test[::-1])
        test=""
    print(answer)
    for k in range(len(arr2)):
        for i in range(n):
            if arr2[k]%2==0:
                test += "0" 
            else:
                test += "#"
            arr2[k] = int(arr2[k]/2)
        answer2.append(test[::-1])
        test=""
    print(answer2)
    for i in range(5):
        for k in range(5):
            if answer[i][k] == answer2[i][k] == "0":
                test +=" "
            else:
                test +="#"
        answer3.append(test[::-1])
        test=""
    return answer3    
#비트 연산을 활용할 수 있는가?
def kabin(n,arr1,arr2):
    answer =[]
    for a1, a2 in zip(arr1, arr2):
        a= str(bin(a1 | a2))[2:]
        a= '0'*(n-len(a)) +a
        a= a.replace('1',"#")
        a= a.replace('0'," ")
        answer.append(a)
    
    return answer

n=5
arr1 =[9, 20, 28, 18, 11]
arr2 =[30, 1, 21, 17, 28]
#print(ka(n, arr1, arr2))
print(kabin(n, arr1, arr2))

#다트 게임 점수로직대로 계산하기
def dart(score):
    sol =[]
    test=[]
    array1 = ['S', 'D', 'T', '*', '#']
    for i in score:
        if i in array1:
            sol.append(i)
        else:
            sol.append(int(i))

    for i in range(len(sol)):
        if sol[i] == 'S':
            test.append(sol[i-1] **1)
        if sol[i] == 'D':
            test.append(sol[i-1] **2)
        elif sol[i] == 'T':
            test.append(sol[i-1] **3)
        elif sol[i] == '*':
            if len(test) >1:
                test[-2] *=2
            test[-1] *=2
        elif sol[i] == '#':
            test[-1] *=-1 
    return sum(test)

a = "1S2D*3T"
print(dart(a))

#20200528
#해시함수 알기전 풀이) 프로그래머스 >해시 > 완주하지 못한 선수
def solution(participant, completion):
    answer = ''
    for i in completion:
        if i in participant:
            participant.remove(i)
    return participant

participant	=['mislav', 'stanko', 'mislav', 'ana']	
completion = ['stanko', 'ana', 'mislav']

#print(solution(participant, completion))

# 어차피 값은 하나이므로 정렬하여 남는 하나 뽑기
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

# collections 이용하기(대박...............)
# 리스트를 입력값으로 넣을시 딕셔너리 형태로 결과값 준다
# 값 = 개수형태로 입력이 가능하다
import collections

c = collections.Counter(a=2,b=3,c=4)
print(collections.Counter(c)) # Counter({'c': 4, 'b': 3, 'a': 2})
print(sorted(c))    #['a', 'b', 'c']
print(sorted(c.elements())) #['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']

# sorted(a) a.sort() 차이 = 전자는 리스트 정렬값을 반환/ 후자는 아예 a 를 다른 리스트로 바꿈
# 문자열 입력시 문자:개수 의 딕셔너리 형태로 반환해 준다
a = collections.Counter()
a.update("abcds")
# most_common : 빈도수(frequency)가 높은 순으로 상위 n개를 리스트(list) 안의 투플(tuple) 형태로 반환

answer = collections.Counter(participant) -collections.Counter(completion)
print(list(answer.keys())[0])

# 해시함수를 이용한 풀이 방법(....와)
def solution(participant,completion):
    answer=''
    temp=0
    dic={}

    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))

    for com in completion:
        dic[hash(com)] = com
        temp -= int(hash(com))    

    answer = dic[temp]
    return answer

print(solution(participant,completion))
