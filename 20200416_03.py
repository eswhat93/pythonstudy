#프로그램의 구조를 쌓는다

money = True

if money:
    print('택시타고가')
else:
    print('걸어가')


money = 2000
if(money>3000):
    print('택시')
elif(money==2000):
    print('걸어')

card = True

if money>=3000:
    print('택시')
elif money==2000 and card:
    print('집에갈수있어')
else :
    print('dkdkdk')


pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket :
    print('그만둬')


if 'money' in pocket:pass
else:print('apssdsk')


#조건부 표현식
message = "조건부표현식" if money==2000 else "테스트안돼"
print(message)

#while문
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1 #treeHit +=1
    print("나무를 %d번 찍었습니다" %treeHit)
    if treeHit==10:
        print("넘어간다")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number=0
while number !=4:
    print(prompt)
    number = int(input())

#continue / break
#while True 무한루프
#https://wikidocs.net/22
