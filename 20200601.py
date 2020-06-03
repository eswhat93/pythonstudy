
#20200603
#해시 > 전화번호 목록 
import collections
def solution(phone_book):
    answer = False
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                print(phone_book[j][:len(phone_book[i])])
                answer = True      

    return answer

a=["119","1200","12074223","1195524421"]
print(solution(a))