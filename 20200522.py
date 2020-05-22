# 1~n 사이의 수중에 소수 갯수 구하기
def solution(n):
    answer = 0
    if n ==1:
        return 0
    for i in range(n+1):
        cnt =0
        for j in range(n,0,-1):
            if i%j == 0:
                cnt +=1
        if cnt == 2 : 
            answer +=1
    return answer

#주어진배열에서 3개 수의 합이 소수인 경우의 수를 출력
def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                sum1 = nums[i]+nums[j]+nums[k]
                cnt =0
                for a in range(2,sum1+1):
                    if sum1%a==0:
                        cnt+=1
                if cnt==1:
                    answer +=1

    return answer

#문자열 유사도 
def solution(str1, str2):
    answer = 0
    arr1=[]
    arr2=[]
    
    #모두 소문자로바꾸기#문자열하나하나를원소로배열로만들기
    str1 = list(str1.lower())
    str2 = list(str2.lower())
    arr2 = str1 +str2
    #모든자리의수비교하기
    for i in range(len(str1)):
        for k in range(len(str2)):
            if str1[i] == str2[k]:
                arr1 += str1[i]
                
    print(arr1," ", arr2)
    #카운트해서 65536 곱하고 정수부만 출력
    answer = int((len(arr1)/len(arr2))*65536)
    return answer

print(solution("FRANCE","french"))
