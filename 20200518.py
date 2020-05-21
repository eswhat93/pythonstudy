#정수 n이 입력으로 주어졌을때 n을 1,2,3 의 합으로 나타낼 수 있는 방법의 수

#f(n) = f(n-1)+f(n-2)+f(n-3)
n =4
def f(data):
    if data < 0  : 
        return 0
    if data==0:
        return 1
    elif data==1:
        return 1
    elif data==2:
        return 2
    elif data==3:
        return 4

    return f(data -1) + f(data -2) + f(data -3)

print(f(10))

#20200519

#파이썬 기초 기본문제를 다시 풀어본다
#소수점 한자리
print(format(3.1111, ".1f"))
#형변환
string = "720"
print(type(int(string)))
print(type(str(string)))

#밑이 6이고 지수가2일때 거듭제곱 값
print(6**2)


#파이썬으로 엑셀만들기=>내일 연차때 해보기/ 예전에 회원가입시 메일보내는것도 다시 해보기
