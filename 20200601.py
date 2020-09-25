
#20200603
#해시 > 전화번호 목록 
import collections
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True


#20200605
#zip 과 startswith 메서드 사용
def solution(phone_book):
    for p1,p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True



#해쉬 이용해서 풀기
def solution(phone_book):
    hash_map={}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp !=phone_number:
                return False
    return True


# itertools의 combinations 모듈 사용하기
# itertools.combinations(char,2) 2개씩조합 뽑아줌 AC
# itertools.permutations(char,2) 2개씩 순열 AC CA

# sorted(list, key=len) => 길이 기준으로 정렬한다는 소리

from itertools import combinations as c
def solution(phone_book):
    sortedPB = sorted(phone_book, key=len)
    for (a,b) in c(sortedPB,2):
        print(a, b)
        if a == b[:len(a)]:
            return False
    return True

a=["119","12074223","1195524421","1200"]
print(solution(a))
def solution(clothes):
    answer = 1
    a=[]
    
    for i in range(len(clothes)):
        #kind 별 분리
        a.append(clothes[i][1])
    c = collections.Counter(a)

    for k,v in c.items():
        answer *= v
    return answer


test = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(test))